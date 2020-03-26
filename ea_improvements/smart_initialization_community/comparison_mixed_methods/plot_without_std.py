from src.plot import plot_dir, collect_results, plt_subplot
import matplotlib.pyplot as plt
import os
from itertools import product
import numpy as np


out_dirs = []
titles = []
res_dirs = []

graph_types = ["wiki", "CA-GrQc", "amazon"]
models = ["WC", "IC"]
variable_to_track = "smart_initialization_percentage"

combs = product(*[graph_types, models])

for comb in combs:
	out_dirs.append("./out/{}/{}/{}".format(comb[0], variable_to_track, comb[1]))
	titles.append("{} {}".format(comb[0], comb[1]))
	res_dirs.append("./plots/{}".format(comb[0]))


for out_dir, title, res_dir in zip(out_dirs, titles, res_dirs):
	Y = ["best_fitness"]
	print(title)
	for y in Y:

		data2plot = collect_results(out_dir, "log", delimiter=",")

		var2plot = variable_to_track

		F = "smart_initialization"
		F_values = sorted(data2plot[F].unique())

		data2plot = data2plot[data2plot["smart_initialization_percentage"]==0.5]

		x = sorted(data2plot[var2plot].unique())



		# print(F_values)

		# select only the best results
		means_F = []
		for f_v in F_values:
			df = data2plot[data2plot[F] == f_v]
			print(f_v)
			mean = df.groupby(var2plot)[y].mean().to_numpy()
			print(mean)
			means_F.append(mean)

		# select only mutations with the highest means
		means_F = np.stack(means_F)
		means_F = np.mean(means_F, axis=1)
		# idx = np.argsort(means_F)[:n]

		F_values = np.array(F_values)
		# F_values = F_values[idx]

		for f_v in F_values:
			df = data2plot[data2plot[F]==f_v]
			mean = df.groupby(var2plot)[y].mean()[x].to_numpy()
			std = df.groupby(var2plot)[y].std()[x].to_numpy()
			plt.plot(x, mean, label=f_v)
			# plt.fill_between(x, mean - std, mean + std, alpha=0.2)
		plt.title(title)
		plt.ylabel(y)
		plt.xlabel(var2plot)
		plt.legend(loc='best')

		if not os.path.exists(res_dir):
			os.makedirs(res_dir)

		plt.savefig(res_dir + "/" + title + "_" + y + ".pdf")

		plt.show()