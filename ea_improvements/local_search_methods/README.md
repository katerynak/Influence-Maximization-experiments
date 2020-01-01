Evolutionary algorithm local mutation methods comparison: 
    - ea_local_neighbors_random_mutation: random gene is selected and mutated with 
    one of its neighbors randomly
    - ea_local_embeddings_mutation: random gene is selected and mutated with one of its most
    similar nodes according to embeddings similarity
    - ea_local_neighbors_second_degree_mutation: random gene is selected and mutated with one if its neighbors;
    the probability to select a neighbor is proportional to its approximated second order degree
    - ea_local_neighbors_second_degree_mutation_emb: random gene is selected and mutated with one if its
    most similar nodes according to embeddings similarity;
    the probability to select a neighbor is proportional to its approximated second order degree 
