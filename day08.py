import os
import time
from collections import defaultdict
from itertools import permutations


def solve():
    input_file_contents = open(os.path.join("input", "day08")).read().rstrip()
    radars = defaultdict(lambda: set())
    for y, line in enumerate(input_file_contents.splitlines()):
        for x, v in enumerate(line):
            if v != ".":
                radars[v].add((x, y))
    dims = x, y
    antinodes = set()
    for positions in radars.values():
        for p1, p2 in permutations(positions, 2):
            ap = p1[0] + (p1[0] - p2[0]), p1[1] + (p1[1] - p2[1])
            if all(0 <= p <= d for p, d in zip(ap, dims)):
                antinodes.add(ap)
    sol_part1 = len(antinodes)
    print("Part 1:", sol_part1)

    antinodes_pt2 = set()
    for positions in radars.values():
        for p1, p2 in permutations(positions, 2):
            sx, sy = p1[0] - p2[0], p1[1] - p2[1]
            ap = p1
            while all(0 <= p <= d for p, d in zip(ap, dims)):
                antinodes_pt2.add(ap)
                ap = ap[0] + sx, ap[1] + sy
    sol_part2 = len(antinodes_pt2)
    print("Part 2:", sol_part2)


if __name__ == "__main__":
    start = time.time()
    solve()
    print(f"Run time: {time.time() - start:.3f}s")
