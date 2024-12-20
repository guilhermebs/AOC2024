import os
import time
import networkx as nx


def count_cheats(cutoff, dist_to_start, dist_to_end, cheat_len):
    result = 0
    for pa, s2a in dist_to_start.items():
        for dx in range(-cheat_len, cheat_len + 1):
            for dy in range(-(cheat_len - abs(dx)), (cheat_len - abs(dx)) + 1):
                a2b = abs(dx) + abs(dy)
                pb = (pa[0] + dx, pa[1] + dy)
                b2e = dist_to_end.get(pb, cutoff + 1)
                result += s2a + a2b + b2e <= cutoff
    return result


def solve():
    input_file_contents = open(os.path.join("input", "day20")).read().rstrip()
    track = input_file_contents.splitlines()
    G = nx.grid_2d_graph(len(track[0]), len(track))
    for y, line in enumerate(track):
        for x, c in enumerate(line):
            if c == "#":
                G.remove_node((x, y))
            elif c == "S":
                start = x, y
            elif c == "E":
                end = x, y

    time_no_cheat = nx.shortest_path_length(G, start, end)
    cutoff = time_no_cheat - 100
    dist_to_start = nx.single_source_shortest_path_length(G, start, cutoff=cutoff)
    dist_to_end = nx.single_source_shortest_path_length(G, end, cutoff=cutoff)
    print("Part 1:", count_cheats(cutoff, dist_to_start, dist_to_end, 2))
    print("Part 1:", count_cheats(cutoff, dist_to_start, dist_to_end, 20))


if __name__ == "__main__":
    start = time.perf_counter_ns()
    solve()
    print(f"Run time: {(time.perf_counter_ns() - start)/1_000}µs")
