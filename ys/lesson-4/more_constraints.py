import numpy as np

def permutations_w_recursion_only(n: int, m: int, prev: int) -> int:
	if m == 1:
		if prev is not n:
			return 1
		else:
			return 0

	count = 0
	for i in range(1, n +1):
		if i is not prev:
			count += permutations(n, m -1, i)
	return count

def permutations_w_dp(n: int, m: int, prev: int, cache: np.ndarray) -> int:
	if m == 1:
		if prev is not n:
			return 1
		else:
			return 0

	if cache[prev -1][m -1] >= 0:
		return cache[prev -1][m -1]
	else:
		count = 0
		for i in range(1, n +1):
			if i is not prev:
				count += permutations_w_dp(n, m -1, i, cache)
		
		cache[prev -1][m -1] = count
		return count

def permutations_2(n: int, m: int, prev: int):
	cache = np.ones((n, m)) * -1
	return permutations_w_dp(n, m, 1, cache)

if __name__ == "__main__":
	permutations_2(33, 26, 1)
	