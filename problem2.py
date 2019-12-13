# OPCODES
ADD = 1
MUL = 2
HLT = 99

OPCODE_ROUTINE_LOOKUP_TABLE = {
    ADD: lambda parm1, parm2: (parm1 + parm2),
    MUL: lambda parm1, parm2: (parm1 * parm2),
    HLT: lambda: halt(),
}

BIT_WIDT = 4
EIP = 0  # ExecutionInstructionPointer


def halt():
    print("Execution halted! Thank you for playing, goodbye!")
    print(program)
    exit(0)


# program = [1, 9, 10, 3, 2, 3, 11, 0, 99, 30, 40, 50]
program = list(map(int, open('program').read().split(',')))


print(f"Welcome to the {BIT_WIDT} bit Intercode Computer\n")
print("Beginning processing of program input")
print(f"{program}\n")

while True:
    opcode = program[EIP]
    routine = OPCODE_ROUTINE_LOOKUP_TABLE[opcode]
    if opcode == HLT:
        routine()

    p1 = program[EIP + 1]
    p2 = program[EIP + 2]
    p3 = program[EIP + 3]  # Destination

    program[p3] = routine(program[p1], program[p2])

    EIP += BIT_WIDT  # move instruction pointer
