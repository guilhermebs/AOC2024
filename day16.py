import os
import time
import heapq

import networkx as nx

def solve():
    input_file_contents = open(os.path.join("input", "day16")).read().rstrip()

    free_tiles = set()
    for y, line in enumerate(input_file_contents.splitlines()):
        for x, c in enumerate(line):
            if c == '#':
                continue
            free_tiles.add((x, y))
            if c == 'S':
                start = (x, y)
            elif c == 'E':
                end = (x, y)
    
    priority_queue = [(0, start, (1, 0))]
    paths = {(start, (1, 0)): [0, set([start])]}
    turns = {
        (1, 0): ((0, -1), (0, 1)),
        (0, 1): ((1, 0), (-1, 0)),
        (-1, 0): ((0, -1), (0, 1)),
        (0, -1): ((1, 0), (-1, 0)),
    }
    best_score = None
    best_paths = set()
    while len(priority_queue):
        score, (x, y), (dx, dy) = heapq.heappop(priority_queue)
        _, path = paths[(x,y), (dx, dy)]
        if (x, y) == end:
            best_score = score
            best_paths = path
            break
        for ddx, ddy in turns[dx,dy]:
            if (x+ddx, y+ddy) in free_tiles:
                if ((x, y), (ddx, ddy)) not in paths:
                    heapq.heappush(priority_queue, (score+1000, (x, y), (ddx, ddy)))
                    paths[(x, y), (ddx, ddy)] = [score + 1000, path]
                elif score+1000 == paths[(x, y), (ddx, ddy)][0]:
                    paths[(x, y), (ddx, ddy)][1] |= path
        xx, yy = x+dx, y+dy
        if (xx, yy) in free_tiles:
            if ((xx, yy), (dx, dy)) not in paths:
                heapq.heappush(priority_queue, (score+1, (xx, yy), (dx, dy)))
                paths[(xx, yy), (dx, dy)] = [score + 1, path | set([(xx, yy)])]
            elif score+1 == paths[(xx, yy), (dx, dy)][0]:
                paths[(xx, yy), (dx, dy)][1] |= path

    sol_part1 = best_score
    print("Part 1:", sol_part1)

    sol_part2 = len(best_paths)
    print("Part 2:", sol_part2)


if __name__ == "__main__":
    start = time.time()
    solve()
    print(f"Run time: {time.time() - start:.3f}s")
