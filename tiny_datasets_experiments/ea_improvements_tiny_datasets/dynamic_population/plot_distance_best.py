from src.plot import plot_dir, collect_results, plt_subplot
import matplotlib.pyplot as plt
import os
from itertools import product


def get_best_fitness(dataset_name, model, k, spread_function="monte_carlo", g_nodes=100):
	"""
	returns fitness of the best individual
	:param dataset_name:
	:param model:
	:param k:
	:param spread_function:
	:param g_nodes:
	:return:
	"""
	ground_truth_name = dataset_name.replace("tiny", "Tiny")
	ground_truth_name += "_{}nodes_seed0_{}_k{}_{}.pickle".format(g_nodes, model, k, spread_function)
	ground_truth_name = "../../ground_truth/" + ground_truth_name

	import pickle
	with open(ground_truth_name, 'rb') as handle:
		scores = pickle.load(handle)
	best_result = scores[list(scores.keys())[0]]
	best_spread = best_result[0]
	return best_spread

graph_types = ["tiny_wiki", "tiny_amazon", 'tiny_CA-GrQc',
			   "tiny_wiki_community", "tiny_amazon_community", 'tiny_CA-GrQc_community']
models = ["WC", "IC"]

variable_to_track = "dynamic_population"

out_dirs = []
titles = []
res_dirs = []

combs = product(*[graph_types, models])

for comb in combs:
	out_dirs.append("./out/{}/{}/{}".format(comb[0], variable_to_track, comb[1]))
	titles.append("{} {}".format(comb[0], comb[1]))
	res_dirs.append("./plots/{}".format(comb[0]))


for out_dir, title, res_dir in zip(out_dirs, titles, res_dirs):
	Y = ["relative_score", "best_mc_spread"]
	data2plot = collect_results(out_dir, "log", delimiter=";")
	dataset, model = title.split(" ")

	for k in [2, 3]:
		best_fitness = get_best_fitness(dataset, model, k, "monte_carlo", 100)
		df1 = data2plot[data2plot["k"] == k]
		F = variable_to_track
		F_values = sorted(data2plot[F].unique())
		means = []
		stds = []
		for fv in F_values:
			df = df1[df1[F] == fv]
			# compute relative best
			best_relative_spread = df["best_mc_spread"]
			relative_mc_spread = (best_fitness - best_relative_spread)/best_fitness
			means.append(relative_mc_spread.mean())
			stds.append(relative_mc_spread.std())
		fig, ax = plt.subplots()
		labels = [str(fv) for fv in F_values]
		ax.bar(labels, means, yerr=stds)

		ax.set(xticks=labels, xticklabels=labels)
		fig.autofmt_xdate()
		plt.title(title + " k=" + str(k))
		ylab = "fitness_distance_from_best"
		plt.ylabel(ylab)

		if not os.path.exists(res_dir):
			os.makedirs(res_dir)
		plt.savefig(res_dir + "/" + title + "_" + ylab + "_k" + str(k) + ".pdf")
		plt.show()
