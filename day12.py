from collections import deque
import os
import time


def fill(x0, y0, farm):
    plant = farm[x0, y0]
    to_explore = deque([(x0, y0)])
    garden = set([(x0, y0)])
    perimeter = 0
    while len(to_explore):
        x, y = to_explore.pop()
        for xx, yy in ((x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)):
            if (xx, yy) not in garden:
                if (xx, yy) in farm and farm[xx, yy] == plant:
                    to_explore.appendleft((xx, yy))
                    garden.add((xx, yy))
                else:
                    perimeter += 1

    edges = set()
    for x, y in garden:
        for xx, yy in ((x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)):
            if (xx, yy) not in garden:
                if xx == x:
                    edges |= {
                        (x - 0.5, (yy + y) / 2),
                        (x, (yy + y) / 2),
                        (x + 0.5, (yy + y) / 2),
                    }
                elif yy == y:
                    edges |= {
                        ((xx + x) / 2, y - 0.5),
                        ((xx + x) / 2, y),
                        ((xx + x) / 2, y + 0.5),
                    }
    possible_next_dir = {
        (0.5, 0): ((0, 0.5), (0, -0.5)),
        (0, 0.5): ((-0.5, 0), (0.5, 0)),
        (-0.5, 0): ((0, -0.5), (0, 0.5)),
        (0, -0.5): ((0.5, 0), (-0.5, 0)),
    }
    start_pos = min(edges)
    dx, dy = 0.5, 0
    x, y = start_pos[0] + dx, start_pos[1] + dy
    n_sides = 1
    # TODO: take into account internal fences!
    while (x, y) != start_pos:
        xx, yy = x + dx, y + dy
        if (xx, yy) in edges:
            x, y = xx, yy
        else:
            for dxx, dyy in possible_next_dir[dx, dy]:
                xx, yy = x + dxx, y + dyy
                if (xx, yy) in edges:
                    n_sides += 1
                    x, y = xx, yy
                    dx, dy = dxx, dyy
                    break
            else:
                raise Exception()

    return garden, len(garden), perimeter, n_sides


def solve():
    input_file_contents = open(os.path.join("input", "day12_ex2")).read().rstrip()
    farm = {
        (x, y): c
        for y, line in enumerate(input_file_contents.splitlines())
        for x, c in enumerate(line)
    }

    explored = set()
    sol_part1 = 0
    sol_part2 = 0
    for x, y in farm.keys():
        if (x, y) in explored:
            continue
        else:
            garden, area, perimeter, n_sides = fill(x, y, farm)
            sol_part1 += area * perimeter
            sol_part2 += area * n_sides
            explored |= garden

    print("Part 1:", sol_part1)
    print("Part 2:", sol_part2)


if __name__ == "__main__":
    start = time.time()
    solve()
    print(f"Run time: {time.time() - start:.3f}s")
