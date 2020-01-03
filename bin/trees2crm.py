### importing packages
import argparse

### importing crm
from crm import getEK_trees, read_trees, write_crm

### parse arguments
parser=argparse.ArgumentParser()
parser.add_argument('--input', type = str, help='input and output file name')

args = vars(parser.parse_args())
args = dict((k,v) for k,v in args.items() if v is not None)

input = args["input"]
output = input[:-6]

### 
trees = read_trees(input)
crm = getEK_trees(trees)

write_crm(crm, output)
