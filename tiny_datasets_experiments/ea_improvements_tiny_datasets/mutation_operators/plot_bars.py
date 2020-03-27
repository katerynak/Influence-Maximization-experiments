from src.plot import plot_dir, collect_results, plt_subplot
import matplotlib.pyplot as plt
import os
from itertools import product

graph_types = ["tiny_wiki", "tiny_amazon", 'tiny_CA-GrQc',
			   "tiny_wiki_community", "tiny_amazon_community", 'tiny_CA-GrQc_community']
models = ["WC", "IC"]

variable_to_track = "mutators_to_alterate"

out_dirs = []
titles = []
res_dirs = []

combs = product(*[graph_types, models])

for comb in combs:
	out_dirs.append("./out/{}/{}/{}".format(comb[0], variable_to_track, comb[1]))
	titles.append("{} {}".format(comb[0], comb[1]))
	res_dirs.append("./plots/{}".format(comb[0]))


for out_dir, title, res_dir in zip(out_dirs, titles, res_dirs):
	Y = ["best_mc_spread"]
	data2plot = collect_results(out_dir, "log", delimiter=";")
	for k in [2, 3]:
		for y in Y:
			df1 = data2plot[data2plot["k"] == k]
			F = variable_to_track
			F_values = sorted(data2plot[F].unique())
			means = []
			stds = []
			for fv in F_values:
				df = df1[df1[F] == fv]
				means.append(df[y].mean())
				stds.append(df[y].std())
			fig, ax = plt.subplots()
			ax.bar(F_values, means, yerr=stds)
			ax.set(xticks=F_values, xticklabels=F_values)
			fig.autofmt_xdate()
			plt.title(title + " k=" + str(k))
			plt.ylabel(y)
			plt.tight_layout()

			if not os.path.exists(res_dir):
				os.makedirs(res_dir)
			plt.savefig(res_dir + "/" + title + "_" + y + "_k" + str(k) + ".pdf")
			plt.show()
