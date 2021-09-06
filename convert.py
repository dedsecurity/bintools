#!/usr/bin/python3

import argparse
import sys


def _convert(to_base, num):
    return to_base(int(num, 0))[2:]

def _test(bits, options):
    result = [options.prefix]
    if options.width:
        result.append('0' * max(0, options.width - len(bits)))
    result.append(bits)
    return ''.join(result)

def main(to_base, prefix, unit_name):
    parser = argparse.ArgumentParser()
    parser.add_argument('number', nargs='*', default=None)
    parser.add_argument(
        '-w',
        type=int,
        help=unit_name+' width to format as',
        metavar='WIDTH',
        dest='width')
    parser.add_argument(
        '-P',
        action='store_const',
        const='',
        default=prefix,
        help='disable `'+prefix+'` prefix',
        dest='prefix')
    options = parser.parse_args()

    if options.number:
        for number in options.number:
            print(_test(_convert(to_base, number), options))
    else:
        for line in sys.stdin:
            print(_test(_convert(to_base, line.strip()), options))
