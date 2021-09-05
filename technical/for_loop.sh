#!/bin/bash
### performs command line arguments over all files in the IN directory.

#choose the directory to loop through
IN=~/CESM/munged/LENS/TS

# perform the loop
for line in ${IN}/*; do
	echo "processing ${line}" # this line prints the names of the files to the command line.
	python3 ~/random_python/zonal_mean.py ${line} # this line 
done
