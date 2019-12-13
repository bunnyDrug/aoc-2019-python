# OPCODES
ADD = 1
MUL = 2
HLT = 99

# ROUTINES/MICROCODE?
ADD_ROUTINE = lambda parm1, parm2: (parm1 + parm2)
MUL_ROUTINE = lambda parm1, parm2: (parm1 * parm2)
HLT_ROUTINE = lambda: halt()


OPCODE_ROUTINE_LOOKUP_TABLE = {
    ADD: ADD_ROUTINE,
    MUL: MUL_ROUTINE,
    HLT: HLT_ROUTINE,
}

BIT_WIDT = 4
EIP = 0  # not a constant but makes sense to declare here


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

    # read the contents of the program at the register locations - if r1 = 3
    # then we are reading the program memory at position 3
    output = routine(program[p1], program[p2])
    print(f"{output}")
    # program[p3] = output
    # run the routine microcode
    # and store it in the reg

    EIP += BIT_WIDT  # move instruction pointer
