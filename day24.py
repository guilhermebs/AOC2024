import itertools
import os
import time
import re
import copy

import networkx as nx


def as_decimal(name, values):
    sorted_values = sorted([(n, v) for n, v in values.items() if n[0]==name and n[1].isdigit()])
    return sum(v * 2**i for i, (_, v) in enumerate(sorted_values))


def evaluate_graph(ops, init_values):
    result = copy.deepcopy(init_values)
    G = nx.DiGraph()
    G.add_edges_from((v[1], r) for r, v in ops.items())
    G.add_edges_from((v[2], r) for r, v in ops.items())
    OPERATIONS = {'AND': lambda a, b: a & b, 'OR': lambda a, b: a | b, 'XOR': lambda a,b: a^b}
    for node in nx.topological_sort(G):
        if node not in result:
            op = ops[node]
            result[node] = OPERATIONS[op[0]](result[op[1]], result[op[2]])
    return result


def find_swap(op_name, var1, var2, inverse_ops, swap):
    key = (op_name, *sorted([var1, var2]))
    if key in inverse_ops:
        return inverse_ops[key]
    else:
        for node in inverse_ops.values():
            for new_vars, s1 in (((var1, node), var2), ((var2, node), var1)):
                if res := inverse_ops.get((op_name, *sorted(new_vars))):
                    swap.append((s1, node))
                    return res
    raise ValueError('No suitable substitutes!')


def find_variables(a, b, cin, inverse_ops):
    if cin is None:
        swaps = []
        sum_var = find_swap('XOR', a, b, inverse_ops, swaps)
        carry_var = find_swap('AND', a, b, inverse_ops, swaps)
        return sum_var, carry_var, swaps
    else:
        swaps = []
        xor_ab_var = find_swap('XOR', a, b, inverse_ops, swaps)
        sum_var = find_swap('XOR', xor_ab_var, cin, inverse_ops, swaps)
        and_ab_var = find_swap('AND', a, b, inverse_ops, swaps)
        and_xor_ab_cin_var = find_swap('AND', xor_ab_var, cin, inverse_ops, swaps)
        carry_var = find_swap('OR', and_ab_var, and_xor_ab_cin_var, inverse_ops, swaps)
        return sum_var, carry_var, swaps
        

def solve():
    input_file_contents = open(os.path.join("input", "day24")).read().rstrip()

    init_values = {m.group(1): int(m.group(2)) for m in re.finditer(r"(\w+\d*): (\d)", input_file_contents)}
    ops = {m.group(4): (m.group(2), *sorted([m.group(1), m.group(3)])) for m in re.finditer(r"(\w+\d*) (AND|OR|XOR) (\w+\d*) -> (\w+\d*)", input_file_contents)}
    original_result = evaluate_graph(ops, init_values)


    sol_part1 = as_decimal('z', original_result)
    print("Part 1:", sol_part1)

    inverse_ops = {v: k for k, v in ops.items()}
    bit = 0
    carry = None
    swap = []
    while f'x{bit:02d}' in init_values: 
        _, carry, s = find_variables(f'x{bit:02d}', f'y{bit:02d}', carry, inverse_ops)
        swap.extend(s)
        bit += 1

    sol_part2 = ','.join(sorted(set(itertools.chain(*swap))))
    print("Part 2:", sol_part2)


if __name__ == "__main__":
    start = time.perf_counter_ns()
    solve()
    print(f"Run time: {(time.perf_counter_ns() - start)/1_000}µs")
