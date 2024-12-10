import os
from itertools import chain
import time


def find_end_of_trail(trail, prev, pos):
    if pos not in trail:
        return []
    cur_elevation = trail[pos]
    if cur_elevation != prev + 1:
        return []
    if cur_elevation == 9:
        return [pos]
    i, j = pos
    return list(
        chain.from_iterable(
            find_end_of_trail(trail, cur_elevation, next_pos)
            for next_pos in ((i - 1, j), (i, j - 1), (i + 1, j), (i, j + 1))
        )
    )


def solve():
    input_file_contents = open(os.path.join("input", "day10")).read().rstrip()

    trail = {
        (i, j): int(v)
        for j, line in enumerate(input_file_contents.splitlines())
        for i, v in enumerate(line)
    }
    elevation_0 = [pos for pos, v in trail.items() if v == 0]
    sol_part1 = 0
    sol_part2 = 0
    for init_pos in elevation_0:
        ends = find_end_of_trail(trail, -1, init_pos)
        sol_part1 += len(set(ends))
        sol_part2 += len(ends)

    print("Part 1:", sol_part1)
    print("Part 2:", sol_part2)


if __name__ == "__main__":
    start = time.time()
    solve()
    print(f"Run time: {time.time() - start:.3f}s")
