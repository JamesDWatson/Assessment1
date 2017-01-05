#!/usr/bin/env python
from argparse import ArgumentParser
from .graph import Greengraph
from matplotlib import pyplot as plt
#import pylab

def process():
    parser = ArgumentParser(description = "Generate greengraph")
    parser.add_argument('--start',  help='a starting location')
    parser.add_argument('--finish',  help='an end location')
    parser.add_argument('--steps', help='number of intermediate steps desired')
    parser.add_argument('--out', '-o', help='flag to print out graph')
    arguments= parser.parse_args()
    

    mygraph=Greengraph( arguments.start, arguments.finish)
    data = mygraph.green_between(arguments.steps)
    fig = plt.plot(data)
    fig = plt.savefig(arguments.out)
    #pylab.savfig(arguments.out)
    
    

if __name__ == "__main__":
    process() 
    