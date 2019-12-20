import os
import json

import itertools
from src.utils import make_dict_read_only


def default_values_dict():
	args = dict()
	args["no_simulations"] = 100
	args["random_seed"] = 42

	return make_dict_read_only(args)

n_repetitions = 1

script="inf_max_comparison.py"

# variables to change for each experiment
graph_types = ["wiki", "epinions", "amazon", "CA-GrQc"]
K = list(range(10, 101, 10))
K = [str(k) for k in K]
models = ["IC", "WC"]
P = ['0.01']
heuristics = ["high_degree_nodes", "general_greedy", "CELF", "single_discount_high_degree_nodes",
			  "generalized_degree_discount"]

configs = list(itertools.product(*[graph_types, models, P, K, heuristics]))
config_vars = ["g_type", "model", "p", "k", "heuristic"]

# for each configuration
for config in configs:
	args = default_values_dict().get_copy()
	for c_value, c_var in zip(config, config_vars):
		args[c_var] = c_value

	# args["out_name"] = "_{}_{}_".format(var, var_value)

	# write the input file
	in_dir = "./in/" + config[0] + "/" + config[1] + "/" + config[2] + "/" + config[3] + "/" + config[4]
	if not os.path.exists(in_dir):
		os.makedirs(in_dir)

	data = dict()
	data["script"] = script
	data["n_repetitions"] = n_repetitions
	data["script_args"] = args

	with open(in_dir + '/' + 'seed_{}_'.format(args["random_seed"]) + 'exp_in.json', 'w') as outfile:
		json.dump(data, outfile, indent=4)
