#!/bin/bash


echo "~~~Running python encryption files~~~"
#if no args supplied, it'll just run the code
if [ $# -eq 0 ] 
    then
       echo "~~~No arguments supplied~~~"
       
fi
#if given an output file name, the code will run and create a result file
if [ $# -eq 1 ] 
then
    echo "running AES-EBC"
    python3 ecb.py $1
    echo "runnning AES-CBC"
    python3 cbc.py $1
fi

echo "~~~Finished running!~~~"


