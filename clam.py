#!/usr/bin/env python3.6

import argparse
from subprocess import run, PIPE
from tempfile import TemporaryDirectory
from pathlib import Path
from shutil import copy, make_archive

outname = Path('.').resolve().name.lower()
requirements = Path('./requirements.txt')
assert requirements.exists()

parser = argparse.ArgumentParser()
parser.add_argument('outname', nargs='?', help='Export to this filename (will append zip)', default=outname)
args = parser.parse_args()

with TemporaryDirectory() as tmp:
    print(f'Building in {tmp}')
    run(['pip', 'install', '-t', tmp, '-r', str(requirements)], check=True, stdout=PIPE, stderr=PIPE)

    for source in Path('.').glob('**/*.py'):
        dest = copy(source, tmp)
        print(f'Copied {source} -> {dest}')

    make_archive(args.outname, 'zip', tmp)

    print(f'Created {args.outname}.zip')
