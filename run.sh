#!/bin/bash

echo "~~~Running main.py~~~"
#if no args supplied, it'll just run the code
if [ $# -eq 0 ] 
    then
        echo "~~~No arguments supplied~~~"
        python3 main.py
fi

#if given an output file name, the code will run and create a result file
if [ $# -eq 1 ] 
then
    python3 main.py > $1.out
    echo "~~~Results sent out to $1.out~~~"
fi

echo "~~~Finished running!~~~"


