from src.plot import plot_dir, collect_results, plt_subplot
import matplotlib.pyplot as plt
import os
from itertools import product

datasets = ["CA-GrQc", "wiki", "amazon"]
models = ["IC", "WC"]

# experiments = ["basic_ea", "selected_config", "all_combined", "multiple_mutations", "best_spread_nodes"]
# experiments = ["all_combined", "selected_config", "basic_ea"]
experiments = ["multiple_mutations", "basic_ea"]

labels = {"all_combined": "all_features", "selected_config": "selected_features", "basic_ea": "basic_GA"}

heuristics = False

for dataset, model in product(*[datasets, models]):

		# Y = ["best_mc_spread"]
		Y = ["best_fitness"]
		# Y = ["exec_time"]
		title = "{} {}".format(dataset, model)
		res_dir = "./plots/multiple_mutations"
		var2plot = "k"

		for y in Y:
			for experiment in experiments:
				if dataset=="wiki" and experiment == "all_combined":
					print("ee")
				else:
					# for out_dir, title, res_dir in zip(out_dirs, titles, res_dirs):
					out_dir = "./{}/out/{}/{}".format(experiment, dataset, model)
					df = collect_results(out_dir, "log", delimiter=";")
					x = sorted(df[var2plot].unique())
					mean = df.groupby(var2plot)[y].mean()[x].to_numpy()
					std = df.groupby(var2plot)[y].std()[x].to_numpy()
					# label = labels[experiment]
					label = experiment
					plt.plot(x, mean, label=label)
					if experiment != "all_combined" or dataset == "amazon":
						plt.fill_between(x, mean - std, mean + std, alpha=0.2)
					else:
						plt.fill_between(x, mean - std, mean + std, alpha=0)
			if heuristics:
				out_dir = "../heuristics_comparison/out/{}/{}/".format(dataset, model)
				data2plot = collect_results(out_dir, "log", delimiter=";")
				# data2plot = data2plot[data2plot["heuristic"] == "CELF"]
				print(data2plot["influence_spread"])
				data2plot["influence_spread"] = data2plot["influence_spread"].apply(lambda x: float(x.split(",")[0][1:]))

				F = "heuristic"
				F_values = sorted(["CELF", "high_degree_nodes"])
				# F_values = ["general_greedy"]

				for f_v in F_values:

					df = data2plot[data2plot[F] == f_v]
					# mean = df.groupby(var2plot)["influence_spread"].mean()[x].to_numpy()
					# std = df.groupby(var2plot)["influence_spread"].std()[x].to_numpy()
					mean = df.groupby(var2plot)["exec_time"].mean()[x].to_numpy()
					std = df.groupby(var2plot)["exec_time"].std()[x].to_numpy()
					plt.plot(x, mean, label=f_v)
					plt.fill_between(x, mean - std, mean + std, alpha=0.2)
			plt.title(title)
			plt.ylabel("best fitness")
			plt.xlabel("seed set size")
			plt.legend(loc='best')

			if not os.path.exists(res_dir):
				os.makedirs(res_dir)

			plt.savefig(res_dir + "/" + title + "_" + y + ".pdf")

			plt.show()