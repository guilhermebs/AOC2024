import functools
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
    (1, 3): "0",
    (2, 3): "A",
}

DIRECTIONAL_KEYPAD = {
    (1, 0): "^",
    (2, 0): "A",
    (0, 1): "<",
    (1, 1): "v",
    (2, 1): ">",
}

KEYPADS = {
    "NUMERICAL": NUMERICAL_KEYPAD,
    "DIRECTIONAL": DIRECTIONAL_KEYPAD,
}

INVERSE_KEYPADS = {
    "NUMERICAL": {v: k for k, v in NUMERICAL_KEYPAD.items()},
    "DIRECTIONAL": {v: k for k, v in DIRECTIONAL_KEYPAD.items()},
}

DIR2TUP = {
    "^": (0, -1),
    "v": (0, 1),
    "<": (-1, 0),
    ">": (1, 0),
}


@functools.cache
def type_single_command(c, prev_c, keypad):
    commands = []
    target_pos = INVERSE_KEYPADS[keypad][c]
    pos = INVERSE_KEYPADS[keypad][prev_c]
    dx, dy = target_pos[0] - pos[0], target_pos[1] - pos[1]
    directions = (">" if dx > 0 else "<") * abs(dx) + ("v" if dy > 0 else "^") * abs(dy)
    for permutation in more_itertools.distinct_permutations(directions):
        p = pos
        for cc in permutation:
            d = DIR2TUP[cc]
            p = p[0] + d[0], p[1] + d[1]
            if p not in KEYPADS[keypad]:
                break
        else:
            commands.append("".join(permutation) + "A")
    return max(
        commands,
        key=lambda cmd: sum(cprev == cnext for cprev, cnext in zip(cmd, cmd[1:])),
    )


@functools.cache
def commands_to_type(to_type):
    assert to_type.endswith("A")
    prev = "A"
    commands = ""
    for char in to_type:
        commands += type_single_command(char, prev, "DIRECTIONAL")
        prev = char
    return commands


def solve():
    input_file_contents = open(os.path.join("input", "day21")).read().rstrip()
    codes = input_file_contents.splitlines()
    # codes = ["029A", "980A", "179A", "456A", "379A"]

    sol_part1 = 0
    depth = 2
    for code in codes:
        print(code)
        command = ""
        lengths = {i: 0 for i in range(depth + 1)}
        commands = {i: "" for i in range(depth + 1)}
        for char, prev_char in zip(code, "A" + code):
            # print(char, prev_char)
            cmd = type_single_command(char, prev_char, "NUMERICAL")
            lengths[0] += len(cmd)
            commands[0] += cmd
            for d in range(depth):
                cmd = "".join(commands_to_type(c + "A") for c in cmd.split("A")[:-1])
                lengths[d + 1] += len(cmd)
                commands[d + 1] += cmd
            command += cmd
        sol_part1 += lengths[2] * int(code[:-1])
        print(len(command))
    print("Part 1:", sol_part1)

    sol_part2 = None
    print("Part 2:", sol_part2)


if __name__ == "__main__":
    start = time.perf_counter_ns()
    solve()
    print(f"Run time: {(time.perf_counter_ns() - start)/1_000}µs")
