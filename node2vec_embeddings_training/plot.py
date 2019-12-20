from src.plot import plot_dir

plot_dir(out_dir="./out/barabasi_albert",
			 levels_function=["separate_x", "subplot"], csv_prefix="log", sub_Y=["best_mc_spread"],
			 F=("smart_initialization", ["community", "community_degree", "community_degree_spectral", "degree", "none"]),
			 res_dir="./plots/barabasi_albert")

plot_dir(out_dir="./out/amazon",
		 levels_function=["separate_x", "subplot"], csv_prefix="log", sub_Y=["best_mc_spread"],
		 F=("smart_initialization", ["community", "community_degree", "community_degree_spectral", "degree", "none"]),
		 res_dir="./plots/amazon")

plot_dir(out_dir="./out/epinions",
		 levels_function=["separate_x", "subplot"], csv_prefix="log", sub_Y=["best_mc_spread"],
		 F=("smart_initialization", ["community", "community_degree", "community_degree_spectral", "degree", "none"]),
		 res_dir="./plots/epinions")

plot_dir(out_dir="./out/wiki",
		 levels_function=["separate_x", "subplot"], csv_prefix="log", sub_Y=["best_mc_spread"],
		 F=("smart_initialization", ["community", "community_degree", "community_degree_spectral", "degree", "none"]),
		 res_dir="./plots/wiki")
