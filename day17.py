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
    out = run_program(registers, program)
    sol_part1 = ",".join(str(i) for i in out)
    print("Part 1:", sol_part1)
    A_in = 0
    for p in reversed(program):
        for next_bits in range(8):
            A_tmp = (A_in << 3) + next_bits
            if run_program({"A": A_tmp, "B": 0, "C": 0}, program)[0] == p:
                A_in = A_tmp
                break
    registers = {"A": A_in, "B": 0, "C": 0}
    out = run_program(registers, program)
    assert out == program
    print("Part 2:", A_in)


if __name__ == "__main__":
    start = time.perf_counter_ns()
    solve()
    print(f"Run time: {(time.perf_counter_ns() - start)/1_000}µs")
