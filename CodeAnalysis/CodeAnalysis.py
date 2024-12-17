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

program = []

for line in file:
    if line.startswith("Register"):
        char = line.split()[1][:-1]
        val = int(line.split()[-1])
        registers[char] = val
    if line.startswith("Program"):
        program = [int(val) for val in line.split()[-1].split(',')]
best = 0
for i in range(100_000_000):
    if i % 100_000 == 0:
        print(i)
    out = []
    registers['A'] = i * 8**10 + 0o3701236017
    pointer = 0
    while pointer < len(program):
        op_code = program[pointer]
        pointer += 1
        val = program[pointer]
        pointer += 1
        if op_code == 0:
            val = resolve_combo(val)
            registers['A'] = floor(registers['A'] / float(2**val))
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
            if val%8 != program[len(out)]:
                break
            out.append(str(val % 8))
            if len(out) > best:
                print(oct(i * 8**10 + 0o3701236017), out)
                best = len(out)
                print(program)
        elif op_code == 6:
            val = resolve_combo(val)
            registers['B'] = floor(registers['A'] / float(2**val))
        elif op_code == 7:
            val = resolve_combo(val)
            registers['C'] = floor(registers['A'] / float(2**val))
    if len(out) == len(program):
        print(",".join(out))
        print(i * 8**10 + 0o3701236017)
        break