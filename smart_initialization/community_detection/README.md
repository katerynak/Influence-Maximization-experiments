Smart initialization of the initial population using smart individuals,
each of them is sampled from different communities, the probability of choosing one 
community upon the others (for each individual) is proportional to its size.

Individuals inside the communities are sampled both with high degree strategy (where
the probabilities to choose the nodes are proportional to their degree) and 
at random.

When sampling nodes for each individual, each node, after being chosen and inserted into 
the individual seed set, is deleted from the graph (with its edges) and community, 
and before sampling the next individual the degrees of all the remaining nodes and 
community sizes are updated, in order to have updated probabilities.

The original graph and communities are reset before the creation of a new individual. 