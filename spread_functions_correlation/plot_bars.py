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
			# "amazon",
			# "wiki",
			# "epinions"
			]

get_label = {"exec_time_mc_mean": "monte carlo", "exec_time_mh_mean": "monte carlo max hop",
			 "exec_time_th_mean": "two hop"}


vars = {"model": "WC", "k": 5}

mcmh_means = []
th_means = []
mc_means = []


for dataset in datasets:

	title = "{} {}".format(dataset, vars["model"])
	var2plot = "k"

	out_dir = "./out/{}/{}/".format(dataset, var2plot)

	df = collect_results(out_dir, csv_prefix="log", delimiter=",")

	for var in vars:
		df = df[df[var]==vars[var]]

	data2plot = df

	mcmh_means.append(df["exec_time_mh_mean"].mean())
	th_means.append(df["exec_time_th_mean"].mean())
	mc_means.append(df["exec_time_mc_mean"].mean())
	# mc_th_means.append(df["mc_th_corr"].mean())
	# mc_th_stds.append(df["mc_th_corr"].std())
#
# print(mc_mcmh_means)

labels = []

for d in datasets:
	d = d.replace("barabasi_albert", "b_a")
	d = d.replace("nodes_","")
	d = d.replace("n_edges_", "")
	labels.append(d)

x = np.arange(len(labels))  # the label locations
width = 0.3  # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(x - width, mc_means, width, label='Monte Carlo')
rects2 = ax.bar(x + width, mcmh_means, width, label='Monte Carlo max hop')
rects3 = ax.bar(x, th_means, width, label='2-hop')

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Runtime (s)')

ax.set_title('Runtimes under the WC model')
ax.set_xticks(x)
ax.set_xticklabels(labels)

fig.autofmt_xdate()
ax.legend()

fig.tight_layout()


res_dir = "./presentation/"

if not os.path.exists(res_dir):
	os.makedirs(res_dir)

filename = "WC_runtimes"

plt.savefig(res_dir + "/" + filename + ".pdf")

plt.show()
