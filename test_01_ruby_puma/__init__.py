#!/usr/bin/env python

import argparse
import sys
import subprocess
import os


CURRENT_PATH = os.path.dirname(__file__)


def main(*args):
    parser = argparse.ArgumentParser(
        description='Benchy ruby server with puma',
        prog=args[0],
    )
    parser.add_argument('--host', type=str, default='0.0.0.0')
    parser.add_argument('--port', type=int, default='8001')
    parser.add_argument('--workers', type=str, default='1')
    parser.add_argument('--threads', type=str, default='16')
    parser.add_argument(
        '--target-uri', type=str, default='http://3.81.93.61:8001'
    )
    arguments = parser.parse_args(args=args[1:])
    inherited_environ = dict(os.environ)
    inherited_environ.update({'REMOTE_ENDPOINT': arguments.target_uri})

    subprocess.run(
        [
            'puma',
            '-w',
            arguments.workers,
            '-t',
            arguments.threads,
            '-b',
            f'tcp://{arguments.host}:{arguments.port}',
        ],
        cwd=CURRENT_PATH,
        env=inherited_environ
    )


if __name__ == '__main__':
    main(*sys.argv[1:-1])
