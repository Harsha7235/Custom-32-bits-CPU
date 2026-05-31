OPCODES = {
    "LOADI": 0x01,
    "ADD": 0x02,
    "SUB": 0x03,
    "MUL": 0x04,
    "DIV": 0x05,

    "LOAD": 0x06,
    "STORE": 0x07,

    "PUSH": 0x08,
    "POP": 0x09,

    "JMP": 0x0A,
    "JZ": 0x0B,

    "CALL": 0x0C,
    "RET": 0x0D,

    "HALT": 0xFF
}


def encode_instruction(op, r1=0, r2=0, imm=0):

    return (op << 24) | (r1 << 20) | (r2 << 16) | (imm & 0xFFFF)


def reg(token):

    token = token.upper().replace("R", "")
    return int(token)


def encode(line, labels):

    tokens = line.replace(",", "").split()

    if not tokens:
        return None

    inst = tokens[0].upper()

    if inst not in OPCODES:
        raise Exception(f"Unknown instruction {inst}")

    op = OPCODES[inst]


    # LOADI r value
    if inst == "LOADI":

        return encode_instruction(
            op,
            reg(tokens[1]),
            0,
            int(tokens[2])
        )


    # ADD SUB MUL DIV
    elif inst in ["ADD", "SUB", "MUL", "DIV"]:

        return encode_instruction(
            op,
            reg(tokens[1]),
            reg(tokens[2]),
            0
        )


    # LOAD r addr
    elif inst == "LOAD":

        return encode_instruction(
            op,
            reg(tokens[1]),
            0,
            int(tokens[2])
        )


    # STORE r addr
    elif inst == "STORE":

        return encode_instruction(
            op,
            reg(tokens[1]),
            0,
            int(tokens[2])
        )


    # PUSH r
    elif inst == "PUSH":

        return encode_instruction(
            op,
            reg(tokens[1])
        )


    # POP r
    elif inst == "POP":

        return encode_instruction(
            op,
            reg(tokens[1])
        )


    # JMP label
    elif inst == "JMP":

        return encode_instruction(
            op,
            0,
            0,
            labels.get(tokens[1], int(tokens[1]))
        )


    # JZ r label
    elif inst == "JZ":

        return encode_instruction(
            op,
            reg(tokens[1]),
            0,
            labels.get(tokens[2], int(tokens[2]))
        )


    # CALL label
    elif inst == "CALL":

        return encode_instruction(
            op,
            0,
            0,
            labels.get(tokens[1], int(tokens[1]))
        )


    # RET
    elif inst == "RET":

        return encode_instruction(op)


    # HALT
    elif inst == "HALT":

        return encode_instruction(op)


    else:
        raise Exception(f"Unknown instruction {inst}")