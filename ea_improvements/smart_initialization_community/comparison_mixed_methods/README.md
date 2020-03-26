Comparison of mixed smart initialization techniques: 
    - degree: insertion of the individual composed of nodes with the highest degrees
    - degree_random: the probability of each node to be inserted in an individual is proportional to its degree
    - community_degree: each node of an individual is chosen probabilistically from one of the detected communities,
    the probability to choose one community is proportional to its size; once the community is chosen, the probability 
    to select a node from the community is proportional to its degree
    - none: random population initialization
    