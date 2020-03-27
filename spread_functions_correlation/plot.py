from src.plot import collect_results
import matplotlib.pyplot as plt
import numpy as np
import os


datasets = ["barabasi_albert_nodes_1000_n_edges_1",
			"barabasi_albert_nodes_1000_n_edges_3",
			"barabasi_albert_nodes_1000_n_edges_5",
			"barabasi_albert_nodes_1000_n_edges_7",
			"barabasi_albert_nodes_1000_n_edges_9",
			"barabasi_albert_nodes_1000_n_edges_11",
			"barabasi_albert_nodes_10000_n_edges_1",
			"barabasi_albert_nodes_10000_n_edges_3",
			"barabasi_albert_nodes_10000_n_edges_5",
			"barabasi_albert_nodes_10000_n_edges_7",
			"barabasi_albert_nodes_10000_n_edges_9",
			"barabasi_albert_nodes_10000_n_edges_11",
			"amazon",
			"wiki",
			"epinions"
			]

get_label = {"exec_time_mc_mean": "monte carlo", "exec_time_mh_mean": "monte carlo max hop",
			 "exec_time_th_mean": "two hop"}


vars = {"model": "WC"}

for dataset in datasets:

	title = "{} {}".format(dataset, vars["model"])
	var2plot = "k"

	out_dir = "./out/{}/{}".format(dataset, var2plot)

	df = collect_results(out_dir, csv_prefix="log", delimiter=",")

	for var in vars:
		df = df[df[var]==vars[var]]

	data2plot = df



	# Y = ["exec_time_mc_mean", "exec_time_mh_mean", "exec_time_th_mean"]
	# Y_std = ["exec_time_mc_std", "exec_time_mh_std", "exec_time_th_std"]

	Y = ["exec_time_mc_mean", "exec_time_mh_mean", "exec_time_th_mean"]
	Y_std = ["exec_time_mc_std", "exec_time_mh_std", "exec_time_th_std"]

	for y, y_std in zip(Y, Y_std):
		x = np.array(sorted(data2plot[var2plot].unique()))
		print(data2plot[y])
		mean = df.groupby(var2plot)[y].mean()[x].to_numpy()
		std = df.groupby(var2plot)[y].std()[x].to_numpy()
		# std = data2plot[y_std].mean()[x].to_numpy()

		label = get_label[y]
		plt.plot(x, mean, label = label)
		plt.fill_between(x, mean - std, mean + std, alpha=0.2)

	plt.title(title)
	plt.ylabel("exec_time")
	plt.xlabel(var2plot)
	plt.legend(loc='best')

	res_dir = "./summary_plots/k"

	if not os.path.exists(res_dir):
		os.makedirs(res_dir)

	plt.savefig(res_dir + "/" + title + "_" + y + ".pdf")

	plt.show()