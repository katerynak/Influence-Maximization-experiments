#!/bin/bash

#PBS -l select=1:ncpus=8:mem=32gb

# set max execution time
#PBS -l walltime=6:00:0

# set the queue
#PBS -q short_cpuQ
module load python-3.7.2
# pip3.7 install inspyred --user
# pip3.7 install networkx --user
# pip3.7 install numpy --user
# pip3.7 install node2vec --user
# pip3.7 install community --user
# pip3.7 install python-louvain --user
cd Influence-Maximization/src/
python3 experiments.py --exp_dir=../experiments/ea_improvements_tiny_datasets/min_degree_nodes/in/tiny_amazon/min_degree/IC/3 --hpc=True & python3 experiments.py --exp_dir=../experiments/ea_improvements_tiny_datasets/min_degree_nodes/in/tiny_amazon/min_degree/IC/2 --hpc=True & python3 experiments.py --exp_dir=../experiments/ea_improvements_tiny_datasets/min_degree_nodes/in/tiny_amazon/min_degree/WC/3 --hpc=True & python3 experiments.py --exp_dir=../experiments/ea_improvements_tiny_datasets/min_degree_nodes/in/tiny_amazon/min_degree/WC/2 --hpc=True & python3 experiments.py --exp_dir=../experiments/ea_improvements_tiny_datasets/min_degree_nodes/in/tiny_wiki_community/min_degree/IC/3 --hpc=True & python3 experiments.py --exp_dir=../experiments/ea_improvements_tiny_datasets/min_degree_nodes/in/tiny_wiki_community/min_degree/IC/2 --hpc=True & python3 experiments.py --exp_dir=../experiments/ea_improvements_tiny_datasets/min_degree_nodes/in/tiny_wiki_community/min_degree/WC/3 --hpc=True & python3 experiments.py --exp_dir=../experiments/ea_improvements_tiny_datasets/min_degree_nodes/in/tiny_wiki_community/min_degree/WC/2 --hpc=True & 
wait