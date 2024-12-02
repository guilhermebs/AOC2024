import os
import time

def is_safe(levels):
    d1 = levels[2] - levels[1]
    for (la, lb) in zip(levels[:-1], levels[1:]):
        abs_diff = abs(lb - la)
        if abs_diff == 0 or abs_diff > 3:
            return False
        if d1 * (lb - la) < 0:
            return False
    return True

def solve():
    input_file_contents = open(os.path.join("input", "day02")).read().rstrip()

    sol_part1 = 0
    for line in input_file_contents.splitlines():
        levels = [int(n) for n in line.split()]
        sol_part1 += is_safe(levels)
    print("Part 1:", sol_part1)

    sol_part2 = 0
    for line in input_file_contents.splitlines():
        levels = [int(n) for n in line.split()]
        sol_part2 += is_safe(levels) or any(is_safe(levels[:i] + levels[i+1:]) for i in range(len(levels)))
    print("Part 2:", sol_part2)


if __name__ == "__main__":
    start = time.time()
    solve()
    print(f"Run time: {time.time() - start:.3f}s")
