from math import floor

file = open('input.txt')

registers = dict()

def resolve_combo(combo_op):
    if combo_op < 4:
        return combo_op
    elif combo_op == 4:
        return registers['A']
    elif combo_op == 5:
        return registers['B']
    elif combo_op == 6:
        return registers['C']


def execute_program(reg_a, program):
    out = []
    registers['A'] = reg_a
    registers['B'] = 0
    registers['C'] = 0
    pointer = 0
    while pointer < len(program):
        op_code = program[pointer]
        pointer += 1
        val = program[pointer]
        pointer += 1
        if op_code == 0:
            val = resolve_combo(val)
            registers['A'] = floor(registers['A'] / float(2 ** val))
        elif op_code == 1:
            registers['B'] = registers['B'] ^ val
        elif op_code == 2:
            val = resolve_combo(val)
            registers['B'] = val % 8
        elif op_code == 3 and registers['A'] != 0:
            pointer = val
        elif op_code == 4:
            registers['B'] = registers['B'] ^ registers['C']
        elif op_code == 5:
            val = resolve_combo(val)
            out.append(val % 8)
        elif op_code == 6:
            val = resolve_combo(val)
            registers['B'] = floor(registers['A'] / float(2 ** val))
        elif op_code == 7:
            val = resolve_combo(val)
            registers['C'] = floor(registers['A'] / float(2 ** val))
    return out

def get_best(program, pos, curr):
    for val in range(8):
        if execute_program(curr * 8 + val, program) == program[pos:]:
            if pos == 0:
                return curr * 8 + val
            step = get_best(program, pos - 1, curr * 8 + val)
            if step is not None:
                return step
    return None
program = []

for line in file:
    if line.startswith("Register"):
        char = line.split()[1][:-1]
        val = int(line.split()[-1])
        registers[char] = val
    if line.startswith("Program"):
        program = [int(val) for val in line.split()[-1].split(',')]

print(get_best(program, len(program) - 1, 0))