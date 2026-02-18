# =========================================================
# Custom 32-bit Secure CPU Simulator
# FINAL – Proper RESET + PAUSE (nand2tetris-like)
# =========================================================

import tkinter as tk
from tkinter import messagebox

# ================= ISA =================

OPCODES = {
    "LOAD":  1,
    "STORE": 2,
    "ADD":   3,
    "SUB":   4,
    "JMP":   5,
    "JGT":   6,
    "JLT":   7,
    "JEQ":   8,
    "HALT":  63
}

REGS = {f"R{i}": i for i in range(8)}

# ================= ASSEMBLER =================

def clean_line(raw):
    for sym in ["#", "//", ";"]:
        if sym in raw:
            raw = raw.split(sym)[0]
    return raw.strip()

def assemble(code):
    program, lines = [], []
    for raw in code.splitlines():
        line = clean_line(raw)
        if not line:
            continue

        parts = line.replace(",", " ").split()
        inst = parts[0]

        if inst not in OPCODES:
            raise ValueError(f"Illegal instruction: {inst}")

        op = OPCODES[inst] << 26

        if inst in ("ADD", "SUB"):
            op |= (REGS[parts[1]] << 21)
            op |= (REGS[parts[2]] << 16)
            op |= (REGS[parts[3]] << 11)

        elif inst == "LOAD":
            op |= (REGS[parts[1]] << 21)
            op |= int(parts[2]) & 0xFFFF

        elif inst == "STORE":
            op |= (REGS[parts[1]] << 21)
            op |= int(parts[2]) & 0xFFFF

        elif inst == "JMP":
            op |= int(parts[1]) & 0x03FFFFFF

        elif inst in ("JGT", "JLT", "JEQ"):
            op |= (REGS[parts[1]] << 21)
            op |= int(parts[2]) & 0x1FFFFF

        program.append(op)
        lines.append(line)

    return program, lines

# ================= CPU STATE =================

REG = [0]*8
MEM = [0]*64
PC = 0
PROGRAM = []
LINES = []
TRACE = []

MODE = "USER"
PROTECTED = 16

RUNNING = False
CLOCK = False
PAUSED = False
STAGE = "IDLE"
LAST_MEM = None

CLOCK_DELAY = 400

# ================= SECURITY =================

def security_error(msg):
    global RUNNING, CLOCK
    TRACE.append("SECURITY | " + msg)
    RUNNING = False
    CLOCK = False
    messagebox.showerror("Security Violation", msg)

# ================= PIPELINE =================

def cpu_step_pipeline():
    global STAGE

    if not RUNNING or PAUSED:
        return

    if PC >= len(PROGRAM):
        stop_execution()
        return

    instr = PROGRAM[PC]
    opcode = (instr >> 26) & 0x3F

    STAGE = "FETCH"
    update_all()
    root.after(CLOCK_DELAY, lambda: decode_stage(instr, opcode))

def decode_stage(instr, opcode):
    global STAGE
    if PAUSED: return
    STAGE = "DECODE"
    update_all()
    root.after(CLOCK_DELAY, lambda: execute_stage(instr, opcode))

def execute_stage(instr, opcode):
    global PC, STAGE, LAST_MEM

    if PAUSED: return

    STAGE = "EXECUTE"
    TRACE.append(f"| PC={PC:02} | {LINES[PC]}")

    if opcode == 1:
        REG[(instr>>21)&0x1F] = instr & 0xFFFF

    elif opcode == 2:
        addr = instr & 0xFFFF
        if MODE == "USER" and addr < PROTECTED:
            security_error("USER cannot write protected memory")
            return
        MEM[addr] = REG[(instr>>21)&0x1F]
        LAST_MEM = addr

    elif opcode == 3:
        rd = (instr>>21)&0x1F
        r1 = (instr>>16)&0x1F
        r2 = (instr>>11)&0x1F
        REG[rd] = REG[r1] + REG[r2]

    elif opcode == 4:
        rd = (instr>>21)&0x1F
        r1 = (instr>>16)&0x1F
        r2 = (instr>>11)&0x1F
        REG[rd] = REG[r1] - REG[r2]

    elif opcode == 5:
        PC = instr & 0x03FFFFFF
        finish_cycle()
        return

    elif opcode == 6:
        rs = (instr>>21)&0x1F
        if REG[rs] > 0:
            PC = instr & 0x1FFFFF
            finish_cycle()
            return

    elif opcode == 7:
        rs = (instr>>21)&0x1F
        if REG[rs] < 0:
            PC = instr & 0x1FFFFF
            finish_cycle()
            return

    elif opcode == 8:
        rs = (instr>>21)&0x1F
        if REG[rs] == 0:
            PC = instr & 0x1FFFFF
            finish_cycle()
            return

    elif opcode == 63:
        if MODE != "KERNEL":
            security_error("HALT is kernel-only")
            return
        TRACE.append("| HALT |")
        stop_execution()
        return

    PC += 1
    finish_cycle()

def finish_cycle():
    update_all()
    highlight_pc()
    if CLOCK and RUNNING and not PAUSED:
        root.after(CLOCK_DELAY, cpu_step_pipeline)

def stop_execution():
    global RUNNING, CLOCK, STAGE
    RUNNING = False
    CLOCK = False
    STAGE = "HALTED"
    update_all()

# ================= GUI ACTIONS =================

def load_program():
    global PROGRAM, LINES, PC, RUNNING, TRACE, MODE, PAUSED, LAST_MEM
    try:
        PROGRAM, LINES = assemble(code_box.get("1.0", tk.END))
    except Exception as e:
        messagebox.showerror("Assembler Error", str(e))
        return

    PC = 0
    TRACE.clear()
    LAST_MEM = None
    PAUSED = False

    for i in range(8): REG[i] = 0
    for i in range(64): MEM[i] = 0

    MODE = mode_var.get()
    RUNNING = True
    update_all()
    highlight_pc()

def step():
    global PAUSED
    PAUSED = False
    if RUNNING:
        cpu_step_pipeline()

def run_all():
    global CLOCK, PAUSED
    PAUSED = False
    if RUNNING:
        CLOCK = True
        cpu_step_pipeline()

def pause():
    global PAUSED
    PAUSED = True

def reset():
    global RUNNING, CLOCK, PAUSED, PC, STAGE, LAST_MEM, PROGRAM, LINES
    RUNNING = False
    CLOCK = False
    PAUSED = False
    PC = 0
    STAGE = "IDLE"
    LAST_MEM = None
    PROGRAM = []
    LINES = []
    TRACE.clear()

    for i in range(8): REG[i] = 0
    for i in range(64): MEM[i] = 0

    code_box.delete("1.0", tk.END)
    code_box.tag_remove("hl", "1.0", tk.END)
    reg_box.delete("1.0", tk.END)
    trace_box.delete("1.0", tk.END)
    mem_box.delete("1.0", tk.END)
    stage_label.config(text="PIPELINE STAGE : IDLE")

# ================= SPEED =================

def set_speed(val):
    global CLOCK_DELAY
    CLOCK_DELAY = int(800 - int(val))

# ================= UI UPDATE =================

def update_all():
    reg_box.delete("1.0", tk.END)
    for i in range(8):
        reg_box.insert(tk.END, f"R{i} | {REG[i]}\n")
        reg_box.insert(tk.END, "-"*12 + "\n")

    trace_box.delete("1.0", tk.END)
    for t in TRACE:
        trace_box.insert(tk.END, t + "\n")
        trace_box.insert(tk.END, "-"*40 + "\n")

    mem_box.delete("1.0", tk.END)
    for i in range(64):
        tag = "chg" if i == LAST_MEM else ""
        mem_box.insert(tk.END, f"MEM[{i:02}] | {MEM[i]}\n", tag)
        mem_box.insert(tk.END, "-"*18 + "\n")
    mem_box.tag_config("chg", background="#90EE90")

    stage_label.config(text=f"PIPELINE STAGE : {STAGE}")

def highlight_pc():
    code_box.tag_remove("hl", "1.0", tk.END)
    if PC < len(LINES):
        code_box.tag_add("hl", f"{PC+1}.0", f"{PC+1}.end")
        code_box.tag_config("hl", background="yellow")

# ================= GUI =================

root = tk.Tk()
root.title("Custom 32-bit Secure CPU Simulator")
root.geometry("1350x720")

tk.Label(root, text="Assembly Code").place(x=20, y=10)
code_box = tk.Text(root, width=42, height=22, font=("Courier", 10))
code_box.place(x=20, y=40)

tk.Label(root, text="Registers").place(x=380, y=10)
reg_box = tk.Text(root, width=18, height=14, font=("Courier", 10))
reg_box.place(x=380, y=40)

tk.Label(root, text="Execution Trace").place(x=580, y=10)
trace_box = tk.Text(root, width=45, height=22, font=("Courier", 10))
trace_box.place(x=580, y=40)

tk.Label(root, text="Data Memory").place(x=980, y=10)
mem_box = tk.Text(root, width=24, height=22, font=("Courier", 10))
mem_box.place(x=980, y=40)

stage_label = tk.Label(root, text="PIPELINE STAGE : IDLE",
                       font=("Arial", 11, "bold"), fg="blue")
stage_label.place(x=20, y=650)

mode_var = tk.StringVar(value="USER")
tk.Radiobutton(root, text="USER", variable=mode_var, value="USER").place(x=250, y=650)
tk.Radiobutton(root, text="KERNEL", variable=mode_var, value="KERNEL").place(x=320, y=650)

tk.Label(root, text="Clock Speed").place(x=420, y=650)
speed = tk.Scale(root, from_=0, to=700, orient="horizontal",
                 showvalue=False, command=set_speed, length=200)
speed.set(400)
speed.place(x=500, y=630)

tk.Button(root, text="LOAD", width=10, command=load_program).place(x=750, y=650)
tk.Button(root, text="STEP", width=10, command=step).place(x=860, y=650)
tk.Button(root, text="RUN", width=10, command=run_all).place(x=970, y=650)
tk.Button(root, text="PAUSE", width=10, command=pause).place(x=1080, y=650)
tk.Button(root, text="RESET", width=10, command=reset).place(x=1190, y=650)

root.mainloop()
