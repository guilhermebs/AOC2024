import os
import re
import sys
import time

import numpy as np
import matplotlib.pyplot as plt


def solve():
    input_file_contents = open(os.path.join("input", "day14")).read().rstrip()
    robot_p_list = []
    robot_v_list = []
    for m in re.finditer(r"p=(\d+),(\d+) v=(\-?\d+),(\-?\d+)", input_file_contents):
        robot_p_list.append((int(m.group(1)), int(m.group(2))))
        robot_v_list.append((int(m.group(3)), int(m.group(4))))

    robot_p = np.array(robot_p_list)
    robot_v = np.array(robot_v_list)
    size_ = np.array([101, 103])

    robot_p += (robot_v * 100)
    robot_p %= size_

    sol_part1 = np.sum((robot_p[:, 0] < size_[0]//2) & (robot_p[:, 1] < size_[1]//2))
    sol_part1 *= np.sum((robot_p[:, 0] > size_[0]//2) & (robot_p[:, 1] < size_[1]//2))
    sol_part1 *= np.sum((robot_p[:, 0] < size_[0]//2) & (robot_p[:, 1] > size_[1]//2))
    sol_part1 *= np.sum((robot_p[:, 0] > size_[0]//2) & (robot_p[:, 1] > size_[1]//2))
    print("Part 1:", sol_part1)

    sol_part2 = None
    robot_p = np.array(robot_p_list)
    N = 300000
    i = 7172
    period = 168 - 65
    robot_p += i * robot_v
    robot_p %= size_
    while i < N - 1:
        if True: #i > 2000:
            fig = np.zeros(size_, dtype=int)
            fig[tuple(robot_p.T)] = 1
            plt.matshow(fig.T)
            plt.title(f"{i=}")
            plt.show()
        i += period
        print(i)
        robot_p += period * robot_v
        robot_p %= size_


    print("Part 2:", sol_part2)


if __name__ == "__main__":
    start = time.time()
    solve()
    print(f"Run time: {time.time() - start:.3f}s")
