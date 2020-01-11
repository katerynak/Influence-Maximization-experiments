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
python3 experiments.py --exp_dir=../experiments/embeddings_testing/in/wiki/node2vec_file/WC/30/_experiments_node2vec_embeddings_training_out_wiki_window_size_dimensions_8_16_seed_3_exp_in_repetition_0_embeddings_window_size_16__emb --hpc=True
	