import os
import time


def get_operand(operand, registers):
    if operand < 4:
        return operand
    elif operand == 4:
        return registers["A"]
    elif operand == 5:
        return registers["B"]
    elif operand == 6:
        return registers["C"]


def run_program(registers, program):
    iptr = 0
    output = []
    while iptr < len(program):
        combo = program[iptr + 1]
        # adv
        if program[iptr] == 0:
            registers["A"] //= 2 ** get_operand(combo, registers)
            iptr += 2
        # bxl
        elif program[iptr] == 1:
            registers["B"] ^= combo
            iptr += 2
        # bst
        elif program[iptr] == 2:
            registers["B"] = get_operand(combo, registers) % 8
            iptr += 2
        # jnz
        elif program[iptr] == 3:
            iptr = combo if registers["A"] != 0 else iptr + 2
        # bxc
        elif program[iptr] == 4:
            registers["B"] ^= registers["C"]
            iptr += 2
        # out
        elif program[iptr] == 5:
            output.append(get_operand(combo, registers) % 8)
            iptr += 2
        # bdv
        elif program[iptr] == 6:
            registers["B"] = registers["A"] // 2 ** get_operand(combo, registers)
            iptr += 2
        # cdv
        elif program[iptr] == 7:
            registers["C"] = registers["A"] // 2 ** get_operand(combo, registers)
            iptr += 2

    return output


def solve():
    registers = {"A": 50230824, "B": 0, "C": 0}
    program = [2, 4, 1, 3, 7, 5, 0, 3, 1, 4, 4, 7, 5, 5, 3, 0]
    # B=A%8, B^=3, C=A//2**B, A=A//8, B=B^4, B=B^C, OUT B%8, JNZ
    # B = 3 last bits of A ^ 011
    # C = A // 2**B
    # A >> 3
    # B ^4 ^C
    # 3 last bits of B
    # C = A >> (A%8 ^ 3)
    # B = A%8 ^ 7 ^ C
    # A >> (A%8^3) = A%8 ^ 7 ^ B
    out = run_program(registers, program)
    sol_part1 = ",".join(str(i) for i in out)
    print("Part 1:", sol_part1)
    A_in = 0
    for p in reversed(program):
        for next_bits in range(8):
            A_tmp = (A_in << 3) + next_bits
            C = A_tmp >> (next_bits ^ 3)
            B = (next_bits ^ 7 ^ C) % 8
            if B == p:
                A_in <<= 3
                A_in += next_bits
                break
    registers = {"A": A_in, "B": 0, "C": 0}
    out = run_program(registers, program)
    assert out == program
    print("Part 2:", A_in)


if __name__ == "__main__":
    start = time.time()
    solve()
    print(f"Run time: {time.time() - start:.3f}s")
