#!/usr/bin/env python

import argparse
import sys
import subprocess
import os


CURRENT_PATH = os.path.dirname(__file__)


def main(*args):
    parser = argparse.ArgumentParser(
        description='Benchy node server with fastify',
        prog=args[0],
    )
    arguments = parser.parse_args(args=args[1:])

    subprocess.run(
        [
            'node',
            'index',
        ],
        cwd=CURRENT_PATH,
    )


if __name__ == '__main__':
    main(*sys.argv[1:-1])
