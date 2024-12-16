# Implementation of the game "Binding of Issac" on an FPGA

## Description
This is the culmination of a semester-worth of ECE 385-Digital Systems Laboratory at the University of Illinois. The various labs and final project were done together by Gustavo Fonseca and Hunter Baisden. In this class, we explored a variety of FPGA concepts. 

For the final project of this class, we designed and developed our game: "Binding of an ECE Major". This game was inspired by the game "Binding of Issac".

I would like to highlight that this game was designed and implemented purely with digital logic in an FPGA; i.e., no software was compiled or interpreted. The game only uses sequential and combinatorial digital circuits. Watch our demo [here](https://youtu.be/i_g9_j7QDNE)!

## Final Project Files

- **[Final Report](./Binding_of_ECE_game_files/Binding%20of%20ECE%20Final%20Report.pdf)**
  - Contains detailed description of game implementation.

- **[src](./Binding_of_ECE_game_files/src)**
  - Contains the all the code and implemnetation to set up the game on the FPGA.

 - **[ram](./Binding_of_ECE_game_files/ram)**
   - Contains the files to set up the RAM for the FPGA.

- **[source](./Binding_of_ECE_game_files/source)**
  - Contains all the sprites used for the game.

Each lab, all of its components, and the correspinding report can be found inside of this repository. 

## Labs 

**Lab 1:** a solo lab where the work was already done. The corresponding report is only Gustavo's Report

**Lab 2:** fully hardware 4 bit processor with 8 arithmetic functions, built entirely on a breadboard

**Lab 3:** introduction to system verilog saw the creation of 3 different adders

**Lab 4:** building on the adders this is an 8-bit shift multiplier

**Lab 5:** this is almost the fully implementation of lc3 inside of system veriilog, with a few things missing. Called slc3

**Lab 6:** introduced the vga capabilites as well as usb protocol

**Lab 7:** pallatte colors and screen savers

**Final Project:** *The Binding of an ECE Major* an implemtation of the binding of isaac with an ECE twist. It can be seen [here](https://youtu.be/i_g9_j7QDNE)

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
