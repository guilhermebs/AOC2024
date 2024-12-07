import os
import math
import time


def concat(a, b):
    return a * 10 ** (int(math.log10(b)) + 1) + b


def find_operation(v, remaining, lhs, pt2=False):
    if v > lhs:
        return False
    if len(remaining) == 0:
        return v == lhs
    return (
        find_operation(v + remaining[0], remaining[1:], lhs, pt2=pt2)
        or find_operation(v * remaining[0], remaining[1:], lhs, pt2=pt2)
        or (
            pt2 and find_operation(concat(v, remaining[0]), remaining[1:], lhs, pt2=pt2)
        )
    )


def solve():
    input_file_contents = open(os.path.join("input", "day07")).read().rstrip()

    sol_part1 = 0
    sol_part2 = 0
    for line in input_file_contents.splitlines():
        lhs, vals = line.split(":")
        lhs = int(lhs)
        vals = [int(v) for v in vals.split()]
        sol_part1 += lhs * find_operation(vals[0], vals[1:], lhs, pt2=False)
        sol_part2 += lhs * find_operation(vals[0], vals[1:], lhs, pt2=True)

    print("Part 1:", sol_part1)
    print("Part 2:", sol_part2)


if __name__ == "__main__":
    start = time.time()
    solve()
    print(f"Run time: {time.time() - start:.3f}s")
