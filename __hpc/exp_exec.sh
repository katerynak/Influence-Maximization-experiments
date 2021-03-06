#!/bin/bash

# set the number of nodes and the RAM and the core used by th nodes
# In the example 4 cores and 10 GB of RAM for each of the 1 nodes

#PBS -l select=1:ncpus=4:mem=128gb

# set max execution time
#PBS -l walltime=24:00:0

# set the queue
#PBS -q common_cpuQ
module load python-3.7.2
pip3.7 install inspyred --user
pip3.7 install networkx --user
pip3.7 install numpy --user
pip3.7 install node2vec --user
pip3.7 install community --user
pip3.7 install python-louvain --user
cd Influence-Maximization/src/
#python3 experiments.py --exp_dir=../experiments/test --hpc=True
python3 embeddings.py