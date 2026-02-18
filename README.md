# Custom 32-Bit Secure Software-Based CPU Simulator

## Overview

This project presents the design and implementation of a **custom 32-bit secure processor architecture** with a user-defined assembly language.  
The processor is fully software-emulated and includes runtime security enforcement, conditional branching, protected memory regions, and a visual pipeline execution model.

The simulator demonstrates core computer architecture concepts including instruction decoding, register-based execution, memory management, control flow, and privilege-level security.

---

## Key Features

### 1. 32-Bit Custom Instruction Set Architecture (ISA)
- Custom opcode format
- Register-based computation (R0–R7)
- Arithmetic instructions (ADD, SUB)
- Memory instructions (LOAD, STORE)
- Control flow instructions (JMP, JGT, JLT, JEQ)
- Privileged HALT instruction

### 2. Dual Execution Modes
- USER Mode (restricted)
- KERNEL Mode (privileged)

Security enforcement includes:
- Protected memory region (0–15)
- HALT allowed only in kernel mode
- Jump target validation

### 3. Visual Pipeline Execution
Each instruction passes through:
- FETCH
- DECODE
- EXECUTE

Clock-based execution with adjustable speed.

### 4. Interactive Dashboard
The simulator includes:
- Assembly code editor
- Register monitor
- Execution trace viewer
- Data memory panel (0–63)
- Clock speed control (Slow ↔ Fast)
- Run / Step / Pause / Reset controls

---

## Architecture Design

The processor follows a simplified RISC-style model:

- 32-bit instruction format
- 8 general purpose registers
- 64-word data memory
- Program Counter (PC)
- Control Unit (software-emulated)
- Security enforcement layer

Instruction format structure:

- 6-bit opcode
- Register fields
- Immediate or jump fields

---

## Instruction Set

| Instruction | Description |
|------------|------------|
| LOAD Rd, Imm | Load immediate value |
| STORE Rs, Addr | Store register value to memory |
| ADD Rd, Rs1, Rs2 | Addition |
| SUB Rd, Rs1, Rs2 | Subtraction |
| JMP Addr | Unconditional jump |
| JGT Rs, Addr | Jump if register > 0 |
| JLT Rs, Addr | Jump if register < 0 |
| JEQ Rs, Addr | Jump if register == 0 |
| HALT | Stop execution (Kernel only) |

---

## Security Model

The processor implements hardware-level security constraints:

- Memory addresses 0–15 are protected
- USER mode cannot modify protected memory
- HALT is restricted to KERNEL mode
- Invalid jump detection

Security violations immediately halt execution.

---

## How to Run

### Requirements
- Python 3.x

### Run Simulator

```bash
python dashboard.py

### EXAMPLE
LOAD R1, 10
LOAD R2, 20
ADD R3, R1, R2
STORE R3, 18
HALT
