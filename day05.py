from collections import defaultdict
import os
import time


def is_sorted(update, page_order_rules):
    for i, v in enumerate(update):
        if intersect := page_order_rules[v].intersection(update[:i]):
            return False, [(i, j) for j, vv in enumerate(update[:i]) if vv in intersect]
    return True, None


def solve():
    input_file_contents = open(os.path.join("input", "day05")).read().rstrip()

    page_order_rules_str, updates_str = input_file_contents.split("\n\n")
    page_order_rules = defaultdict(lambda: set())
    for rule_str in page_order_rules_str.splitlines():
        pages = [int(n) for n in rule_str.split("|")]
        page_order_rules[pages[0]].add(pages[1])

    sol_part1 = 0
    sol_part2 = 0
    for line in updates_str.splitlines():
        update = [int(n) for n in line.split(",")]
        is_ordered, out_of_order = is_sorted(update, page_order_rules)
        if is_ordered:
            sol_part1 += update[len(update) // 2]
        else:
            while not is_ordered:
                switch = out_of_order[0]
                update[switch[0]], update[switch[1]] = (
                    update[switch[1]],
                    update[switch[0]],
                )
                is_ordered, out_of_order = is_sorted(update, page_order_rules)
            sol_part2 += update[len(update) // 2]

    print("Part 1:", sol_part1)
    print("Part 2:", sol_part2)


if __name__ == "__main__":
    start = time.time()
    solve()
    print(f"Run time: {time.time() - start:.3f}s")
