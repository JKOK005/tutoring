import os

def build_graph(file: str):
	road_networks = {}

	with open(file) as f:
		lines = f.readlines()
		lines = list(map(lambda x: x.replace("\n", ""), lines))
		[N, K] = lines[0].split(" ")
		
		for each_line in lines[1:]:
			[start, end, cost] = each_line.split(" ")
			[start, end, cost] = [int(start), int(end), int(cost)]
			if start in road_networks:
				road_networks[start][end] = cost
			else:
				road_networks[start] = {end : cost}
		return(road_networks, int(N), int(K))

def solve(road, starting_city, visited) -> int:
	if starting_city not in road:
		return 0
	else:
		travelled_dist = [0]
		for each_city in road[starting_city].keys():
			if not visited[starting_city -1][each_city -1]:
				cost = road[starting_city][each_city]
				visited[starting_city -1][each_city -1] = True
				travelled_dist.append(cost + solve(road, each_city, visited))
				visited[starting_city -1][each_city -1] = False
		return max(travelled_dist)

if __name__ == "__main__":
	graph_file = os.path.join(os.getcwd(), "resources/test_1.txt")
	(road_networks, N, K) = build_graph(file = graph_file)
	visited = [[False for _ in range(N)] for _ in range(N)]
	max_dist = solve(road = road_networks, starting_city = K, visited = visited)
	print(max_dist)