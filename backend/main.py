from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from cpu import CPU
from assembler.assembler import Assembler
from vm.vm_translator import VMTranslator
from analyzer.performance import PerformanceAnalyzer
from analyzer.code_analyzer import CodeAnalyzer
from modes import mode_manager
from encoder import encode


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

cpu = CPU()
assembler = Assembler()
vm = VMTranslator()
analyzer = CodeAnalyzer()


@app.post("/analyze")
def analyze_code(payload: dict):

    code = payload.get("code", "")
    result = analyzer.analyze(code)

    return result


@app.get("/")
def root():
    return {"status": "CPU Backend Running"}


@app.post("/mode")
def set_mode(payload: dict):

    mode = payload.get("mode", "developer")

    mode_manager.set_mode(mode)

    return {"mode": mode_manager.get_mode()}


@app.get("/mode")
def get_mode():

    return {"mode": mode_manager.get_mode()}


@app.post("/vm")
def translate_vm(payload: dict):

    code = payload.get("code", "")
    asm = vm.translate(code)

    return {"assembly": asm}


@app.get("/stats")
def stats():

    return analyzer.analyze(cpu)


@app.post("/load")
def load(program: dict):

    code = program["code"]

    # ---------- GENERATE 32 BIT BINARY ----------
    binary = []
    labels = {}

    lines = code.strip().split("\n")

    pc = 0
    for line in lines:
        line = line.strip()
        if not line:
            continue
        if line.endswith(":"):
            labels[line[:-1]] = pc
        else:
            pc += 1

    for line in lines:

        line = line.strip()

        if not line or line.endswith(":"):
            continue

        encoded = encode(line, labels)

        binary.append(format(encoded, "032b"))

    # ---------- PARSE FOR CPU EXECUTION ----------
    parsed = []

    for line in code.split("\n"):

        parts = line.strip().split()

        if not parts:
            continue

        op = parts[0].upper()

        if op == "LOADI":
            parsed.append(("LOADI", int(parts[1]), int(parts[2])))

        elif op in ["ADD", "SUB", "MUL", "DIV"]:
            parsed.append((op, int(parts[1]), int(parts[2])))

        elif op in ["LOAD", "STORE"]:
            parsed.append((op, int(parts[1]), int(parts[2])))

        elif op in ["PUSH", "POP"]:
            parsed.append((op, int(parts[1])))

        elif op == "JMP":
            parsed.append(("JMP", int(parts[1])))

        elif op == "JZ":
            parsed.append(("JZ", int(parts[1]), int(parts[2])))

        elif op == "CALL":
            parsed.append(("CALL", int(parts[1])))

        elif op == "RET":
            parsed.append(("RET",))

        elif op == "HALT":
            parsed.append(("HALT",))

    cpu.reset()
    cpu.load_program(parsed)

    state = cpu.get_state()

    state["binary"] = binary

    return state


@app.post("/step")
def step():

    return cpu.step()


@app.post("/run")
def run():

    return cpu.run()


@app.post("/reset")
def reset():

    cpu.reset()

    return cpu.get_state()