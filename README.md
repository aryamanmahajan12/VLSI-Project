# VLSI-Project

## The problem statement consisted of designing a 4-bit ALU capable of
   performing the following operations:
  1 Addition
  2 Subtraction
  3 Comparison
  4 Logical AND
  
The circuit consisted of a decoder, in line with three parallel enabler
circuits, which were series connected to the respective circuits. The
operation selected through the decoder activates the input bits through
the respective enabler. The input bits are then fed to the required circuit
for logical processing.


**The adder circuit was interchangeably used as a subtractor circuit as well,
based upon the choice of input given to the decoder. The input bits for this
circuit are each passed through XOR gates and are processed with a select
line. Thus, based upon the logic value in this select line, we can
interchangeably use the circuit as both an adder and a subtractor,
reducing the hardware cost and improving the efficiency of the design
considerably.**


-The fabrication level circuit was designed on the ‘MAGIC Layout’
application. The design was done using 180 nm technology.

-The circuit was tested on the pre-layout stage using NGSpice
programming.

-The final testing for the circuit for all input values was comprehensively
achieved using - iVerilog
