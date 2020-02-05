#!/usr/bin/env python

import argparse
import sys

from .app import app


def main(*args):
    parser = argparse.ArgumentParser(
        description='Benchy remote server',
        prog=args[0],
    )
    parser.add_argument('--host', type=str, default='0.0.0.0')
    parser.add_argument('--port', type=int, default='8000')
    arguments = parser.parse_args(args=args[1:])
    app.run(host=arguments.host, port=arguments.port)


if __name__ == '__main__':
    main(*sys.argv[1:-1])
