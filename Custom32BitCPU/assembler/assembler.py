# ==============================
# Custom 32-bit Multi-Format Assembler
# ==============================

OPCODES = {
    "LOAD":  1,   # I-type
    "STORE": 2,   # I-type
    "ADD":   3,   # R-type
    "SUB":   4,   # R-type
    "JMP":   5,   # J-type
    "HALT":  63   # Special
}

REGISTERS = {
    "R0": 0, "R1": 1, "R2": 2, "R3": 3,
    "R4": 4, "R5": 5, "R6": 6, "R7": 7
}


def assemble_line(line):
    line = line.replace(",", "").strip()
    parts = line.split()

    instr = parts[0]
    opcode = OPCODES[instr] << 26

    # ---------------- R-TYPE ----------------
    if instr in ["ADD", "SUB"]:
        rd  = REGISTERS[parts[1]] << 21
        rs1 = REGISTERS[parts[2]] << 16
        rs2 = REGISTERS[parts[3]] << 11
        return opcode | rd | rs1 | rs2

    # ---------------- I-TYPE ----------------
    elif instr == "LOAD":
        rd  = REGISTERS[parts[1]] << 21
        imm = int(parts[2]) & 0xFFFF
        return opcode | rd | imm

    elif instr == "STORE":
        rs1 = REGISTERS[parts[1]] << 21
        imm = int(parts[2]) & 0xFFFF
        return opcode | rs1 | imm

    # ---------------- J-TYPE ----------------
    elif instr == "JMP":
        addr = int(parts[1]) & 0x03FFFFFF
        return opcode | addr

    # ---------------- HALT ----------------
    elif instr == "HALT":
        return opcode

    else:
        raise ValueError("Unknown instruction")


def assemble_file(filename):
    output = []
    with open(filename, "r") as f:
        for line in f:
            if line.strip() == "" or line.startswith("#"):
                continue
            output.append(assemble_line(line))
    return output


if __name__ == "__main__":
    program = assemble_file("test1.asm")

    print("Machine Code:")
    for code in program:
        print(hex(code))
