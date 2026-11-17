#!/usr/bin/env python3
"""Compare every retained Pika path with the pinned official free package."""
import hashlib
import io
import json
from pathlib import Path
import re
import tarfile
import urllib.request

ROOT = Path(__file__).resolve().parent
source = json.loads((ROOT / 'PIKA-UPSTREAM.json').read_text(encoding='utf-8'))
with urllib.request.urlopen(source['archive_url'], timeout=30) as response:
    archive = response.read()
assert hashlib.sha256(archive).hexdigest() == source['archive_sha256'], 'Upstream archive changed'
with tarfile.open(fileobj=io.BytesIO(archive), mode='r:gz') as package:
    upstream = package.extractfile('package/dist/index.js').read().decode()
    metadata = json.load(package.extractfile('package/package.json'))
    license_text = package.extractfile('package/LICENSE').read().decode()
assert (metadata['name'], metadata['version']) == (source['package'], source['version'])
assert (ROOT / source['license_file']).read_text(encoding='utf-8').strip() == license_text.strip(), 'MIT notice changed'

exports = {}
for line in upstream.splitlines():
    match = re.fullmatch(r'export const (\w+) = (.+);', line)
    if match:
        exports[match[1]] = json.loads(match[2])


def tokens(path):
    return re.findall(r'[A-Za-z]|[-+]?(?:\d*\.\d+|\d+)(?:[eE][-+]?\d+)?', path)


assert tokens('M1 23') != tokens('M12 3')
assert tokens('M1,2 L3 4') == tokens('M1 2L3,4')


def upstream_paths(nodes):
    paths = []
    for node in nodes:
        if node[0] == 'path':
            paths.append(tokens(node[1]['d']))
        if len(node) > 2:
            paths.extend(upstream_paths(node[2]))
    return paths


def check(text, export, label):
    paths = [tokens(path) for path in re.findall(r'\bd="([^"]+)"', text)]
    assert paths == upstream_paths(exports[export]), f'Pika source mismatch: {label}'


icons = ROOT / 'src/pika/icons'
assert {file.name for file in icons.glob('*.tsx')} == set(source['icons']), 'Unchecked Pika icon file'
for filename, export in source['icons'].items():
    check((icons / filename).read_text(encoding='utf-8'), export, filename)
for item in source['embedded']:
    text = (ROOT / item['file']).read_text(encoding='utf-8')
    if 'function' in item:
        match = re.search(r'export function ' + re.escape(item['function']) + r'\b[\s\S]*?(?=\nexport function |\Z)', text)
        assert match, f'Missing embedded icon: {item["function"]}'
        text = match.group()
    check(text, item['export'], item['file'])
print(f'Verified {len(source["icons"])} standalone and {len(source["embedded"])} embedded Pika icons against {source["package"]}@{source["version"]}; complete MIT notice matches.')
