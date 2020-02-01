from src.plot import plot_dir, collect_results, plt_subplot
import matplotlib.pyplot as plt
import os
import  pandas as pd

out_dirs = []
titles = []
res_dirs = []

# out_dirs.append("./out/amazon/moving_avg_len/WC")
# titles.append("Amazon WC")
# res_dirs.append("./plots/amazon")
#
# out_dirs.append("./out/amazon/moving_avg_len/IC")
# titles.append("Amazon IC")
# res_dirs.append("./plots/amazon")
# #
# out_dirs.append("./out/wiki/moving_avg_len/WC")
# titles.append("Wiki WC")
# res_dirs.append("./plots/wiki")
#
# out_dirs.append("./out/wiki/moving_avg_len/IC")
# titles.append("Wiki IC")
# res_dirs.append("./plots/wiki")
#
# out_dirs.append("./out/CA-GrQc/moving_avg_len/IC")
# titles.append("CA-GrQc IC")
# res_dirs.append("./plots/CA-GrQc")
#
# out_dirs.append("./out/CA-GrQc/moving_avg_len/WC")
# titles.append("CA-GrQc WC")
# res_dirs.append("./plots/CA-GrQc")

# out_dirs.append("./out/amazon/exploration_weight/WC")
# titles.append("Amazon WC")
# res_dirs.append("./plots/amazon")

# out_dirs.append("./out/amazon/exploration_weight/IC")
# titles.append("Amazon IC")
# res_dirs.append("./plots/amazon")
#
# out_dirs.append("./out/wiki/exploration_weight/WC")
# titles.append("Wiki WC")
# res_dirs.append("./plots/wiki")
#
# out_dirs.append("./out/wiki/exploration_weight/IC")
# titles.append("Wiki IC")
# res_dirs.append("./plots/wiki")
#
# out_dirs.append("./out/CA-GrQc/exploration_weight/IC")
# titles.append("CA-GrQc IC")
# res_dirs.append("./plots/CA-GrQc")
#
out_dirs.append("./out/CA-GrQc/exploration_weight/WC")
titles.append("CA-GrQc WC")
res_dirs.append("./plots/CA-GrQc")


for out_dir, title, res_dir in zip(out_dirs, titles, res_dirs):

	# Y = ["best_mc_spread"]
	Y = ["best_fitness"]
	# Y = ["exec_time"]
	for y in Y:

		data2plot = collect_results(out_dir, "log", delimiter=';')
		# data2plot2append = collect_results(out_dir.replace("moving_avg_len", "exploration_weight"), "log")
		# li = [data2plot, data2plot2append]
		li = [data2plot]
		data2plot = pd.concat(li, axis=0, ignore_index=True)


		# def replace(x):
		# 	if "ea_local_neighbors_random_mutation" in x:
		# 		return "ea_local_neighbors_random_mutation"
		# 	elif "ea_local_neighbors_second_degree_mutation" in x:
		# 		return "ea_local_neighbors_second_degree_mutation"
		# 	elif "ea_local_embeddings_mutation" in x:
		# 		return "ea_local_embeddings_mutation"
		# 	elif "ea_local_approx_spread_mutation" in x:
		# 		return "ea_local_approx_spread_mutation"
		# 	return x

		# data2plot["adaptive_local_rate"] = data2plot["adaptive_local_rate"].apply(lambda x:  replace(x))
		# data2plot = data2plot[data2plot["adaptive_local_rate"]==False]
		var2plot = "k"
		# F = "moving_avg_len"
		F = "exploration_weight"
		# F_values = sorted(data2plot[F].unique())
		# F_values = [100]
		F_values = [1.]

		x = sorted(data2plot[var2plot].unique())

		for f_v in F_values:
			df = data2plot[data2plot[F]==f_v]
			mean = df.groupby(var2plot)[y].mean()[x].to_numpy()
			std = df.groupby(var2plot)[y].std()[x].to_numpy()
			# plt.plot(x, mean, label=f_v)
			plt.plot(x, mean, label='mutations_combined')
			plt.fill_between(x, mean - std, mean + std, alpha=0.2)
		plt.title(title)
		plt.ylabel(y)
		plt.xlabel(var2plot)
		plt.legend(loc='best')


out_dir = "../../ea_improvements/local_global_combinations/out/CA-GrQc/local_search_rate/WC"
# out_dir = "../local_global_combinations/out/CA-GrQc/local_search_rate/IC"
# out_dir = "../../ea_improvements/local_global_combinations/out/wiki/local_search_rate/WC"
# out_dir = "../local_global_combinations/out/wiki/local_search_rate/IC"
# out_dir = "../local_global_combinations/out/amazon/local_search_rate/IC"
# out_dir = "../../ea_improvements/local_global_combinations/out/amazon/local_search_rate/WC"
data2plot = collect_results(out_dir, "log")
data2plot = data2plot[data2plot["adaptive_local_rate"] == False]

data2plot = data2plot[data2plot["local_search_rate"] == 0.]
var2plot = "k"

x = sorted(data2plot[var2plot].unique())

df = data2plot
mean = df.groupby(var2plot)[y].mean()[x].to_numpy()
std = df.groupby(var2plot)[y].std()[x].to_numpy()
plt.plot(x, mean, label='global_random')
plt.fill_between(x, mean - std, mean + std, alpha=0.2)
plt.title(title)
plt.ylabel(y)
plt.xlabel(var2plot)
plt.legend(loc='best')

if not os.path.exists(res_dir):
	os.makedirs(res_dir)

plt.savefig(res_dir + "/" + title + "_" + y + ".pdf")

plt.show()
