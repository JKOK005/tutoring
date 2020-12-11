"""
Metaheuristic approach to TSP using Genetic Algorithm
"""
import copy
import numpy as np
import random

def validateRouteFeasibility(candidate_route: [int], adjacency_mat: np.ndarray) -> bool:
	"""
	Validates of a route is feasible by looking at the adjacency matrix and seeing if there are defined paths for the route
	"""
	for i in range(len(candidate_route) -1):
		from_city 	= candidate_route[i]
		to_city 	= candidate_route[i +1]
		if adjacency_mat[from_city][to_city] == 0:
			return False 
	return True
 
def generateRoutes(num_routes: int, cities: int, start_city: int, end_city: int, adjacency_mat: np.ndarray) -> [[int]]:
	"""
	Generates num_routes Routes beginning with a starting city and ending with an end city

	We will check for the feasibility of a route before we shortlist it as one candidate route
	"""
	candidate_routes = []
	cities_to_permutate = [i for i in range(cities)]
	cities_to_permutate.remove(start_city) if start_city in cities_to_permutate else None
	cities_to_permutate.remove(end_city) if end_city in cities_to_permutate else None

	# Care for edge case where all possible routes is fewer than num_routes
	while(len(candidate_routes) <= num_routes):
		new_candidate = copy.copy(cities_to_permutate)
		random.shuffle(new_candidate)
		new_candidate = [start_city] + new_candidate + [end_city]
		if validateRouteFeasibility(candidate_route = new_candidate, adjacency_mat = adjacency_mat) and new_candidate not in candidate_routes:
			candidate_routes.append(new_candidate)
	return candidate_routes

def evaluateFitness(candidate_route: [int], cost_mat: np.ndarray) -> float:
	"""
	Evaluates the fitness score for a chosen candidate route
	"""
	cum_cost = 0
	for i in range(len(candidate_route) -1):
		from_city 	= candidate_route[i]
		to_city 	= candidate_route[i +1]
		cum_cost += cost_mat[from_city][to_city]
	return 1 / cum_cost

def separateElites(N_elites: int, candidate_routes: [[int]], cost_mat: np.ndarray) -> ([[int]], [[int]]):
	"""
	Separates out N_elites from the rest of the candidates
	"""
	candidate_routes_w_fitness = list(map(lambda each_route: (each_route, evaluateFitness(candidate_route = each_route, cost_mat = cost_mat)), candidate_routes))
	candidate_routes_w_fitness.sort(key = lambda x: x[1])
	candidate_routes_w_fitness = list(map(lambda each_route: each_route[0], candidate_routes_w_fitness))
	return (candidate_routes_w_fitness[-1 * N_elites : ], candidate_routes_w_fitness[ : -1 * N_elites])

def filterByProbability(candidate_routes: [[int]], cost_mat: np.ndarray) -> [[int]]:
	"""
	Generates new candidates into the mating pool via probability selection. 

	Each candidate route is attached a probability of selection proportionate to its fitness value
	"""
	pass

def filterByTournament(candidate_routes: [[int]], N_per_tournament: int, cost_mat: np.ndarray) -> [[int]]:
	"""
	Generates new candidates into the mating pool via probability selection. 

	We select N_per_tournament candidates to challenge each other and the winner will be the one with the highest fitness score	
	"""
	best_candidates 	= []
	candidate_splits 	= np.array_split(candidate_routes, N_per_tournament)
	for each_candidate_split in candidate_splits:
		candidate_routes_w_fitness = list(map(lambda each_route: (each_route, evaluateFitness(candidate_route = each_route, cost_mat = cost_mat)), each_candidate_split))
		candidate_routes_w_fitness.sort(key = lambda x: x[1])
		best_candidates.append(candidate_routes_w_fitness[-1][0])
	return best_candidates

def breed(parent_1: [int], parent_2: [int]) -> [int]:
	"""
	Performs cross over mutation between parents to generate a new candidate route

	Cross over is done at the halfway point
	"""
	halfway_point = len(parent_1) // 2
	
	pass

def breedN(candidate_routes: [[int]], N_iterations: int) -> [[int]]:
	"""
	Performs corss over mutation between parents N_iterations times
	"""
	after_breeding 	 	 = []
	for _ in range(N_iterations):
		[parent_1, parent_2] = random.sample(candidate_routes, 2)
		after_breeding.append(breed(parent_1 = parent_1, parent_2 = parent_2))
	return after_breeding

def mutate(candidate_routes: [[int]], prob_of_mutation: float) -> [int]:
	"""
	Mutates an existing route by swapping randomly selected positions based on a given probability
	"""
	pass

if __name__ == "__main__":
	ITERATIONS 		= 100
	CITIES 			= 100
	SAMPLE_ROUTES 	= 10000
	ELITES 			= 100
	BREEDINGS 		= 9900

	ADJACENCY_MAT 	= np.ones([CITIES, CITIES])
	COST_MAT 		= np.random.randint(low = 0, high = 100, size=(CITIES, CITIES))

	candidate_pool 	= generateRoutes(num_routes = SAMPLE_ROUTES, cities = CITIES, start_city = 0, end_city = 0, adjacency_mat = ADJACENCY_MAT)

	for _ in range(ITERATIONS):
		(elites, others) 		= separateElites(N_elites = ELITES, candidate_routes = candidate_pool, cost_mat = COST_MAT)
		best_routes_selection 	= filterByTournament(candidate_routes = others, N_per_tournament = 10)
		new_breeds 				= breedN(candidate_routes = best_routes_selection, N_iterations = BREEDINGS)

