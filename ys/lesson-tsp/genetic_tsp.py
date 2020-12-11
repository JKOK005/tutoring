"""
Metaheuristic approach to TSP using Genetic Algorithm
"""
import numpy as np

def validateRouteFeasibility(candidate_route: [int], adjacency_mat: np.ndarray) -> bool:
	"""
	Validates of a route is feasible by looking at the adjacency matrix and seeing if there are defined paths for the route
	"""
	pass

def generateRoutes(num_routes: int, cities: int, start_city: int, end_city: int, adjacency_mat: np.ndarray) -> [[int]]:
	"""
	Generates num_routes Routes beginning with a starting city and ending with an end city

	We will check for the feasibility of a route before we shortlist it as one candidate route
	"""
	pass

def evaluateFitness(candidate_route: [int], cost: [int]) -> float:
	"""
	Evaluates the fitness score for a chosen candidate route
	"""
	pass

def mate_by_probability(candidate_routes: [[int]]) -> [[int]]:
	"""
	Generates new candidates into the mating pool via probability selection. 

	Each candidate route is attached a probability of selection proportionate to its fitness value
	"""
	pass

def mate_by_tournament(candidate_routes: [[int]], N_per_tournament: int) -> [[int]]:
	"""
	Generates new candidates into the mating pool via probability selection. 

	We select N_per_tournament candidates to challenge each other and the winner will be the one with the highest fitness score	
	"""
	pass

def breed(parent_1: [int], parent_2: [int]) -> [int]:
	"""
	Performs cross over mutation between parents to generate a new candidate route
	"""
	pass

def mutate(candidate_route: [int], prob_of_mutation: float) -> [int]:
	"""
	Mutates an existing route by swapping randomly selected positions based on a given probability
	"""
	pass

if __name__ == "__main__":
	ITERATIONS = 100

	initalize_candidate_routes = generateRoutes(num_routes = 10000, cities = 10, start_city = 1, end_city = 1, adjacency_mat = ???)
