class Assembler:

    OPCODES = {
        "LOADI": "0001",
        "ADD": "0010",
        "SUB": "0011",
        "MUL": "0100",
        "DIV": "0101",
        "LOAD": "0110",
        "STORE": "0111",
        "PUSH": "1000",
        "POP": "1001",
        "JMP": "1010",
        "HALT": "1111",
        "CALL": "1011",
        "RET": "1100",
        "JZ": "1101"
    }

    def reg(self, r):
        return format(int(r), "04b")

    def val(self, v):
        return format(int(v), "08b")

    def addr(self, a):
        return format(int(a), "012b")

    def assemble(self, code):

        lines = code.strip().split("\n")
        binary = []

        for line in lines:

            parts = line.strip().split()

            if not parts:
                continue

            op = parts[0].upper()

            opcode = self.OPCODES.get(op)

            if not opcode:
                raise Exception(f"Unknown instruction {op}")

            if op == "LOADI":

                r = self.reg(parts[1])
                v = self.val(parts[2])

                instr = opcode + r + v

            elif op in ["ADD", "SUB", "MUL", "DIV"]:

                r1 = self.reg(parts[1])
                r2 = self.reg(parts[2])

                instr = opcode + r1 + r2 + "0000"

            elif op in ["LOAD", "STORE"]:

                r = self.reg(parts[1])
                addr = self.addr(parts[2])

                instr = opcode + r + addr

            elif op in ["PUSH", "POP"]:

                r = self.reg(parts[1])
                instr = opcode + r + "00000000"

            elif op == "JMP":

                addr = self.addr(parts[1])
                instr = opcode + "0000" + addr

            elif op == "HALT":

                instr = opcode + "000000000000"
           
            elif op == "JZ":

                r = self.reg(parts[1])
                addr = self.addr(parts[2])
                instr = opcode + r + addr 
           
            elif op == "CALL":

                if len(parts) < 2:
                    raise Exception("CALL requires an address")

                addr = self.addr(parts[1])
                instr = opcode + "0000" + addr

            elif op == "RET":

                instr = opcode + "000000000000"

            binary.append(instr)

        return binary