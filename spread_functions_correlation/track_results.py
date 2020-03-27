from src.plot import plot_dir, collect_results, plt_subplot
import matplotlib.pyplot as plt
import os
from itertools import product
import numpy as np
import pandas as pd

out_file = "summary_table_IC.csv"
df = pd.DataFrame(columns=["dataset", "mc_mcmh_corr", "mc_th_corr", "mc_exec", "mcmh_exec",
						   "th_exec", "mc_std"])


out_dirs = ["./out/barabasi_albert_nodes_1000_n_edges_1",
			"./out/barabasi_albert_nodes_1000_n_edges_3",
			"./out/barabasi_albert_nodes_1000_n_edges_5",
			"./out/barabasi_albert_nodes_1000_n_edges_7",
			"./out/barabasi_albert_nodes_1000_n_edges_9",
			"./out/barabasi_albert_nodes_1000_n_edges_11",
			"./out/barabasi_albert_nodes_10000_n_edges_1",
			"./out/barabasi_albert_nodes_10000_n_edges_3",
			"./out/barabasi_albert_nodes_10000_n_edges_5",
			"./out/barabasi_albert_nodes_10000_n_edges_7",
			"./out/barabasi_albert_nodes_10000_n_edges_9",
			"./out/barabasi_albert_nodes_10000_n_edges_11",
			"./out/amazon",
			"./out/wiki",
			# "./out/epinions",
			]

vars = {"model": "IC", "k": 5, "no_simulations": 100, "p": 0.1}
for out_dir in out_dirs:

	data2plot = collect_results(out_dir, "log", delimiter=",")

	for var in vars:
		data2plot = data2plot[data2plot[var] == vars[var]]
	print(data2plot)
	df = df.append(pd.Series([out_dir.replace("./out/", ""),
							  data2plot["mc_mcmh_corr"].mean(),
							  data2plot["mc_th_corr"].mean(),
							  data2plot["exec_time_mc_mean"].mean(),
							  data2plot["exec_time_mh_mean"].mean(),
							  data2plot["exec_time_th_mean"].mean(),
							  data2plot["mc_std"].mean()
							  ], index=df.columns), ignore_index=True)


print(df)
df = df.round(3)
df.to_csv(out_file)
