# Implementation of the game "Binding of Issac" on an FPGA

## Description
This is the culmination of a semester-worth of ECE 385-Digital Systems Laboratory at the University of Illinois. The various labs and final project were done together by Gustavo Fonseca and Hunter Baisden. In this class, we explored a variety of FPGA concepts. 

For the final project of this class, we designed and developed our game: "Binding of an ECE Major". This game was inspired by the game "Binding of Issac".

I would like to highlight that this game was designed and implemented purely with digital logic in an FPGA; i.e., no software was compiled or interpreted. The game only uses sequential and combinatorial digital circuits. 

Watch our demo [here](https://youtu.be/i_g9_j7QDNE)!

## Final Project Files

- **[Final Report](./Binding_of_ECE_game_files/Binding%20of%20ECE%20Final%20Report.pdf)**
  - Contains detailed description of game implementation.

- **[src](./Binding_of_ECE_game_files/src)**
  - Contains all the code and implementation to set up the game on the FPGA.

 - **[ram](./Binding_of_ECE_game_files/ram)**
   - Contains the files to set up the RAM for the FPGA.

- **[source](./Binding_of_ECE_game_files/source)**
  - Contains all the sprites used for the game. 

## Interesting Labs 

In addition to the final project we also worked on several interesting labs as well.

- **[Four-Bit Processor Circuit](./Four_bit_processor_circuit)**
  - Implementation of a 4-bit processor with 8 arithmetic functions, built entirely on a breadboard.

- **[Eight-bit processor in FPGA](./Eight_bit_processor_fpga)**
  - Implementation of an 8-bit processor in SystemVerilog with 3 different adders.

 - **[Eight-bit Multipliers](./Eight_bit_adders_multipliers)**
   - Expansion of the 8-bit processor with an 8-bit shift multiplier.

- **[LC3 Assembly](./LC3_Assembly)**
  - Implementation of most of the LC3 assembly language using SystemVerilog.
 
- **[VGA USB Communication](./VGA_USB_communication)**
  - Implemented VGA video capabilities and USB communication with peripherals.
  - Fundamental building block for final project.

- **[Images in VGA](./Images_in_VGA)**
  - Implemented colors and sprites through the VGA output.
  - Fundamental building block for final project.

## Topics Covered

- **Combinational Logic**: Adders, multiplexers, and combinational networks in SystemVerilog.
- **Sequential Logic**: Counters, shift registers, and state machines.
- **Circuit Characteristics**: Timing analysis, delays, fanout, and synchronization.
- **FPGAs**: Prototyping digital designs on FPGA platforms.
- **Microprocessors and SoC**: Integration of processors, memory, and peripherals.
- **Logic Simulation**: Testbench creation and validation for digital systems.

## Skills and Technologies Used
- **Programming Language**: SystemVerilog, Assembly (for microprocessor programming)
- **Hardware**: FPGAs, Microprocessors
- **Tools**: Digital simulators, FPGA design tools (e.g., Vivado, Quartus)
- **Concepts**: Digital design, synchronization, timing analysis
- **Testing**: Simulation and verification using testbenches
