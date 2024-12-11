from functools import cache
import math
import os
import time

@cache
def n_descendents(s, depth):
    if depth == 0:
        return 1
    if s == 0:
        return n_descendents(1, depth - 1)
    ndigits = int(math.log10(s)) + 1
    if ndigits % 2 == 0:
        decimal_split = 10 ** (ndigits // 2)
        left = s//decimal_split
        right = s - left * decimal_split
        return n_descendents(left, depth-1) + n_descendents(right, depth-1)
    else:
        return n_descendents(s * 2024, depth-1)   


def solve():
    input_file_contents = open(os.path.join("input", "day11")).read().rstrip()
    stones = [int(s) for s in input_file_contents.split()]
    sol_part1 = 0
    for s in stones:
        sol_part1 += n_descendents(s, 25)

    print("Part 1:", sol_part1)

    sol_part2 = 0
    for s in stones:
        sol_part2 += n_descendents(s, 75)
    print("Part 2:", sol_part2)


if __name__ == "__main__":
    start = time.time()
    solve()
    print(f"Run time: {time.time() - start:.3f}s")
