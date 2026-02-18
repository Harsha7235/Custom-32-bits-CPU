# ==============================
# Custom 32-bit Multi-Format CPU Emulator
# ==============================

# Registers
REG = [0] * 8
PC = 0
RUNNING = True

# Memory
CODE_MEMORY = []
DATA_MEMORY = [0] * 1024

# Opcodes
OP_LOAD  = 1
OP_STORE = 2
OP_ADD   = 3
OP_SUB   = 4
OP_JMP   = 5
OP_HALT  = 63


def load_program(program):
    global CODE_MEMORY
    CODE_MEMORY = program.copy()


def fetch():
    global PC
    instr = CODE_MEMORY[PC]
    PC += 1
    return instr


def decode_execute(instr):
    global PC, RUNNING

    opcode = (instr >> 26) & 0x3F

    # -------- R-TYPE --------
    if opcode in [OP_ADD, OP_SUB]:
        rd  = (instr >> 21) & 0x1F
        rs1 = (instr >> 16) & 0x1F
        rs2 = (instr >> 11) & 0x1F

        if opcode == OP_ADD:
            REG[rd] = REG[rs1] + REG[rs2]
        else:
            REG[rd] = REG[rs1] - REG[rs2]

    # -------- I-TYPE --------
    elif opcode == OP_LOAD:
        rd  = (instr >> 21) & 0x1F
        imm = instr & 0xFFFF
        REG[rd] = imm

    elif opcode == OP_STORE:
        rs1 = (instr >> 21) & 0x1F
        imm = instr & 0xFFFF
        DATA_MEMORY[imm] = REG[rs1]

    # -------- J-TYPE --------
    elif opcode == OP_JMP:
        addr = instr & 0x03FFFFFF
        PC = addr

    # -------- HALT --------
    elif opcode == OP_HALT:
        RUNNING = False

    else:
        print("Illegal instruction")
        RUNNING = False


def run():
    global RUNNING
    RUNNING = True
    while RUNNING:
        instr = fetch()
        decode_execute(instr)


if __name__ == "__main__":

    # Machine code copied from assembler output
    program = [
        0x0410000A,  # LOAD R1, 10
        0x04200014,  # LOAD R2, 20
        0x0C610000,  # ADD R3, R1, R2
        0xFC000000   # HALT
    ]

    load_program(program)
    run()

    print("Final Register Values:")
    for i in range(8):
        print(f"R{i} =", REG[i])
