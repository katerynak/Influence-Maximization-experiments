from src.plot import plot_dir

# plot_dir(out_dir="../wiki",
# 			 levels_function=["separate_x", "separate"],
# 			 csv_prefix="log",
# 		 	 name="wiki",
# 			 sub_Y=[{"correlation": ["mc_th_corr", "mc_mcmh_corr"]},
# 					{"exec_time": ["exec_time_th_mean", "exec_time_mh_mean", "exec_time_mc_mean"]}, "mc_std"],
# 			 res_dir="../plots")
#
# plot_dir(out_dir="../amazon",
# 			 levels_function=["separate_x", "separate"],
# 			 csv_prefix="log",
# 		 	 name="amazon",
# 			 sub_Y=[{"correlation": ["mc_th_corr", "mc_mcmh_corr"]},
# 					{"exec_time": ["exec_time_th_mean", "exec_time_mh_mean", "exec_time_mc_mean"]}, "mc_std"],
# 			 res_dir="../plots/amazon")
#
# plot_dir(out_dir="../epinions",
# 			 levels_function=["separate_x", "separate"],
# 			 csv_prefix="log",
# 		 	 name="epinions",
# 			 sub_Y=[{"correlation": ["mc_th_corr", "mc_mcmh_corr"]},
# 					{"exec_time": ["exec_time_th_mean", "exec_time_mh_mean", "exec_time_mc_mean"]}, "mc_std"],
# 			 res_dir="../plots/epinions")
#
#
# pref_dir = "barabasi_albert_nodes_10000_n_edges_"
# for i in range(1, 12, 2):
# 	plot_dir(out_dir="../" + pref_dir + "{}".format(i),
# 			 levels_function=["separate_x", "separate"],
# 			 csv_prefix="log",
# 			 name=pref_dir + "{}".format(i),
# 			 sub_Y=[{"correlation": ["mc_th_corr", "mc_mcmh_corr"]},
# 					{"exec_time": ["exec_time_th_mean", "exec_time_mh_mean", "exec_time_mc_mean"]}, "mc_std"],
# 			 res_dir="../plots/" + pref_dir + "{}".format(i))

pref_dir = "barabasi_albert_nodes_1000_n_edges_"
for i in range(1, 12, 2):
	plot_dir(out_dir="../" + pref_dir + "{}".format(i),
			 levels_function=["separate_x", "separate"],
			 csv_prefix="log",
			 name=pref_dir + "{}".format(i),
			 sub_Y=[{"correlation": ["mc_th_corr", "mc_mcmh_corr"]},
					{"exec_time": ["exec_time_th_mean", "exec_time_mh_mean", "exec_time_mc_mean"]}, "mc_std"],
			 res_dir="../plots/" + pref_dir + "{}".format(i))

# plot_dir(out_dir="../barabasi_albert",
# 			 levels_function=["separate_x", "separate"],
# 			 csv_prefix="log",
# 			 sub_Y=[{"correlation": ["mc_th_corr", "mc_mcmh_corr"]},
# 					{"exec_time": ["exec_time_th_mean", "exec_time_mh_mean", "exec_time_mc_mean"]}, "mc_std"],
# 			 res_dir="../plots/barabasi_albert_")
