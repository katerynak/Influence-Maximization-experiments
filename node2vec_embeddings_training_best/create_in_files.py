import os
import json

import itertools
from src.utils import make_dict_read_only


def default_values_dict():
	args = dict()
	args["walk_length"] = 100
	args["num_walks"] = 10
	args["workers"] = 4
	args["window_size"] = 4
	args["iter"] = 1
	args["p"] = 1
	args["q"] = 1
	args["min_count"] = 1
	args["batch_words"] = 4

	args["random_seed"] = 42
	args["g_nodes"] = 1000
	args["g_new_edges"] = 2
	args["g_type"] = 'barabasi_albert'
	args["g_seed"] = 0

	return make_dict_read_only(args)


n_repetitions = 1

script="embeddings.py"

# variables to track, keeping to defaults the others
# Walk_length = [50, 80, 100]
# Window_size = [4, 10, 16]
# Iter = [1, 5, 10]
# # p =
# # q =
#
# variables = ['walk_length', 'window_size', 'iter']
# values = [Walk_length, Window_size, Iter]

# variables to change for each experiment
Dimensions = ['4', '8', '16', '32', '64', '128']
graph_types = ["CA-GrQc", "wiki", "amazon"]
# repeat for 5 different seeds to be sure the improvement is not due to a particular seed
random_seeds = range(5)

configs = list(itertools.product(*[graph_types, Dimensions, random_seeds]))
config_vars = ["g_type", "dimensions", "random_seed"]

# for each configuration
for config in configs:
			args = default_values_dict().get_copy()
			for c_value, c_var in zip(config, config_vars):
				args[c_var] = c_value
			args["out_name"] = "seed_{}_embedding.emb".format(config[2])

			# write the input file
			in_dir = "./in/" + config[0] + "/" + "dimensions_{}".format(config[1])
			if not os.path.exists(in_dir):
				os.makedirs(in_dir)

			data = dict()
			data["script"] = script
			data["n_repetitions"] = n_repetitions
			data["script_args"] = args

			with open(in_dir + '/' + 'seed_{}_'.format(config[2]) + 'exp_in.json', 'w') as outfile:
				json.dump(data, outfile, indent=4)
