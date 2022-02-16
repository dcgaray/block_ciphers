import sys

from cbc import CBC
from ecb import EBC
from confid import condifidentialityLimits

def main():
    infile = sys.argv[1]
    #Task1
    EBC(infile)
    CBC(infile)
    #Task2 
    condifidentialityLimits()


if __name__ == "__main__":
    main()
