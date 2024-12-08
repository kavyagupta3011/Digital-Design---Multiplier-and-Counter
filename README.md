# Digital Design - Multiplier and Counter


## **Project Overview**
This project focuses on the design, implementation, and analysis of two key digital circuits:  
1. A **2-bit Binary Multiplier** (Combinational Circuit).  
2. A **Mod-3 Up Counter** (Sequential Circuit).  

The circuits were designed and tested as part of the **ESS 102: Digital Design** course at IIIT Bangalore.

## **1. Combinational Circuit: 2-Bit Binary Multiplier**

### **Description**
A 2-bit binary multiplier multiplies two 2-bit binary numbers (A1A0 and B1B0) to produce a 4-bit binary output (P3P2P1P0).  
- **Inputs:** A1A0 (Multiplicand) and B1B0 (Multiplier).  
- **Outputs:** P3P2P1P0 (Product).

### **Implementation**
- Binary multiplication follows these rules:  
  - 0 × 0 = 0  
  - 0 × 1 = 0  
  - 1 × 0 = 0  
  - 1 × 1 = 1  
- Boolean Expressions for Outputs:  
  - P3 = A1 * A0 * B1 * B0  
  - P2 = A1 * B1 * (A0 * B0)’  
  - P1 = (A1 * B0) ⊕ (A0 * B1)  
  - P0 = A0 * B0  

### **Results**
- **Voltage Representation:** Logic 1 = 5V, Logic 0 = 0V.  
- Inputs and outputs were tested using a simulated testbench.  
- Negligible voltage values (e.g., 24.5 nV) were approximated to 0V, confirming outputs matched the truth table.

---

## **2. Sequential Circuit: Mod-3 Up Counter**

### **Description**
A Mod-3 counter counts through three states (00, 01, 10) before resetting to its initial state. It operates in "count-up" mode, incrementing the count with each clock pulse.  

- **Inputs:** Clock pulses.  
- **Outputs:** Three unique states representing counts (0, 1, 2).  
- **Flip-Flops Used:** 2.

### **Implementation**
- **State Transition:**  
  - 00 → 01 → 10 → 00.  
- **Components:** Two flip-flops connected together.  
- The counter transitions through three unique states using the clock pulse.

### **Results**
- State transition diagram, truth tables, and K-maps were used to verify design.  
- Simulated waveforms matched theoretical expectations, validating the Mod-3 counter's functionality.  

---

## **Key Features**
- Designed using Boolean algebra, state diagrams, and K-maps.  
- Verified outputs against theoretical truth tables for both circuits.  
- Accurate simulation of results using testbenches and waveforms.

---

## **Figures and Resources**
### **2-Bit Binary Multiplier**  
- Testbench Circuit.  
- Boolean Logic Subcircuit and Symbol.

### **Mod-3 Up Counter**  
- State Transition Diagram.  
- Truth Table and K-maps.  
- Waveforms and Output Snapshot.  

---

## **Conclusion**
This project demonstrates the design and implementation of essential combinational and sequential circuits, reinforcing core concepts in digital design. The circuits performed as expected, and results were validated through simulation.

