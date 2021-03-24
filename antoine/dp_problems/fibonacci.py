def fibonnaci_w_recur(N):
	if N <= 1:
		return N
	else:
		return fibonnaci_w_recur(N -1) + fibonnaci_w_recur(N -2)

def fibonnaci_w_dp(N):
	def inner(N, stored_cache):
		if N <= 1:
			return N
		elif N in stored_cache:
			return stored_cache[N]
		else:
			stored_cache[N] = inner(N -1, stored_cache) + inner(N -2, stored_cache)
			return stored_cache[N]
	return inner(N = N, stored_cache = {0: 0, 1: 1})

if __name__ == "__main__":
	import cProfile
	import sys
	sys.setrecursionlimit(15000)

	FIBONNACI_N = 20
	cProfile.runctx("fibonnaci_w_dp({0})".format(FIBONNACI_N), globals = globals(), locals = locals())
	cProfile.runctx("fibonnaci_w_recur({0})".format(FIBONNACI_N), globals = globals(), locals = locals())