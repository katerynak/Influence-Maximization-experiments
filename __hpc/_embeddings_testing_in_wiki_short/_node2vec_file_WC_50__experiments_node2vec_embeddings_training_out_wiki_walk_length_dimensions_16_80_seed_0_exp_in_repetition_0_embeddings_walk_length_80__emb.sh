#!/bin/bash

#PBS -l select=1:ncpus=4:mem=32gb

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
python3 experiments.py --exp_dir=../experiments/embeddings_testing/in/wiki/node2vec_file/WC/50/_experiments_node2vec_embeddings_training_out_wiki_walk_length_dimensions_16_80_seed_0_exp_in_repetition_0_embeddings_walk_length_80__emb --hpc=True
	