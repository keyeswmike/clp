import argparse

## Create Parser object
parser = argparse.ArgumentParser(description="Process some integers. ")


## Add arguments 'integers' and '--sum'
parser.add_argument('integers', metavar='N', type=int, nargs='+',
                    help='an integer for the accumulator')

parser.add_argument('--sum', dest='sum', action='store_const',
                    const=sum, default=max,
                    help='avg the integers (default: find the max)')

##
args = parser.parse_args()
print args.sum(args.integers)
