import os
import time
import re


def solve():
    input_file_contents = open(os.path.join("input", "day03")).read().rstrip()
    expression = r"mul\((\d{1,3}),(\d{1,3})\)"
    sol_part1 = 0
    for line in input_file_contents.splitlines():
        for m in re.finditer(expression, line):
            sol_part1 += int(m[1]) * int(m[2])

    print("Part 1:", sol_part1)

    expression = r"(mul\((\d{1,3}),(\d{1,3})\)|do\(\)|don't\(\))"
    sol_part2 = 0
    active = True
    for line in input_file_contents.splitlines():
        for m in re.finditer(expression, line):
            if m[0] == "do()":
                active = True
            elif m[0] == "don't()":
                active = False
            elif active:
                sol_part2 += int(m[2]) * int(m[3])

    print("Part 2:", sol_part2)



if __name__ == "__main__":
    start = time.time()
    solve()
    print(f"Run time: {time.time() - start:.3f}s")
