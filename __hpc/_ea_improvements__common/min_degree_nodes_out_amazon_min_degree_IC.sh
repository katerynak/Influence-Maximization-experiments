#!/bin/bash

#PBS -l select=1:ncpus=1:mem=32gb

# set max execution time
#PBS -l walltime=30:00:0

# set the queue
#PBS -q common_cpuQ
module load python-3.7.2
# pip3.7 install inspyred --user
# pip3.7 install networkx --user
# pip3.7 install numpy --user
# pip3.7 install node2vec --user
# pip3.7 install community --user
# pip3.7 install python-louvain --user
cd Influence-Maximization/src/
python3 experiments.py --exp_dir=../experiments/ea_improvements/min_degree_nodes/out/amazon/min_degree/IC --hpc=True
	