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
	args["population_size"] = 2
	args["offspring_size"] = 2
	args["max_individual_copies"] = 100
	args["random_seed"] = 42
	args["max_generations"] = 100
	args["n_parallel"] = 1
	args["g_nodes"] = 100
	args["g_new_edges"] = 3
	args["g_seed"] = 0
	args["g_file"] = None
	args["g_type"] = 'amazon'
	args["out_file"] = None
	args["log_file"] = None
	args["generations_file"] = None
	args["smart_initialization"] = "degree_random"
	args["community_detection_algorithm"] = "louvain"
	args["n_clusters"] = 10
	args["smart_initialization_percentage"] = 1
	args["crossover_rate"] = 1.0
	args["mutation_rate"] = 0.1
	args["tournament_size"] = 5
	args["num_elites"] = 1
	args["min_degree"] = 1
	args["adaptive_local_rate"] = "False"
	args["local_mutation_operator"] = "ea_local_neighbors_random_mutation"
	args["global_mutation_operator"] = "ea_global_random_mutation"
	args["local_search_rate"] = 0
	args["mutators_to_alterate"] = [
		"ea_local_activation_mutation",
		'ea_local_neighbors_second_degree_mutation',
		"ea_local_embeddings_mutation",
		"ea_local_neighbors_random_mutation",
		"ea_local_approx_spread_mutation",
		"ea_global_activation_mutation",
		"ea_global_low_deg_mutation",
		"ea_global_random_mutation",
	]
	args["adaptive_mutations"] = True
	args["moving_avg_len"] = 10
	args["exploration_weight"] = 1 # dinamico
	args["node2vec_file"] = None
	args["best_nodes_percentage"] = 1 # da mettere automatico , opp mettere limite allo spazio di combinazioni
	args["filter_best_spread_nodes"] = True
	args["out_name"] = None

	args["dynamic_population"] = True

	return make_dict_read_only(args)

n_repetitions = 1

script = "evolutionary_algorithm_exec.py"

models = ["IC", "WC"]
graph_types = ["amazon", "wiki", 'CA-GrQc']


K = [10, 20, 30, 40, 50]
# repeat for 3 different seeds to be sure the improvement is not due to a particular seed
random_seeds = range(5)
# random_seeds = [0]

configs = list(itertools.product(*[graph_types, models, K, random_seeds]))
config_vars = ["g_type", "model", "k", "random_seed"]

# for each configuration
for config in configs:
			args = default_values_dict().get_copy()
			for c_value, c_var in zip(config, config_vars):
				args[c_var] = c_value

			# node2vec file with same params
			args["node2vec_file"] = "../experiments/node2vec_embeddings_training_best/out/{}/dimensions_128/seed_4_exp_" \
									   "in/repetition_0/embeddingsseed_4_embedding.emb.emb".format(config[0])

			# write the input file
			in_dir = "./in/" + config[0] + "/" + config[1] + "/" + str(config[2])
			if not os.path.exists(in_dir):
				os.makedirs(in_dir)

			data = dict()
			data["script"] = script
			data["n_repetitions"] = n_repetitions
			data["script_args"] = args

			with open(in_dir + '/' + 'seed_{}_'.format(config[3]) + 'exp_in.json', 'w') as outfile:
				json.dump(data, outfile, indent=4)
