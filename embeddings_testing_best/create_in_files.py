import os
import json
import itertools

from src.utils import make_dict_read_only, find_files


def default_values_dict():
	args = dict()
	args["k"] = 10
	args["p"] = 0.01
	args["spread_function"] = "monte_carlo_max_hop"
	args["no_simulations"] = 100
	args["max_hop"] = 3
	args["population_size"] = 100
	args["offspring_size"] = 100
	args["max_individual_copies"] = 100
	args["random_seed"] = 42
	args["max_generations"] = 100
	args["n_parallel"] = 1
	args["g_type"] = 'wiki'
	args["smart_initialization"] = "none"
	args["crossover_rate"] = 1.0
	args["mutation_rate"] = 0.1
	args["tournament_size"] = 5
	args["num_elites"] = 2
	args["min_degree"] = 0
	# global search only
	args["adaptive_local_rate"] = False
	args["local_search_rate"] = 1
	args["local_mutation_operator"] = "ea_local_embeddings_mutation"
	args["global_mutation_operator"] = "ea_global_random_mutation"

	return make_dict_read_only(args)


n_repetitions = 1

script = "evolutionary_algorithm_exec.py"

file_embeddings_to_test = find_files("../node2vec_embeddings_training_best/out/CA-GrQc")
# file_embeddings_to_test = find_files("../node2vec_embeddings_training/out/wiki")
files_prefix = "../experiments/"
file_embeddings_to_test = [f.replace("../", files_prefix) for f in file_embeddings_to_test]


# variables to track, keeping to defaults the others
#TODO: add embeddings files parameters
Node2vec_files = file_embeddings_to_test

variables = ['node2vec_file']
values = [Node2vec_files]

# variables to change for each experiment
#TODO: forse non serve il modello IC per amazon

models = ["WC", "IC"]
# graph_types = ["amazon"]
# graph_types = ["wiki"]
graph_types = ["CA-GrQc"]
K = [10, 20, 30, 40, 50]
# repeat for 3 different seeds to be sure the improvement is not due to a particular seed
random_seeds = range(3)

configs = list(itertools.product(*[graph_types, models, K, random_seeds]))
config_vars = ["g_type", "model", "k", "random_seed"]

# for each configuration
for config in configs:
	# change one variable at a time
	for var, var_values in zip(variables, values):
		# for each value of this variable
		for var_value in var_values:
			args = default_values_dict().get_copy()
			for c_value, c_var in zip(config, config_vars):
				args[c_var] = c_value
			args[var] = var_value
			# set in the experiments offspring size equal to the population size
			if var == "population_size":
				args["offspring_size"] = var_value

			# output file name suffix
			var_str = var_value.replace("/", "_")
			var_str = var_str.replace("..", "")
			var_str = var_str.replace(".", "_")
			# print(var_str)
			# exit(0)
			args["out_name"] = "{}_{}_".format(var, var_str)

			# write the input file
			in_dir = "./in/" + config[0] + "/" + var + "/" + config[1] + "/" + str(config[2]) + "/" + "{}".format(var_str)
			if not os.path.exists(in_dir):
				os.makedirs(in_dir)

			data = dict()
			data["script"] = script
			data["n_repetitions"] = n_repetitions
			data["script_args"] = args

			with open(in_dir + '/' + 'seed_{}_'.format(config[3]) + 'exp_in.json', 'w') as outfile:
				json.dump(data, outfile, indent=4)
