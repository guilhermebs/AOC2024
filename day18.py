import os
import time
import networkx as nx


def solve():
    input_file_contents = open(os.path.join("input", "day18")).read().rstrip()
    SIZE = 71
    bytes_to_use = 1024
    byte_positions = [
        tuple(int(p) for p in line.split(","))
        for line in input_file_contents.splitlines()
    ]
    G = nx.Graph()
    G.add_edges_from(
        ((x, y), (xx, yy))
        for x in range(SIZE)
        for y in range(SIZE)
        for (xx, yy) in ((x + 1, y), (x, y + 1), (x - 1, y), (x, y - 1))
        if 0 <= xx < SIZE
        and 0 <= yy < SIZE
    )

    G.remove_nodes_from(byte_positions[:bytes_to_use])

    sol_part1 = nx.shortest_path_length(G, (0, 0), (SIZE - 1, SIZE - 1))
    print("Part 1:", sol_part1)

    i = bytes_to_use
    while nx.has_path(G, (0, 0), (SIZE - 1, SIZE - 1)):
        i += 1
        if byte_positions[i] in G:
            G.remove_node(byte_positions[i])

    sol_part2 = byte_positions[i]
    print("Part 2:", sol_part2)


if __name__ == "__main__":
    start = time.perf_counter_ns()
    solve()
    print(f"Run time: {(time.perf_counter_ns() - start)/1_000}µs")
