import os
import time

NEXT_DIR = {
    (0, -1): (1, 0),
    (1, 0): (0, 1),
    (0, 1): (-1, 0),
    (-1, 0): (0, -1),
}


def guard_loops(init_position, init_dir, obstacles, dim_x, dim_y):
    visited = set()
    guard_position = init_position
    guard_dir = init_dir
    len(obstacles)
    while 0 <= guard_position[0] < dim_x and 0 <= guard_position[1] < dim_y:
        if (guard_position, guard_dir) in visited:
            return True
        next_pos = (guard_position[0] + guard_dir[0], guard_position[1] + guard_dir[1])
        if next_pos in obstacles:
            guard_dir = NEXT_DIR[guard_dir]
        else:
            visited.add((guard_position, guard_dir))
            guard_position = next_pos
    return False


def solve():
    input_file_contents = open(os.path.join("input", "day06")).read().rstrip()
    lines = input_file_contents.splitlines()
    init_position = [
        (x, y) for y, line in enumerate(lines) for x, c in enumerate(line) if c == "^"
    ][0]
    obstacles = {
        (x, y) for y, line in enumerate(lines) for x, c in enumerate(line) if c == "#"
    }
    dim_y, dim_x = len(lines), len(lines[0])
    init_dir = (0, -1)
    visited = set()
    guard_position = init_position
    guard_dir = init_dir
    while 0 <= guard_position[0] < dim_x and 0 <= guard_position[1] < dim_y:
        next_pos = (guard_position[0] + guard_dir[0], guard_position[1] + guard_dir[1])
        if next_pos in obstacles:
            guard_dir = NEXT_DIR[guard_dir]
        else:
            visited.add(guard_position)
            guard_position = next_pos

    print("Part 1:", len(visited))

    sol_part2 = 0
    for ox in range(dim_x):
        for oy in range(dim_y):
            if (ox, oy) == init_position or (ox, oy) in obstacles:
                continue
            sol_part2 += guard_loops(
                init_position, init_dir, obstacles | set([(ox, oy)]), dim_x, dim_y
            )
    print("Part 2:", sol_part2)


if __name__ == "__main__":
    start = time.time()
    solve()
    print(f"Run time: {time.time() - start:.3f}s")
