import os
import time
import re

import numpy as np

np.set_printoptions(precision=20)
def solve():
    input_file_contents = open(os.path.join("input", "day13")).read().rstrip()
    machine_matrices = []
    machine_prizes = []
    moves = []
    for m in re.finditer(r"Button A: X\+(\d+), Y\+(\d+)\nButton B: X\+(\d+), Y\+(\d+)\nPrize: X=(\d+), Y=(\d+)", input_file_contents):
        values = [int(m.group(i)) for i in range(1, 7)]
        machine_matrices.append(np.array(values[:4], dtype=np.float64).reshape(2, 2).T)
        machine_prizes.append(np.array(values[4:], dtype=np.float64))
    
    sol_part1 = 0
    for mat, p in zip(machine_matrices, machine_prizes):
        moves = np.linalg.solve(mat, p)
        if np.all(moves >= 0) and np.allclose(moves, moves.round()):
            sol_part1 += moves.dot([3, 1])
    
    print("Part 1:", round(sol_part1))


    sol_part2 = 0
    for mat, p in zip(machine_matrices, machine_prizes):
        moves = np.linalg.solve(mat, p + 10000000000000)
        m = (round(moves[0]), round(moves[1]))
        if np.all(moves >= 0) and np.allclose(moves, moves.round(), rtol=1e-15, atol=1e-15):
            sol_part2 += 3 * round(moves[0]) + round(moves[1])
 
    print("Part 2:", round(sol_part2))


if __name__ == "__main__":
    start = time.time()
    solve()
    print(f"Run time: {time.time() - start:.3f}s")
