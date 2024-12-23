import os
import time

import networkx as nx


def solve():
    input_file_contents = open(os.path.join("input", "day23")).read().rstrip()

    G = nx.Graph()
    G.add_edges_from(line.split("-") for line in input_file_contents.splitlines())
    
    sol_part1 = 0
    for clique in nx.enumerate_all_cliques(G):
        if len(clique) == 3 and any(n[0] == 't' for n in clique):
            sol_part1 += 1

    print("Part 1:", sol_part1)

    sol_part2 = ",".join(sorted(clique))
    print("Part 2:", sol_part2)


if __name__ == "__main__":
    start = time.perf_counter_ns()
    solve()
    print(f"Run time: {(time.perf_counter_ns() - start)/1_000}µs")
