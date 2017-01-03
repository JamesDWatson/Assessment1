#!/usr/bin/env python
from argparse import ArgumentParser
if __name__ == "__main__":
    parser = ArgumentParser(description = "Generate greengraph")
    parser.add_argument('--start', action="store_true", help='a starting location')
    parser.add_argument('--to', action="store_true", help='an end location')
    parser.add_argument('--steps','-steps', action="store_true", help='number of intermediate steps desired')
    parser.add_argument('--out', '-o', help='flag to print out graph')
    arguments= parser.parse_args()
    
from greengraph import Greengraph
    mygraph=Greengraph( arguments.--start, arguments.--to)
    data = mygraph.green_between(arguments.--steps)
    plt.plot(data)
    pylab.savfig(arguments.--out)
    