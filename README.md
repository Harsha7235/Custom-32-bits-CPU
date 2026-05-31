Custom 32-Bit CPU Simulator (Mid Project)

Overview

The Custom 32-Bit CPU Simulator is an educational computer architecture project designed to demonstrate how a processor executes instructions, manages memory, performs arithmetic and logical operations, and interacts with hardware components. The project combines CPU simulation, instruction execution, virtual machine concepts, debugging tools, and FPGA integration into a single interactive platform.

This repository contains the Mid Project implementation and ongoing development work.

---

Project Objectives

- Design a custom 32-bit CPU architecture
- Implement a custom Instruction Set Architecture (ISA)
- Simulate Fetch–Decode–Execute cycle
- Visualize registers, memory, and CPU operations
- Support assembly-level programming
- Implement Virtual Machine (VM) execution concepts
- Integrate FPGA-style switches and LEDs
- Provide debugging and performance analysis tools

---

Current Features (Mid Project)

CPU Architecture

- 32-bit processor design
- Program Counter (PC)
- Register File
- Arithmetic Logic Unit (ALU)
- Control Unit
- RAM Integration
- Stack Support

Instruction Set Architecture (ISA)

Implemented instruction categories include:

- Arithmetic Operations
  
  - ADD
  - SUB
  - MUL
  - DIV
  - MOD

- Logical Operations
  
  - AND
  - OR
  - XOR
  - NOT

- Shift Operations
  
  - SHL
  - SHR
  - ASR

- Comparison Operations
  
  - EQ
  - GT
  - LT

- Memory Operations
  
  - LOAD
  - STORE

- Stack Operations
  
  - PUSH
  - POP

- Control Operations
  
  - JMP
  - JZ
  - CALL
  - RET
  - HALT

Visualization

- Register monitoring
- Memory monitoring
- CPU execution tracking
- Debugging support

FPGA Integration

- Virtual FPGA board implementation
- Switch input support
- LED output display
- Clock control interface

---

Technology Stack

- Logisim Evolution
- CPU Design and Simulation
- Custom ISA Development
- Virtual Machine Concepts
- FPGA-Based Hardware Mapping
- Assembly Programming

---

Project Structure

CPU Core
├── Program Counter
├── Register File
├── ALU
├── Control Unit
├── RAM
└── Stack

Simulation Layer
├── Instruction Execution
├── Debugging
├── Visualization
└── Performance Tracking

Hardware Layer
├── FPGA Virtual Board
├── Switch Inputs
└── LED Outputs

---

Mid Project Status

Completed:

- CPU architecture design
- Register file implementation
- ALU implementation
- Memory integration
- ISA design
- Execution framework
- Virtual FPGA board

In Progress:

- Advanced VM support
- AI-assisted code generation improvements
- Complete ISA example generation
- Enhanced FPGA interaction
- Performance analytics dashboard

---

Future Enhancements (Final Project)

- Complete VM-to-Assembly translator
- Improved AI code generation
- Advanced debugging tools
- Real FPGA deployment support
- Performance comparison system
- Enhanced visualization features
- Complete ISA testing suite

---

Educational Purpose

This project is developed as part of a Computer Architecture and System Design learning initiative to understand processor internals, instruction execution, memory management, assembly language, virtual machines, and FPGA-based hardware interaction.

---

Author

Pittu.Harsha Vardhan Reddy

B.Tech AI & Data Science (Cyber Physical Systems & Security)

Amrita Vishwa Vidyapeetham, Coimbatore
