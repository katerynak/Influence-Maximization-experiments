import os
import json
import itertools

from src.utils import make_dict_read_only


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
	args["g_type"] = 'amazon'
	args["smart_initialization"] = "none"
	args["crossover_rate"] = 1.0
	args["mutation_rate"] = 0.1
	args["tournament_size"] = 5
	args["num_elites"] = 2
	# args["min_degree"] = 0
	# global search only
	args["adaptive_local_rate"] = False
	args["local_search_rate"] = 0
	args["global_mutation_operator"] = "ea_global_random_mutation"

	return make_dict_read_only(args)


n_repetitions = 1

script = "evolutionary_algorithm_exec.py"

# variables to track, keeping to defaults the others

Min_degree = [0, 1, 2, 3, 4]

variables = ['min_degree']
values = [Min_degree]

# variables to change for each experiment
#TODO: forse non serve il modello IC per amazon

models = ["IC", "WC"]
graph_types = ["wiki", "amazon", 'CA-GrQc']
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
			args["out_name"] = "{}_{}_".format(var, var_value)

			# write the input file
			in_dir = "./in/" + config[0] + "/" + var + "/" + config[1] + "/" + str(config[2]) + "/" + "{}".format(var_value)
			if not os.path.exists(in_dir):
				os.makedirs(in_dir)

			data = dict()
			data["script"] = script
			data["n_repetitions"] = n_repetitions
			data["script_args"] = args

			with open(in_dir + '/' + 'seed_{}_'.format(config[3]) + 'exp_in.json', 'w') as outfile:
				json.dump(data, outfile, indent=4)