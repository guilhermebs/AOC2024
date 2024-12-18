import os
import time
import networkx as nx


def solve():
    input_file_contents = open(os.path.join("input", "day18")).read().rstrip()
    MAX_DIM = 70
    bytes_to_use = 1024
    byte_positions = [
        tuple(map(int, line.split(","))) for line in input_file_contents.splitlines()
    ]
    G = nx.grid_2d_graph(MAX_DIM + 1, MAX_DIM + 1)

    G.remove_nodes_from(byte_positions[:bytes_to_use])

    sol_part1 = nx.shortest_path_length(G, (0, 0), (MAX_DIM, MAX_DIM))
    print("Part 1:", sol_part1)

    i = bytes_to_use
    while nx.has_path(G, (0, 0), (MAX_DIM, MAX_DIM)):
        i += 1
        if byte_positions[i] in G:
            G.remove_node(byte_positions[i])

    sol_part2 = byte_positions[i]
    print("Part 2:", ",".join(map(str, sol_part2)))


if __name__ == "__main__":
    start = time.perf_counter_ns()
    solve()
    print(f"Run time: {(time.perf_counter_ns() - start)/1_000}µs")
