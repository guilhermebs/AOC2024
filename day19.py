import os
import time
import functools


@functools.cache
def is_design_possible(design, patterns):
    if len(design) == 0:
        return True
    return any(
        is_design_possible(design[len(p) :], patterns)
        for p in patterns
        if design.startswith(p)
    )


@functools.cache
def n_designs_possible(design, patterns):
    if len(design) == 0:
        return 1
    return sum(
        n_designs_possible(design[len(p) :], patterns)
        for p in patterns
        if design.startswith(p)
    )


def solve():
    input_file_contents = open(os.path.join("input", "day19")).read().rstrip()
    patterns_str, designs_str = input_file_contents.split("\n\n")
    patterns = tuple(patterns_str.split(", "))
    sol_part1 = 0
    sol_part2 = 0
    for design in designs_str.splitlines():
        sol_part1 += is_design_possible(design, patterns)
        sol_part2 += n_designs_possible(design, patterns)

    print("Part 1:", sol_part1)
    print("Part 2:", sol_part2)


if __name__ == "__main__":
    start = time.perf_counter_ns()
    solve()
    print(f"Run time: {(time.perf_counter_ns() - start)/1_000}µs")
