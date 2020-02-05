#!/usr/bin/env python

import argparse
import sys

from .client import client


def main(*args):
    parser = argparse.ArgumentParser(
        description='Benchy client',
        prog=args[0],
    )
    parser.add_argument('--aio-worker-count', type=int, default=10)
    parser.add_argument('--times', type=int, default=10)
    parser.add_argument('--url', type=str, default='http://localhost:8001')

    arguments = parser.parse_args(args=args[1:])

    client(
        worker_count=arguments.aio_worker_count,
        times=arguments.times,
        url=arguments.url
    )


if __name__ == '__main__':
    main(*sys.argv[1:-1])
