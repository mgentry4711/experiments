#!/bin/bash
#SBATCH --job-name=mpi_job
#SBATCH --account=P93300065
#SBATCH --ntasks=8
#SBATCH --ntasks-per-node=4
#SBATCH --time=00:10:00
#SBATCH --partition=dav
#SBATCH --output=mpi_job.out.%j

### performs command line arguments over all files in the IN directory.
### the #SBATCH options specify job parameters

#choose the directory to loop through
IN=~/CESM/munged/LENS/TS

# perform the loop 
for line in ${IN}/*; do
        echo "processing ${line}" # this line prints the names of the files to the command line.
        python3 ~/random_python/zonal_mean.py ${line} # this line 
done
