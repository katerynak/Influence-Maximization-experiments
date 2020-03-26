from src.plot import plot_dir, collect_results, plt_subplot
import matplotlib.pyplot as plt
import os
from itertools import product
import numpy as np


out_dirs = []
titles = []
res_dirs = []

mut = "local"

graph_types = ["wiki", "amazon", "CA-GrQc"]
models = ["WC", "IC"]
# variable_to_track = "smart_initialization"
# number of the best results to be selected

combs = product(*[graph_types, models])

for comb in combs:
	out_dirs.append("./out/{}/{}".format(comb[0], comb[1]))
	titles.append("{} {}".format(comb[0], comb[1]))
	res_dirs.append("./plots/local".format(mut))

for out_dir, title, res_dir in zip(out_dirs, titles, res_dirs):
	Y = ["best_fitness"]
	# Y = ["exec_time"]
	for y in Y:

		data2plot = collect_results(out_dir, "log", delimiter=";")

		var2plot = "k"

		F = "global_mutation_operator"
		F_values = sorted(data2plot[F].unique())
		print(F_values)

		x = sorted(data2plot[var2plot].unique())

		# select only the best results
		means_F = []
		for f_v in F_values:

			df = data2plot[data2plot[F] == f_v]
			mean = df.groupby(var2plot)[y].mean()[x].to_numpy()
			means_F.append(mean)

		# select only mutations with the highest means
		means_F = np.stack(means_F)
		means_F = np.mean(means_F, axis=1)

		F_values = np.array(F_values)

		for f_v in F_values:
			if mut in f_v:
				df = data2plot[data2plot[F]==f_v]
				mean = df.groupby(var2plot)[y].mean()[x].to_numpy()
				std = df.groupby(var2plot)[y].std()[x].to_numpy()
				plt.plot(x, mean, label=f_v)
				plt.fill_between(x, mean - std, mean + std, alpha=0.2)

		dataset = "amazon"
		if "wiki" in out_dir:
			dataset = "wiki"
		elif "CA-GrQc" in out_dir:
			dataset = "CA-GrQc"

		model = "IC"
		if "WC" in out_dir:
			model = "WC"
		out_dir = "../basic_ea/out/{}/{}".format(dataset, model)
		df = collect_results(out_dir, "log", delimiter=";")
		x = sorted(df[var2plot].unique())
		mean = df.groupby(var2plot)[y].mean()[x].to_numpy()
		std = df.groupby(var2plot)[y].std()[x].to_numpy()
		plt.plot(x, mean, label="basic_ea")

		plt.title(title)
		plt.ylabel("best fitness")
		plt.xlabel("seed set size")
		plt.legend(loc='best')

		if not os.path.exists(res_dir):
			os.makedirs(res_dir)

		plt.savefig(res_dir + "/" + title + "_" + y + ".pdf")

		plt.show()

	# variable_to_track2 = "best_nodes_percentage"
	#
	# combs = product(*[graph_types, models])
	#
	# out_dir="../best_spread_nodes/out/{}/{}/{}".format(comb[0], variable_to_track2, comb[1])
	#
	# for y in Y:
	#
	# 	data2plot = collect_results(out_dir, "log", delimiter=";")
	#
	# 	var2plot = "k"
	# 	F = variable_to_track2
	# 	F_values = [0.4]
	# 	# F_values = sorted(data2plot[F].unique())
	#
	# 	x = sorted(data2plot[var2plot].unique())
	#
	# 	# select only the best results
	# 	means_F = []
	# 	for f_v in F_values:
	# 		df = data2plot[data2plot[F] == f_v]
	# 		mean = df.groupby(var2plot)[y].mean()[x].to_numpy()
	# 		means_F.append(mean)
	#
	# 	# select only mutations with the highest means
	# 	means_F = np.stack(means_F)
	# 	means_F = np.mean(means_F, axis=1)
	# 	idx = np.argsort(means_F)[:n]
	#
	# 	F_values = np.array(F_values)
	# 	F_values = F_values[idx]
	#
	# 	for f_v in F_values:
	# 		df = data2plot[data2plot[F]==f_v]
	# 		mean = df.groupby(var2plot)[y].mean()[x].to_numpy()
	# 		std = df.groupby(var2plot)[y].std()[x].to_numpy()
	# 		plt.plot(x, mean, label="best spread nodes")
	# 		plt.fill_between(x, mean - std, mean + std, alpha=0.2)
	# 	plt.title(title)
	# 	plt.ylabel(y)
	# 	plt.xlabel(var2plot)
	# 	plt.legend(loc='best')
	#
	# if not os.path.exists(res_dir):
	# 	os.makedirs(res_dir)
	#
	# plt.savefig(res_dir + "/" + title + "_" + y + "_best{}".format(n) + ".pdf")
	#
	# plt.show()
