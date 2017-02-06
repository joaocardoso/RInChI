#!/usr/bin/env python3
"""
RInChI addition script

This script analyses flat files of RInChIs separated by newlines.

    C.H.G. Allen 2012
    D.F. Hampshire 2016- Rewritten to use argparse module and Python3

"""

import argparse

from rinchi_tools import tools, utils

# TODO refactor into a more logical command line call interface

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="RInChI addition \n{}".format(__doc__))
    parser.add_argument("input_path", help="Path of file to input")
    parser.add_argument("-o","--output_name",default='file',help="Optionally specify the file output name")
    action = parser.add_mutually_exclusive_group()
    action.add_argument("-f", "--fileout", action="store_false", help="Output to file instead of printing")
    args = parser.parse_args()
    if args.input_path:
        input_file = open('%s' % args.input_path).read()
        input_rinchis = input_file.strip().splitlines()
        overall_rinchi = tools.add(input_rinchis)
        utils.output(overall_rinchi,args.output_name, "rinchi")
