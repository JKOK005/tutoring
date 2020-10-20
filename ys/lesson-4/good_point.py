import math

def solve_for_p(g_opt: float, start: float, end: float) -> float:
	x 	= (end - start) / 2
	L1 	= math.sqrt(4**2 + (start + x)**2)
	L2 	= math.sqrt(4**2 + (3 - start - x)**2)
	g 	= L1 - L2

	if abs(g_opt - g) < 1e-9:
		return start + x
	elif g > g_opt:
		return solve_for_p(g_opt = g_opt, start = start, end = start + x)
	else:
		return solve_for_p(g_opt = g_opt, start = start + x, end = end)

if __name__ == "__main__":
	solve_for_p(g_opt = 1, start = 0, end = 0)