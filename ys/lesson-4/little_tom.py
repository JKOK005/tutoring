def navigate(start: int, map_to, visited: [int]) -> int:
	if visited[start] is True:
		return -1

	if start in map_to:
		next_loc = map_to[start]
		visited[start] = True
		return navigate(start = next_loc, map_to = map_to, visited = visited)
	else:
		return start

if __name__ == "__main__":
	N = 5
	map_to = {1:3, 3:4, 4:5, 5:3}

	for each_n in range(1, N+1):
		final_dest = navigate(start = each_n, map_to = map_to, visited = [False] * (N +1))
		
		if final_dest < 0:
			print("Never Stop")
		else:
			print(final_dest)