from src.plot import plot_dir

# plot_dir(out_dir="../wiki",
# 			 levels_function=["separate_x", "subplot"],
# 			 csv_prefix="log",
# 			 sub_Y=["exec_time", "best_mc_spread"],
# 		  	 F=("spread_function", ["monte_carlo", "monte_carlo_max_hop", "two_hop"]),
# 			 res_dir="../plots/wiki")

# plot_dir(out_dir="../amazon/population_size",
# 			 levels_function=["subplot"], x2plot="population_size",
# 			 csv_prefix="log",
# 			 sub_Y=["exec_time", "best_mc_spread"],
# 		  	 F=("spread_function", ["monte_carlo", "two_hop"]),
# 			 res_dir="../plots/amazon", name="population_size")

# plot_dir(out_dir="../amazon/p",
# 			 levels_function=["subplot"], x2plot="p",
# 			 csv_prefix="log",
# 			 sub_Y=["exec_time", "best_mc_spread"],
# 		  	 F=("spread_function", ["monte_carlo","monte_carlo_max_hop", "two_hop"]),
# 			 res_dir="../plots/amazon", name="p")

# plot_dir(out_dir="../amazon/k",
# 			 levels_function=["subplot"], x2plot="k",
# 			 csv_prefix="log",
# 			 sub_Y=["exec_time", "best_mc_spread"],
# 		  	 F=("spread_function", ["monte_carlo", "two_hop"]),
# 			 res_dir="../plots/amazon", name="k")

# plot_dir(out_dir="../amazon",
# 			 levels_function=["separate_x", "subplot"],
# 			 csv_prefix="log",
# 			 sub_Y=["exec_time", "best_mc_spread"],
# 		  	 F=("spread_function", ["monte_carlo", "monte_carlo_max_hop", "two_hop"]),
# 			 res_dir="../plots/amazon")

# plot_dir(out_dir="../amazon",
# 			 levels_function=["separate_x", "subplot"],
# 			 csv_prefix="log",
# 			 sub_Y=["exec_time", "diversity"],
# 		  	 F=("spread_function", ["monte_carlo", "monte_carlo_max_hop", "two_hop"]),
# 			 res_dir="../plots/amazon")

# plot_dir(out_dir="../wiki",
# 			 levels_function=["separate_x", "subplot"],
# 			 csv_prefix="log",
# 			 sub_Y=["exec_time", "diversity"],
# 		  	 F=("spread_function", ["monte_carlo", "monte_carlo_max_hop", "two_hop"]),
# 			 res_dir="../plots/wiki")

plot_dir(out_dir="../epinions",
			 levels_function=["separate_x", "subplot"],
			 csv_prefix="log",
			 sub_Y=["exec_time", "best_mc_spread"],
		  	 F=("spread_function", ["monte_carlo", "monte_carlo_max_hop", "two_hop"]),
			 res_dir="../plots/epinions")
