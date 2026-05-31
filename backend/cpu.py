from memory import Memory
from exceptions import CPUException


class CPU:

    def __init__(self):

        self.memory = Memory(4096)

        self.registers = [0] * 16

        self.SP = 1536
        self.PC = 0

        self.running = False

        self.instructions = 0
        self.cycles = 0
        self.peak_stack = 0

        self.last_write = None
        self.trace = []

        self.stage = "FETCH"


    # RESET CPU
    def reset(self):

        self.memory.reset()

        self.registers = [0] * 16

        self.SP = 1536
        self.PC = 0

        self.running = False

        self.instructions = 0
        self.cycles = 0

        self.last_write = None
        self.trace = []

        self.stage = "FETCH"


    # LOAD PROGRAM
    def load_program(self, binary):

        for i, instr in enumerate(binary):
            self.memory.write(i, instr)

        self.PC = 0
        self.running = True


    # FETCH
    def fetch(self):

        self.stage = "FETCH"

        instr = self.memory.read(self.PC)

        if not isinstance(instr, tuple):
           self.running = False
           return ("HALT",)

        self.PC += 1

        return instr


    # EXECUTE
    def execute(self, instr):

        self.stage = "EXECUTE"

        op = instr[0]


        # LOAD CONSTANT
        if op == "LOADI":

            r = instr[1]
            v = instr[2]

            self.registers[r] = v
            self.last_write = r


        # ADD
        elif op == "ADD":

            r1 = instr[1]
            r2 = instr[2]

            self.registers[r1] += self.registers[r2]
            self.last_write = r1


        # SUB
        elif op == "SUB":

            r1 = instr[1]
            r2 = instr[2]

            self.registers[r1] -= self.registers[r2]
            self.last_write = r1
      

        # MUL
        elif op == "MUL":

            r1 = instr[1]
            r2 = instr[2]

            self.registers[r1] *= self.registers[r2]
            self.last_write = r1


        # DIV
        elif op == "DIV":

            r1 = instr[1]
            r2 = instr[2]

            if self.registers[r2] == 0:
                raise CPUException("Division by zero")

            self.registers[r1] //= self.registers[r2]
            self.last_write = r1


        # LOAD FROM MEMORY
        elif op == "LOAD":

            r = instr[1]
            addr = instr[2]

            self.registers[r] = self.memory.read(addr)
            self.last_write = r


        # STORE TO MEMORY
        elif op == "STORE":

            r = instr[1]
            addr = instr[2]

            self.memory.write(addr, self.registers[r])


        # PUSH STACK
        elif op == "PUSH":

            r = instr[1]

            self.SP -= 1

            self.memory.write(self.SP, self.registers[r])

            if self.SP < self.peak_stack:
                self.peak_stack = self.SP


        # POP STACK
        elif op == "POP":

            r = instr[1]

            self.registers[r] = self.memory.read(self.SP)

            self.SP += 1

            self.last_write = r


        # JUMP
        elif op == "JMP":

            addr = instr[1]

            self.PC = addr


        # JUMP IF ZERO
        elif op == "JZ":

            r = instr[1]
            addr = instr[2]

            if self.registers[r] == 0:
                self.PC = addr


        # CALL
        elif op == "CALL":

            addr = instr[1]

            self.SP -= 1

            self.memory.write(self.SP, self.PC)

            self.PC = addr


        # RETURN
        elif op == "RET":

            self.PC = self.memory.read(self.SP)

            self.SP += 1


        # HALT
        elif op == "HALT":

            self.running = False


        else:
            raise CPUException(f"Unknown instruction: {op}")


    # STEP EXECUTION
    def step(self):

        if not self.running:
            return self.get_state()

        instr = self.fetch()

        self.trace.append(instr)

        self.execute(instr)

        self.instructions += 1
        self.cycles += 1

        return self.get_state()


    # RUN PROGRAM
    def run(self):

        while self.running:

            instr = self.fetch()

            self.trace.append(instr)

            self.execute(instr)

            self.instructions += 1
            self.cycles += 1

        return self.get_state()


    # RETURN CPU STATE
    def get_state(self):

        mem_access = None

        if self.memory.last_access:
            mem_access = self.memory.last_access[1]

        return {

            "pc": self.PC,
            "registers": self.registers,
            "memory": self.memory.data,

            "sp": self.SP,

            "running": self.running,

            "mem_access": mem_access,

            "last_write": self.last_write,

            "trace": self.trace,

            "stage": self.stage,

            "binary": [],

            "stats": {
                "instructions": self.instructions,
                "cycles": self.cycles,
                "reads": self.memory.reads,
                "writes": self.memory.writes,
                "peak_stack": self.peak_stack
            }
        }