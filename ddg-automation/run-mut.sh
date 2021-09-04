#!/bin/bash
#PBS -l select=1:ncpus=40:mpiprocs=40:ompthreads=1:jobtype=small
#PBS -l walltime=120:00:00

python {{PATH_TO_RESIDUE_DDG}}/run_example_2_saturation.py
