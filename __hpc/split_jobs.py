"""
splits jobs of the desired subdirectory level
"""
import os
from src.utils import traverse_level

in_dir = "../smart_initialization/community_detection/in"
# in_dir = "../experiments/spread_functions_correlation/in"
# in_dir = "../experiments/smart_initialization_comparison/in"
# in_dir = "../experiments/spread_functions_comparisons_ea/in"

split_level = 4

sub_directories = []
level_dirs = traverse_level(in_dir, split_level)
for lev_dir, _, _ in level_dirs:
	sub_directories.append(lev_dir)


n_cpus = 4
mem = 64
walltime = 100
queue = "common"


directory = in_dir.replace("..", "").replace("/", "_") + "_" + queue
if not os.path.exists(directory):
	os.makedirs(directory)

for sub_dir in sub_directories:
	if "amazon" in sub_dir:
		mem = 256
	shell_text = """#!/bin/bash

#PBS -l select=1:ncpus={}:mem={}gb

# set max execution time
#PBS -l walltime={}:00:0

# set the queue
#PBS -q {}_cpuQ
module load python-3.7.2
pip3.7 install inspyred --user
pip3.7 install networkx --user
pip3.7 install numpy --user
pip3.7 install node2vec --user
pip3.7 install community --user
pip3.7 install python-louvain --user
cd Influence-Maximization/src/
python3 experiments.py --exp_dir={} --hpc=True
	""".format(n_cpus, mem, walltime, queue, sub_dir)
	filename = sub_dir.replace(in_dir, "").replace("/", "_") + ".sh"
	with open(directory + "/" + filename, "w") as f:
		f.write(shell_text)
