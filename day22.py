from collections import defaultdict
import os
import time


def mix_and_prune(a, b):
    return (a ^ b) % 16777216


def solve():
    input_file_contents = open(os.path.join("input", "day22")).read().rstrip()
    secret_numbers = list(map(int, input_file_contents.splitlines()))
    prices = [[int(str(n)[-1])] for n in secret_numbers]
    price_diff = [[] for _ in secret_numbers]
    seq_to_price = [{} for _ in secret_numbers]

    sol_part1 = 0
    for n, p, dp, s2p in zip(secret_numbers, prices, price_diff, seq_to_price):
        for i in range(2000):
            n = mix_and_prune(n * 64, n)
            n = mix_and_prune(n // 32, n)
            n = mix_and_prune(n * 2048, n)
            p.append(int(str(n)[-1]))
            dp.append(p[-1] - p[-2])
            if i > 3:
                prev4 = tuple(dp[-4:])
                if prev4 not in s2p:
                    s2p[prev4] = p[-1]
        sol_part1 += n

    print("Part 1:", sol_part1)

    all_seqs_totals = defaultdict(lambda: 0)
    for s2p in seq_to_price:
        for seq, price in s2p.items():
            all_seqs_totals[seq] += price

    sol_part2 = max(all_seqs_totals.values())
    print("Part 2:", sol_part2)


if __name__ == "__main__":
    start = time.perf_counter_ns()
    solve()
    print(f"Run time: {(time.perf_counter_ns() - start)/1_000}µs")
