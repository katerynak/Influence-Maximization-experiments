from src.plot import plot_dir, collect_results, plt_subplot
import matplotlib.pyplot as plt
import os

out_dirs = []
titles = []
res_dirs = []

out_dirs.append("./out/amazon/local_mutation_operator/WC")
titles.append("Amazon WC")
res_dirs.append("./plots/amazon")

out_dirs.append("./out/amazon/local_mutation_operator/IC")
titles.append("Amazon IC")
res_dirs.append("./plots/amazon")

out_dirs.append("./out/wiki/local_mutation_operator/WC")
titles.append("Wiki WC")
res_dirs.append("./plots/wiki")

out_dirs.append("./out/wiki/local_mutation_operator/IC")
titles.append("Wiki IC")
res_dirs.append("./plots/wiki")

out_dirs.append("./out/CA-GrQc/local_mutation_operator/IC")
titles.append("CA-GrQc IC")
res_dirs.append("./plots/CA-GrQc")

out_dirs.append("./out/CA-GrQc/local_mutation_operator/WC")
titles.append("CA-GrQc WC")
res_dirs.append("./plots/CA-GrQc")


for out_dir, title, res_dir in zip(out_dirs, titles, res_dirs):

	Y = ["best_fitness", "best_mc_spread"]
	# Y = ["exec_time"]
	for y in Y:

		data2plot = collect_results(out_dir, "log")

		def replace(x):
			if "ea_local_neighbors_random_mutation" in x:
				return "ea_local_neighbors_random_mutation"
			elif "ea_local_neighbors_second_degree_mutation" in x:
				return "ea_local_neighbors_second_degree_mutation"
			elif "ea_local_embeddings_mutation" in x:
				return "ea_local_embeddings_mutation"
			elif "ea_local_approx_spread_mutation" in x:
				return "ea_local_approx_spread_mutation"
			return x

		data2plot["local_mutation_operator"] = data2plot["local_mutation_operator"].apply(lambda x:  replace(x))
		var2plot = "k"
		F = "local_mutation_operator"
		F_values = sorted(data2plot[F].unique())
		# exit(0)

		x = sorted(data2plot[var2plot].unique())

		for f_v in F_values:
			df = data2plot[data2plot[F]==f_v]
			mean = df.groupby(var2plot)[y].mean()[x].to_numpy()
			std = df.groupby(var2plot)[y].std()[x].to_numpy()
			plt.plot(x, mean, label=f_v)
			plt.fill_between(x, mean - std, mean + std, alpha=0.2)
		plt.title(title)
		plt.ylabel(y)
		plt.xlabel(var2plot)
		plt.legend(loc='best')

		if not os.path.exists(res_dir):
			os.makedirs(res_dir)

		plt.savefig(res_dir + "/" + title + "_" + y + ".pdf")

		plt.show()
