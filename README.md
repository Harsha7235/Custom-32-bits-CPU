Nexus CPU Flow - Custom 32-Bit CPU Simulator

Project Overview

Nexus CPU Flow is a complete educational CPU simulation platform developed as part of the Computer Organization and Embedded Computing (EOC) project. The project demonstrates the design, implementation, visualization, and execution of a custom 32-bit processor architecture from instruction fetch to write-back.

The project combines:

- Custom 32-bit CPU Architecture
- Logisim Evolution Hardware Design
- Custom Instruction Set Architecture (ISA)
- Register File and Memory System
- ALU Operations
- ROM and RAM Integration
- Execution Visualization
- FPGA Simulation Interface
- Web-Based Interactive Simulator (Base44)

---

Final Project Demo

Live Application:

https://nexus-cpu-flow-base44.app

---

Mid Project

The mid-project focused on designing and validating the complete CPU datapath using Logisim Evolution.

Implemented Components

- Program Counter (PC)
- Instruction ROM
- Register File (16 × 32-bit Registers)
- Arithmetic Logic Unit (ALU)
- Multiplexers and Demultiplexers
- RAM (4K × 32)
- Control Unit
- Instruction Decoder
- Write Enable Logic
- Clock and Reset System

Objectives

- Understand CPU internals
- Implement custom ISA
- Execute instructions through datapath
- Validate register transfers
- Perform memory read/write operations

---

Custom 32-Bit CPU Architecture

The processor follows a simplified RISC-style architecture.

Datapath Flow

PC
↓
ROM Fetch
↓
Instruction Decode
↓
Register Read
↓
ALU Execute
↓
Memory Access
↓
Write Back
↓
Next Instruction

---

Register File

The CPU contains 16 general-purpose registers:

R0 – R15

Features:

- 32-bit width
- Synchronous write
- Multiple read paths
- Register selection through decoder logic

---

Memory System

ROM

Stores executable machine code instructions.

Functions:

- Instruction Fetch
- Program Storage
- Opcode Generation

RAM

4K × 32-bit memory

Functions:

- LOAD operations
- STORE operations
- Data storage
- Runtime memory access

---

Instruction Set Architecture (ISA)

Arithmetic Instructions

Instruction| Description
ADD| Addition
SUB| Subtraction
MUL| Multiplication
DIV| Division
MOD| Modulus

Examples:

ADD R1,R2
SUB R3,R4
MUL R5,R6
DIV R7,R8
MOD R9,R10

---

Logical Instructions

Instruction| Description
AND| Logical AND
OR| Logical OR
XOR| Exclusive OR
NOT| Bitwise NOT

Examples:

AND R1,R2
OR R3,R4
XOR R5,R6
NOT R7

---

Shift Instructions

Instruction| Description
SHL| Shift Left
SHR| Shift Right
ASR| Arithmetic Shift Right

Examples:

SHL R1,2
SHR R2,1
ASR R3,1

---

Comparison Instructions

Instruction| Description
EQ| Equal
GT| Greater Than
LT| Less Than

Examples:

EQ R1,R2
GT R3,R4
LT R5,R6

---

Data Transfer Instructions

Instruction| Description
MOV| Register Transfer
LOAD| Memory Read
STORE| Memory Write

Examples:

MOV R1,R2
LOAD R1,[100]
STORE R2,[200]

---

Stack Instructions

Instruction| Description
PUSH| Push Stack
POP| Pop Stack

Examples:

PUSH R1
POP R2

---

Control Flow Instructions

Instruction| Description
JMP| Jump
ZJMP| Jump if Zero
NZJMP| Jump if Not Zero
CALL| Function Call
RET| Return
HALT| Stop Execution
NOP| No Operation

Examples:

JMP LOOP
ZJMP DONE
CALL FUNC
RET
HALT

---

CPU Flags

Zero Flag (ZF)

Set when result equals zero.

Sign Flag (SF)

Set when result is negative.

Overflow Flag (OF)

Set when arithmetic overflow occurs.

These flags are used by conditional instructions.

---

ALU Features

Supported operations:

- Add
- Subtract
- Multiply
- Divide
- Modulus
- Shift Left
- Shift Right
- Arithmetic Shift Right
- AND
- OR
- XOR
- NOT
- Comparisons

---

Execution Stages

Fetch

Instruction is read from ROM.

Decode

Opcode and operands are extracted.

Execute

ALU performs operation.

Memory

LOAD and STORE access RAM.

Write Back

Results are written into destination registers.

---

FPGA Integration

The final project includes FPGA-style visualization.

Supported Components

- Virtual Switches
- Virtual LEDs
- Register Monitoring
- Live Execution Display

Switches can be mapped to CPU inputs and LEDs can display register outputs and execution states.

---

Base44 Simulator Features

The web simulator provides:

- Instruction Execution
- Register Visualization
- Memory Viewer
- RAM Monitoring
- ROM Monitoring
- ALU Output Tracking
- Pipeline Observation
- Flag Visualization
- FPGA Switch Simulation
- LED Output Monitoring

---

Technologies Used

Hardware

- Logisim Evolution

Software

- Base44
- JavaScript
- HTML
- CSS

Concepts

- Computer Architecture
- CPU Design
- Instruction Set Architecture
- Memory Systems
- FPGA Concepts
- Digital Logic Design

---

Learning Outcomes

Through this project:

- Designed a complete CPU from scratch
- Implemented a custom ISA
- Built a register file architecture
- Integrated RAM and ROM systems
- Developed execution visualization tools
- Simulated FPGA interactions
- Understood processor datapath design
- Explored instruction execution workflows

---

Future Enhancements

- Pipelined CPU Design
- Cache Memory
- Interrupt Handling
- Advanced Branch Prediction
- FPGA Hardware Deployment
- Assembly Compiler
- VM Translation Support
- Performance Analysis Tools

---

Author

Pittu.Harsha vardhan Reddy

B.Tech Artificial Intelligence & Data Science
Cyber Physical Systems & Security

---

Project Status

Mid Project: Completed

Final Project: Active Development and Enhancement done
