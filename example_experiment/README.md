Example of experimental structure and execution.

To run the experiment:

``
cd Influence-Maximization;
``

``
python -m src.experiments --exp-dir=./experiments/example_experiment/in
``

The experiments.py script (can be found in src/ folder) accepts in input a directory path 
containing input .json files, where the experimental script, the number of repetitions and 
the list of input parameters should be specified. For each .json file a correspondent directory with 
output files and current source code revision number is created.

