from src.plot import plot_dir


plot_dir(out_dir="./out/amazon",
		 levels_function=["separate_x", "subplot"], csv_prefix="log", sub_Y=["best_mc_spread"],
		 F=("smart_initialization", ["community_degree", "degree_random", "degree", "none"]),
		 res_dir="./plots/amazon")

# plot_dir(out_dir="./out/CA-GrQc",
# 		 levels_function=["separate_x", "subplot"], csv_prefix="log", sub_Y=["best_mc_spread"],
# 		 F=("smart_initialization", ["community_degree", "degree_random", "degree", "none"]),
# 		 res_dir="./plots/CA-GrQc")
#
# plot_dir(out_dir="./out/wiki",
# 		 levels_function=["separate_x", "subplot"], csv_prefix="log", sub_Y=["best_mc_spread"],
# 		 F=("smart_initialization", ["community_degree", "degree_random", "degree", "none"]),
# 		 res_dir="./plots/wiki")


