#!/bin/bash

#PBS -l select=1:ncpus=8:mem=128gb

# set max execution time
#PBS -l walltime=100:00:0

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
python3 experiments.py --exp_dir=../experiments/ea_improvements/multiple_mutations_combined/in/CA-GrQc/exploration_weight/WC/30 --hpc=True & python3 experiments.py --exp_dir=../experiments/ea_improvements/multiple_mutations_combined/in/CA-GrQc/exploration_weight/WC/50 --hpc=True & python3 experiments.py --exp_dir=../experiments/ea_improvements/multiple_mutations_combined/in/CA-GrQc/moving_avg_len/IC/10 --hpc=True & python3 experiments.py --exp_dir=../experiments/ea_improvements/multiple_mutations_combined/in/CA-GrQc/moving_avg_len/IC/40 --hpc=True & python3 experiments.py --exp_dir=../experiments/ea_improvements/multiple_mutations_combined/in/CA-GrQc/moving_avg_len/IC/20 --hpc=True & python3 experiments.py --exp_dir=../experiments/ea_improvements/multiple_mutations_combined/in/CA-GrQc/moving_avg_len/IC/30 --hpc=True & python3 experiments.py --exp_dir=../experiments/ea_improvements/multiple_mutations_combined/in/CA-GrQc/moving_avg_len/IC/50 --hpc=True & python3 experiments.py --exp_dir=../experiments/ea_improvements/multiple_mutations_combined/in/CA-GrQc/moving_avg_len/WC/10 --hpc=True & 
wait