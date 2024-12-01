import os
import time
import numpy as np


def solve():
    input_lists = np.loadtxt(os.path.join("input", "day01"), dtype=int)

    sol_part1 = np.sum(np.abs(np.sort(input_lists[:, 0]) - np.sort(input_lists[:, 1])))
    print("Part 1:", sol_part1)

    sol_part2 = 0
    for n1 in input_lists[:, 0]:
        sol_part2 += n1 * np.sum(input_lists[:, 1] == n1)
    print("Part 2:", sol_part2)


if __name__ == "__main__":
    start = time.time()
    solve()
    print(f"Run time: {time.time() - start:.3f}s")
