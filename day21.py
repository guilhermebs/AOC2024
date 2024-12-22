import functools
import os
import time

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
def type_single_command(c, prev_c, keypad, depth=0):
    commands = []
    target_pos = INVERSE_KEYPADS[keypad][c]
    pos = INVERSE_KEYPADS[keypad][prev_c]
    dx, dy = target_pos[0] - pos[0], target_pos[1] - pos[1]
    hmoves = (">" if dx > 0 else "<") * abs(dx)
    vmoves = ("v" if dy > 0 else "^") * abs(dy)
    for permutation in [hmoves + vmoves, vmoves + hmoves]:
        p = pos
        for cc in permutation:
            d = DIR2TUP[cc]
            p = p[0] + d[0], p[1] + d[1]
            if p not in KEYPADS[keypad]:
                break
        else:
            commands.append("".join(permutation) + "A")

    return min(commands, key=lambda c: n_commands_to_type(c, depth))


@functools.cache
def n_commands_to_type(to_type, depth):
    assert to_type.endswith("A")
    if depth == 0:
        return len(to_type)
    prev = "A"
    result = 0
    for char in to_type:
        result += n_commands_to_type(
            type_single_command(char, prev, "DIRECTIONAL", depth=depth-1), depth - 1
        )
        prev = char
    return result


def solve():
    input_file_contents = open(os.path.join("input", "day21")).read().rstrip()
    codes = input_file_contents.splitlines()

    sol_part1 = 0
    sol_part2 = 0
    for code in codes:
        depth2 = 0
        depth25 = 0
        for char, prev_char in zip(code, "A" + code):
            cmd = type_single_command(char, prev_char, "NUMERICAL", 25)
            depth2 += n_commands_to_type(cmd, 2)
            depth25 += n_commands_to_type(cmd, 25)
        sol_part1 += depth2 * int(code[:-1])
        sol_part2 += depth25 * int(code[:-1])
    print("Part 1:", sol_part1)
    print("Part 2:", sol_part2)


if __name__ == "__main__":
    start = time.perf_counter_ns()
    solve()
    print(f"Run time: {(time.perf_counter_ns() - start)/1_000}µs")
