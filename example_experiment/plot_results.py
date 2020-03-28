# example of how the results can be gathered to plot them
from src.additional_experimental_scripts.plot_utils import collect_results

out_dir = "./out"

# collect results of all log files in a unified table
all_results = collect_results(out_dir, csv_prefix="log", delimiter=";")
print(all_results)

# if needed, collect results of a particular directory
nested_dir1_results = collect_results("./out/nested_dir1", csv_prefix="log", delimiter=";")
print(nested_dir1_results)