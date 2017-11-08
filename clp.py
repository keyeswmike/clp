import argparse
import os

## Create Parser object
parser = argparse.ArgumentParser(description="Sort by line. Reverse option")

## Create 'file' positional argument
parser.add_argument('file', metavar='FILE', type=file,
                    help='a file to be sorted')

## Create '--asort' option/flag
parser.add_argument('--asort', dest='asort', action='store_const',
                      const=True, help='boolean for ascending sorting')

## Create '--dsort' option/flag
parser.add_argument('--dsort', dest='dsort', action='store_const',
                      const=True, help='boolean for ascending sorting')

## Create '--reverse' option/flag
parser.add_argument('--reverse', dest='reverse', action='store_const',
                      const=True, help='boolean set to for reverse')


## Parse Argument Object
args = parser.parse_args()

if(args.asort):
    for line in sorted(args.file.readlines()):
        print line.rstrip()
elif(args.dsort):
    for line in reversed(sorted(args.file.readlines())):
        print line.rstrip()
elif(args.reverse):
    for line in reversed(args.file.readlines()):
        print line.rstrip()
else:
    for line in args.file.readlines():
        print line.rstrip()
