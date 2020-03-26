from src.plot import plot_dir, collect_results, plt_subplot
import matplotlib.pyplot as plt
import os
import itertools
import time


titles = []
res_dirs = []

K = [10, 20, 30, 40, 50]
models = ['IC', 'WC']
# datasets = ["amazon", "wiki", "CA-GrQc"]
datasets = ["wiki", "CA-GrQc"]
methods = ["smart_initialization"]


configs = list(itertools.product(*[datasets, methods, models, K]))
for config in configs:
	# if config[1] == methods[0]:
	# 	values = [False, True]
	# elif config[1] == methods[1]:
	# 	values = [0, 0.2, 0.4, 0.6, 0.8, 1]
	values = ["betweenness", "closeness", "degree", "eigenvector", "katz"]
	out_dirs = []
	for value in values:
		out_dirs.append("./out/{}/{}/{}/{}/{}".format(config[0],
													config[1],
													config[2],
													config[3],
													value))
	title = "{} {} {} k={}".format(config[0], config[1], config[2], config[3])
	res_dir = "./plots/generations/{}".format(config[0])

	for out_dir in out_dirs:

		Y = [" diversity"]
		for y in Y:

			data2plot = collect_results(out_dir, "population")
			print(data2plot)
			exit(0)

			#

			var2plot = "generation number"

			print(data2plot.columns)
			# diversity = data2plot[" std"].str.split(pat='.').str[-1]
			#
			# diversity = '0.' + diversity.astype(str)
			#
			# diversity = diversity.str.replace('0.nan', 'nan')
			#
			# diversity = diversity.astype(float)
			# data2plot[" diversity"] = diversity

			print(data2plot[" diversity"])
			# print(data2plot[" std"].str.replace('.', ' '))
			# data2plot[" diversity"] = data2plot[" std"]
			# F = "global_mutation_operator"
			# F_values = sorted(data2plot[F].unique())
			# exit(0)
			# print(data2plot.columns)
			x = sorted(data2plot[var2plot].unique())

			# for f_v in F_values:
			# 	df = data2plot[data2plot[F]==f_v]
			mean = data2plot.groupby(var2plot)[y].mean()[x].to_numpy()
			std = data2plot.groupby(var2plot)[y].std()[x].to_numpy()
			plt.plot(x, mean, label=out_dir.split('/')[-1])
			plt.fill_between(x, mean - std, mean + std, alpha=0.2)
			plt.title(title)
			plt.ylabel(y)
			plt.xlabel(var2plot)
			plt.legend(loc='best')

	if not os.path.exists(res_dir):
		os.makedirs(res_dir)

	plt.savefig(res_dir + "/" + title + "_" + y + ".pdf")

	time.sleep(1)
	plt.show()
