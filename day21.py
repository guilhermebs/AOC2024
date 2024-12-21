import heapq
import itertools
import os
import time

import more_itertools

NUMERICAL_KEYPAD = {
    (0, 0): "7",
    (1, 0): "8",
    (2, 0): "9",
    (0, 1): "4",
    (1, 1): "5",
    (2, 1): "6",
    (0, 2): "1",
    (1, 2): "2",
    (2, 2): "3",
    (0, 3): None,
    (1, 3): "0",
    (2, 3): "A",
}

NUMERICAL_START_POS = (2, 3)

DIRECTIONAL_KEYPAD = {
    (0, 0): None,
    (1, 0): "^",
    (2, 0): "A",
    (0, 1): "<",
    (1, 1): "v",
    (2, 1): ">",
}

DIRECTIONAL_START_POS = (2, 0)

KEYPADS = {
    "NUMERICAL": NUMERICAL_KEYPAD,
    "DIRECTIONAL": DIRECTIONAL_KEYPAD,
}

DIR2TUP = {
    '^': (0, -1),
    'v': (0, 1),
    '<': (-1, 0),
    '>': (1, 0),
}


def commands_to_type(to_type, position, keypad):
    commands = ['']
    pos = position
    for c in to_type:
        new_commands = []
        target_pos = [k for k, v in keypad.items() if v == c][0]
        dx, dy = target_pos[0] - pos[0], target_pos[1] - pos[1]
        directions = (
            (">" if dx > 0 else "<") * abs(dx)
            + ("v" if dy > 0 else "^") * abs(dy)
        )
        for permutation in more_itertools.distinct_permutations(directions):
            p = pos
            for cc in permutation:
                d = DIR2TUP[cc]
                p = p[0]+d[0], p[1] + d[1] 
                if keypad[p] is None:
                    break
            else:
                new_commands.extend(c + ''.join(permutation) + 'A' for c in commands)
        commands = new_commands
        pos = target_pos
    return commands


def solve():
    input_file_contents = open(os.path.join("input", "day21")).read().rstrip()
    sequences = input_file_contents.splitlines()
    #sequences = ["029A", "980A", "179A", "456A", "379A"]
    starting_positions = [
        NUMERICAL_START_POS,
        DIRECTIONAL_START_POS,
        DIRECTIONAL_START_POS,
    ]
    keypads = [NUMERICAL_KEYPAD, DIRECTIONAL_KEYPAD, DIRECTIONAL_KEYPAD]
    sol_part1 = 0
    for seq in sequences:
        print(seq)
        candidates = [seq]
        for pos, keypad in zip(starting_positions, keypads):
            #candidates = list(itertools.chain.from_iterable(commands_to_type(s, pos, keypad) for s in candidates))
            candidates = commands_to_type(candidates[0], pos, keypad)
        sol_part1 += min(len(c) for c in candidates) * int(seq[:-1])

    print("Part 1:", sol_part1)

    sol_part2 = None
    print("Part 2:", sol_part2)


if __name__ == "__main__":
    start = time.perf_counter_ns()
    solve()
    print(f"Run time: {(time.perf_counter_ns() - start)/1_000}µs")
