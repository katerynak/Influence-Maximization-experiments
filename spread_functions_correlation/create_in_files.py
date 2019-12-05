import os
import json

from src.utils import make_dict_read_only


def default_values_dict():
	args = dict()
	args["k"] = 5
	args["p"] = 0.1
	args["n"] = 100
	args["no_simulations"] = 100
	args["max_hop"] = 2
	args["random_seed"] = 42
	args["g_nodes"] = 1000
	args["g_new_edges"] = 2
	args["g_type"] = 'barabasi_albert'
	args["g_seed"] = 0

	return make_dict_read_only(args)


n_repetitions = 1
random_seeds = range(10)

script="spread_computation.py"

K = range(1, 22, 2)
# G_nodes = [50, 100, 200, 500, 1000, 2000]
MC_simulations = [10, 50, 100, 500, 1000, 5000, 10000]

# vars = ["k", "g_nodes"]
# values = [K, G_nodes]

# g_types = ["wiki", "amazon"]

# g_types = ["epinions", "wiki", "amazon"]
# vars = ["k", "g_nodes"]
vars = ["no_simulations", "k"]
# g_types = ["barabasi_albert", "epinions", "wiki", "amazon"]
g_types = ["barabasi_albert"]
values = [MC_simulations, K]
G_nodes = [1000, 10000]
G_new_edges = range(1, 12, 2)

for g_type in g_types:
	for g_nodes in G_nodes:
		for g_new_edges in G_new_edges:
			for i, var in enumerate(vars):
				for value in values[i]:
					for model in ["IC", "WC"]:
					# for model in ["IC"]:
						for seed in random_seeds:
							args = default_values_dict().get_copy()
							args[var] = value
							args["model"] = model
							args["random_seed"] = seed
							args["g_type"] = g_type
							args["g_nodes"] = g_nodes
							args["g_new_edges"] = g_new_edges
							in_dir = "./in/" + args["g_type"] + "_nodes_{}_n_edges_{}".format(g_nodes, g_new_edges) \
									 + "/" + var + "/" + model + "/" + "{}".format(value)
							if not os.path.exists(in_dir):
								os.makedirs(in_dir)

							data = dict()
							data["script"] = script
							data["n_repetitions"] = n_repetitions
							data["script_args"] = args

							with open(in_dir + '/' + 'seed_{}_'.format(seed) + 'p_{}'.format(args["p"]) + 'exp_in.json', 'w') as outfile:
								json.dump(data, outfile, indent=4)

			# # WC specific
			# G_new_edges = range(1, 20, 2)
			#
			# for g_new_edges in G_new_edges:
			# 	for seed in random_seeds:
			# 		args = default_values_dict().get_copy()
			# 		args["g_new_edges"] = g_new_edges
			# 		args["random_seed"] = seed
			# 		args["model"] = "WC"
			# 		args["g_type"] = g_type
			# 		in_dir = "./in/" + args["g_type"] + "/" + "g_new_edges" + "/" + "WC" + "/" + "{}".format(g_new_edges)
			# 		if not os.path.exists(in_dir):
			# 			os.makedirs(in_dir)
			#
			# 		data = dict()
			# 		data["script"] = script
			# 		data["n_repetitions"] = n_repetitions
			# 		data["script_args"] = args
			#
			# 		with open(in_dir + '/' + 'seed_{}_'.format(seed) + 'exp_in.json', 'w') as outfile:
			# 			json.dump(data, outfile, indent=4)


			# IC specific
			P = [0.05, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6]
			for p in P:
				for seed in random_seeds:
					args = default_values_dict().get_copy()
					args["p"] = p
					args["random_seed"] = seed
					args["model"] = "IC"
					args["g_type"] = g_type
					args["g_nodes"] = g_nodes
					args["g_new_edges"] = g_new_edges
					in_dir = "./in/" + args["g_type"] + "_nodes_{}_n_edges_{}".format(g_nodes, g_new_edges) \
									 + "/" + "p" + "/" + "IC" + "/" + "{}".format(p)
					# in_dir = "./in/" + args["g_type"] + "/" + "p" + "/" + "IC" + "/" + "{}".format(p)
					if not os.path.exists(in_dir):
						os.makedirs(in_dir)

					data = dict()
					data["script"] = script
					data["n_repetitions"] = n_repetitions
					data["script_args"] = args

					with open(in_dir + '/' + 'seed_{}_'.format(seed) + 'exp_in.json', 'w') as outfile:
						json.dump(data, outfile, indent=4)

