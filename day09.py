from collections import deque
from dataclasses import dataclass
import heapq
from itertools import zip_longest
import os
import time

@dataclass
class FileDesc:
    pos: int
    size: int
    id_: int

    def __lt__(self, other):
        return self.pos > other.pos

def solve():
    input_file_contents = open(os.path.join("input", "day09")).read().rstrip()
    #input_file_contents = "2333133121414131402"
    empty = deque()
    files = []
    pos = 0
    file_id = 0
    for f, e in zip_longest(input_file_contents[::2], input_file_contents[1::2], fillvalue="0"):
        if int(f) > 0:
            files.append(FileDesc(pos, int(f), file_id))
            file_id += 1
            pos += int(f)
        if int(e) > 0:
            empty.append((pos, int(e)))
            pos += int(e)

    heapq.heapify(files)
    file = heapq.heappop(files)
    empty_pos, empty_size = empty.popleft()
    while empty_pos < file.pos:
        if file.size == 0:
            file = heapq.heappop(files)
        to_insert = min(file.size, empty_size)
        if to_insert > 0:
            heapq.heappush(files, FileDesc(empty_pos, to_insert, file.id_))
            empty_pos += to_insert
            empty_size -= to_insert
            file.size -= to_insert
        if empty_size == 0:
            empty_pos, empty_size = empty.popleft()

    if file.size:
        heapq.heappush(files, FileDesc(file.pos, file.size, file.id_))
    files = sorted(files, reverse=True)
    sol_part1 = 0
    for f in files:
        sol_part1 += f.id_ * f.size * (2 * f.pos + f.size - 1) // 2

    print("Part 1:", sol_part1)

    empty = []
    files = {}
    pos = 0
    file_id = 0
    for f, e in zip_longest(input_file_contents[::2], input_file_contents[1::2], fillvalue="0"):
        if int(f) > 0:
            files[file_id] = (pos, int(f))
            file_id += 1
            pos += int(f)
        if int(e) > 0:
            empty.append((pos, int(e)))
            pos += int(e)

    files_defrag = {}
    for fid, (fpos, fsize) in reversed(files.items()):
        for i, (epos, esize) in enumerate(empty):
            if epos > fpos:
                files_defrag[fid] = (fpos, fsize)
                break
            if esize >= fsize:
                files_defrag[fid] = (epos, fsize)
                empty.remove((epos, esize))
                if fsize < esize:
                    empty.insert(i, (epos + fsize, esize - fsize))
                break
                
    sol_part2 = 0
    for fid, (fpos, fsize) in files_defrag.items():
        sol_part2 += fid * fsize * (2 * fpos + fsize - 1) // 2

    print("Part 2:", sol_part2)


if __name__ == "__main__":
    start = time.time()
    solve()
    print(f"Run time: {time.time() - start:.3f}s")
