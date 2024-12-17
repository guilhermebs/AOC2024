import os
import time


def will_move(pos, dir_, warehouse):
    x, y = pos
    dx, dy = dir_
    if warehouse[y][x] == ".":
        return set()
    elif warehouse[y][x] == "#":
        return {None}
    elif warehouse[y][x] == "[" and dir_ in ((0, 1), (0, -1)):
        return {(x, y), (x+1, y)} | (will_move((x, y + dy), dir_, warehouse) | will_move((x + 1, y + dy), dir_, warehouse))
    elif warehouse[y][x] == "[" and dir_ == (1, 0):
        return {(x, y), (x+1, y)} | will_move((x + 2, y), dir_, warehouse)
    elif warehouse[y][x] == "]" and dir_ in ((0, 1), (0, -1)):
        return {(x, y), (x-1, y)} | (will_move((x, y + dy), dir_, warehouse) | will_move((x - 1, y + dy), dir_, warehouse))
    elif warehouse[y][x] == "]" and dir_ == (-1, 0):
        return {(x, y), (x-1, y)} | will_move((x - 2, y), dir_, warehouse)
    else:
        raise ValueError(warehouse[y][x], dir_)


def solve():
    input_file_contents = open(os.path.join("input", "day15")).read().rstrip()

    warehouse_str, directions_str = input_file_contents.split("\n\n")
    directions_str = "".join(directions_str.splitlines())
    warehouse = [list(line) for line in warehouse_str.splitlines()]
    x, y = [
        (xx, yy)
        for yy, line in enumerate(warehouse)
        for xx, c in enumerate(line)
        if c == "@"
    ][0]
    assert warehouse[y][x] == "@"
    warehouse[y][x] = "."
    start_count = sum(c == "O" for line in warehouse for c in line)

    for m in directions_str:
        if m == ">":
            dx, dy = 1, 0
        elif m == "<":
            dx, dy = -1, 0
        elif m == "v":
            dx, dy = 0, 1
        elif m == "^":
            dx, dy = 0, -1
        else:
            raise ValueError(m)
        xx, yy = x + dx, y + dy
        if warehouse[yy][xx] == "#":
            pass
        elif warehouse[yy][xx] == ".":
            x, y = xx, yy
        elif warehouse[yy][xx] == "O":
            n_move = 1
            while warehouse[y + (n_move + 1) * dy][x + (n_move + 1) * dx] == "O":
                n_move += 1
            if warehouse[y + (n_move + 1) * dy][x + (n_move + 1) * dx] == ".":
                warehouse[yy][xx] = "."
                warehouse[y + (n_move + 1) * dy][x + (n_move + 1) * dx] = "O"
                x, y = xx, yy
        else:
            raise ValueError()

        assert start_count == sum(c == "O" for line in warehouse for c in line)

        # warehouse[y][x] = "@"
        # print("\n".join("".join(line) for line in warehouse))
        # warehouse[y][x] = "."

    sol_part1 = sum(
        x + 100 * y
        for y, line in enumerate(warehouse)
        for x, c in enumerate(line)
        if c == "O"
    )
    print("Part 1:", sol_part1)

    warehouse = [
        list(line)
        for line in warehouse_str.replace(".", "..")
        .replace("#", "##")
        .replace("O", "[]")
        .replace("@", "@.")
        .splitlines()
    ]
    x, y = [
        (xx, yy)
        for yy, line in enumerate(warehouse)
        for xx, c in enumerate(line)
        if c == "@"
    ][0]
    assert warehouse[y][x] == "@"
    warehouse[y][x] = "."

    for m in directions_str:
        if m == ">":
            dx, dy = 1, 0
        elif m == "<":
            dx, dy = -1, 0
        elif m == "v":
            dx, dy = 0, 1
        elif m == "^":
            dx, dy = 0, -1
        else:
            raise ValueError(m)
        xx, yy = x + dx, y + dy
        if warehouse[yy][xx] == "#":
            pass
        elif warehouse[yy][xx] == ".":
            x, y = xx, yy
        elif warehouse[yy][xx] in "[]":
            coords_moving = will_move((xx, yy), (dx, dy), warehouse)
            if None not in coords_moving:
                x, y = xx, yy
                org = {(cx, cy): warehouse[cy][cx] for cx, cy in coords_moving}
                for cx, cy in coords_moving:
                    warehouse[cy+dy][cx+dx] = org[cx, cy]
                    if (cx-dx, cy-dy) not in coords_moving:
                        warehouse[cy][cx] = '.'
        else:
            raise ValueError()

    sol_part2 = sum(
        x + 100 * y
        for y, line in enumerate(warehouse)
        for x, c in enumerate(line)
        if c == "["
    )
    print("Part 2:", sol_part2)


if __name__ == "__main__":
    start = time.time()
    solve()
    print(f"Run time: {time.time() - start:.3f}s")
