#!/usr/bin/env python

import argparse
import sys
import threading


def main():
    parser = argparse.ArgumentParser(description='Benchy')
    parser.add_argument(
        'action',
        choices=[
            'remote_server',
            'test_01_ruby_puma',
            'test_02_nodejs',
            'client',
        ]
    )
    parser.add_argument('rest', nargs=argparse.REMAINDER)

    arguments = parser.parse_args()
    mod = __import__(arguments.action)
    mod.main(sys.argv[0], *arguments.rest)


if __name__ == '__main__':
    main()
