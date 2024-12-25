import itertools
import os
import time

def read_key_or_lock(block):
    is_lock =  block.startswith("#####")
    if is_lock:
        return tuple(block[c::6].find('.') - 1 for c in range(5)), is_lock
    else:
        return tuple(7 - block[c::6].find('#') - 1 for c in range(5)), is_lock


def solve():
    input_file_contents = open(os.path.join("input", "day25")).read().rstrip()

    locks = []
    keys = []
    for block in input_file_contents.split("\n\n"):
        combination, is_lock = read_key_or_lock(block)
        if is_lock:
            locks.append(combination)
        else:
            keys.append(combination)
    
    sol_part1 = 0
    for key, lock in itertools.product(locks, keys):
        sol_part1 += all(hk + hl <= 5 for hk, hl in zip(key, lock))
    print("Part 1:", sol_part1)


if __name__ == "__main__":
    start = time.perf_counter_ns()
    solve()
    print(f"Run time: {(time.perf_counter_ns() - start)/1_000}µs")
