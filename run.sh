#!/bin/bash

echo "Running main.py"

if [ $# -eq 0 ]
    then
        echo "No arguments supplied"
fi
if [ $# -eq 1 ]
    then
    python3 main.py > $1.out
    echo "Results sent out to $1.out"
fi

echo "Finished running!"


