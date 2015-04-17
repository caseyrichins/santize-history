#!/usr/bin/python

__author        = "Casey Richins"
__copyright__   = "Copyright 2015, Casey Richins"
__email__       = "casey@richinsconsulting.com"
__status__      = "Prototype"

import os, sys, argparse

parser = argparse.ArgumentParser(
                prog='sanitze_history.py',
                description='A simple script to check ssh credentials imported from csv file.',
                epilog='''This program is distributed in the hope that it will be useful,
                but WITHOUT ANY WARRANTY; without even the implied warranty of
                MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. The author is not liable for
                issues arising from loss of data or other unexpected destruction or malice.''')
parser.add_argument('-w', '--word', dest='WORD', help='Specify word or phrase to search for.')
parser.add_argument('-r', '--range', dest='RANGE', help='Specify range of entries to remove.')
parser.add_argument('-l', '--logfile', dest='LOG', help='Location of logfile for %(prog)s output')
parser.add_argument('-V', '--version', action='version', version='%(prog)s 0.1_beta')
args = parser.parse_args()

if args.WORD is not None:
    print "Word Search: ", args.WORD, "\r"
    search = os.system("history | grep args.WORD | awk {'print $1'}")
    for i in search:
        print i
#        os.system("history -d i")

if args.RANGE is not None:
    print "Range: ", args.RANGE, "\r"
    for i in xrange(args.RANGE):
        history -d i

