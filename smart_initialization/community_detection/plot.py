from src.plot import plot_dir


plot_dir(out_dir="../barabasi_albert",
			 levels_function=["separate_x", "subplot"], csv_prefix="log", sub_Y=["best_mc_spread"],
			 F=("smart_initialization", ["betweenness", "closeness", "degree",
										 "eigenvector", "katz", "none"]),
			 res_dir="./barabasi_albert")
# plot_dir(out_dir="../barabasi_albert",
# 			 levels_function=["separate_x", "subplot"], csv_prefix="log", sub_Y=["best_mc_spread"],
# 			 F=("smart_initialization", ["betweenness", "none"]),
# 			 res_dir="./barabasi_albert")
plot_dir(out_dir="../wiki",
			 levels_function=["separate_x", "subplot"], csv_prefix="log", sub_Y=["best_mc_spread"],
			 F=("smart_initialization", ["betweenness", "closeness", "degree",
										 "eigenvector", "katz", "none"]),
			 res_dir="./wiki")
plot_dir(out_dir="../epinions",
			 levels_function=["separate_x", "subplot"], csv_prefix="log", sub_Y=["best_mc_spread"],
			 F=("smart_initialization", ["betweenness", "closeness", "degree",
										 "eigenvector", "katz", "none"]),
			 res_dir="./epinions")
plot_dir(out_dir="../amazon",
			 levels_function=["separate_x", "subplot"], csv_prefix="log", sub_Y=["best_mc_spread"],
			 F=("smart_initialization", ["betweenness", "closeness", "degree",
										 "eigenvector", "katz", "none"]),
			 res_dir="./amazon")
