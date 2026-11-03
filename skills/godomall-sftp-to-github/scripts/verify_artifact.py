"""Verify preserved artifact bytes without executing their contents."""
import argparse
import hashlib
import json
from pathlib import Path
from urllib.request import Request, urlopen


def compare(source, candidate, allow_trailing=False):
    exact = source == candidate
    prefix = bool(source) and candidate.startswith(source)
    return {
        'verified': exact or (allow_trailing and prefix),
        'exact': exact,
        'source_bytes': len(source),
        'candidate_bytes': len(candidate),
        'source_sha256': hashlib.sha256(source).hexdigest(),
        'candidate_sha256': hashlib.sha256(candidate).hexdigest(),
        'source_is_prefix': prefix,
        'trailing_bytes': len(candidate) - len(source) if prefix else None,
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('source', type=Path)
    target = parser.add_mutually_exclusive_group(required=True)
    target.add_argument('--url')
    target.add_argument('--file', type=Path)
    parser.add_argument('--allow-trailing-response', action='store_true', help='Diagnostic: accept source prefix plus extra response bytes.')
    args = parser.parse_args()
    source = args.source.read_bytes()
    if not source:
        parser.error('Source artifact is empty.')
    if args.url:
        if not args.url.startswith('https://'):
            parser.error('Use HTTPS.')
        with urlopen(Request(args.url, headers={'User-Agent': 'artifact-verifier/1.0'}), timeout=60) as response:
            candidate = response.read()
    else:
        candidate = args.file.read_bytes()
    result = compare(source, candidate, args.allow_trailing_response)
    print(json.dumps(result, indent=2))
    return 0 if result['verified'] else 1


if __name__ == '__main__':
    raise SystemExit(main())
