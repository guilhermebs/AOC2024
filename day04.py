import os
import time
from collections import Counter

NEXT_LETTER = {"X": "M", "M": "A", "A": "S", "S": None}


def find_xmas_dir(grid, i, j, letter, dir):
    if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]):
        return 0
    if grid[i][j] != letter:
        return 0
    if NEXT_LETTER[letter] is None:
        return 1
    else:
        return find_xmas_dir(grid, i + dir[0], j + dir[1], NEXT_LETTER[letter], dir)


def find_mas(grid, i, j, letter, dir):
    if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]):
        return None
    if grid[i][j] != letter:
        return None
    if NEXT_LETTER[letter] is None:
        return (i - dir[0], j - dir[1])
    else:
        return find_mas(grid, i + dir[0], j + dir[1], NEXT_LETTER[letter], dir)


def solve():
    input_file_contents = open(os.path.join("input", "day04")).read().rstrip()
    grid = [line for line in input_file_contents.splitlines()]

    sol_part1 = sum(
        find_xmas_dir(grid, i, j, "X", dir)
        for dir in [
            (1, 0),
            (-1, 0),
            (0, 1),
            (0, -1),
            (1, 1),
            (-1, 1),
            (1, -1),
            (-1, -1),
        ]
        for i in range(len(grid))
        for j in range(len(grid[0]))
    )
    print("Part 1:", sol_part1)

    a_coords = Counter(
        find_mas(grid, i, j, "M", dir)
        for dir in [(1, 1), (-1, 1), (1, -1), (-1, -1)]
        for i in range(len(grid))
        for j in range(len(grid[0]))
    )
    sol_part2 = sum(v == 2 for v in a_coords.values())
    print("Part 2:", sol_part2)


if __name__ == "__main__":
    start = time.time()
    solve()
    print(f"Run time: {time.time() - start:.3f}s")
