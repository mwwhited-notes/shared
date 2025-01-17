# Memory Controller

SAP-1 - Ben Eater 8-Bit Computer

## Description

The combinational logic was replaced with a ATF16v8b and the following code

- [Source code](./CUPL_Memory%20Controller/RAMCTRL.PLD)
- [Truth Table](./logic%20tables.csv)

## IC Pinout

![](./Memory%20Controller-IC.svg)

## Logic Diagram

![](./Memory%20Controller-Logic.svg)

## Source Code

```cupl
Name     Memory Controller.dig ;
PartNo   00 ;
Date     15.01.2025 ;
Revision 01 ;
Designer mwwhi ;
Company  unknown ;
Assembly None ;
Location unknown ;
Device   g16v8a ;

/* inputs */
PIN 2 = CTR_CLK;
PIN 3 = CTR_HLT;
PIN 4 = CTR_MI;
PIN 5 = CTR_RI;
PIN 6 = CTR_RO;
PIN 7 = U_Inspect;
PIN 8 = U_Program;
PIN 9 = U_Write;

/* outputs */
PIN 12 = RAM_CE;
PIN 13 = RAM_WE;
PIN 14 = RAM_OE;
PIN 15 = U_OE;
PIN 16 = Bus_OE;
PIN 17 = Bus_Dir;
PIN 18 = Halt_Out;
PIN 19 = MAR_Cp;

/* combinatorial logic */
Bus_Dir = CTR_RI & !CTR_RO & !U_Program;
Bus_OE = (!CTR_RI & !CTR_RO) # (CTR_RI & CTR_RO) # U_Program;
Halt_Out = CTR_HLT # U_Program;
MAR_Cp = CTR_CLK & CTR_MI;
RAM_CE = (!CTR_RI & !CTR_RO & !U_Program) # (CTR_RI & CTR_RO & !U_Program);
RAM_OE = (CTR_RI & !U_Program) # (!CTR_RO & !U_Program) # (!U_Inspect & U_Program);
RAM_WE = (!CTR_RI & !U_Program) # (CTR_RO & !U_Program) # (U_Inspect & U_Program) # (U_Program & !U_Write);
U_OE = U_Inspect # !U_Program;
```

## Rules and Data Tables

### Data Bus

When the memory is in program mode direct access to memory should be allowed and isolated from the databus.  This may be acomplished by disabling the output on the databus transceiver.  

```cupl
Bus_Dir = CTR_RI & !CTR_RO & !U_Program;
Bus_OE = (!CTR_RI & !CTR_RO) # (CTR_RI & CTR_RO) # U_Program;
```

| /CTR RI | /CTR RO | U Program | | Bus Dir | /Bus OE |
| -------:| -------:| ---------:|-| -------:| -------:|
|       1 |       1 |         1 | |       X |       1 |
|       0 |       1 |         1 | |       X |       1 |
|       1 |       0 |         1 | |       X |       1 |
|       0 |       0 |         1 | |       X |       1 |
|       1 |       1 |         0 | |       0 |       1 |
|       0 |       1 |         0 | |       0 |       1 |
|       1 |       0 |         0 | |       1 |       0 |
|       0 |       0 |         0 | |       0 |       1 |

### Halt Control

Then the memory is in program mode the CPU should be halted.

```cupl
Halt_Out = CTR_HLT # U_Program;
```

| CTR HLT | U Program | | Halt Out |
| -------:| ---------:|-| --------:|
|       1 |         1 | |        1 |
|       0 |         1 | |        1 |
|       1 |         0 | |        1 |
|       0 |         0 | |        0 |

### Memory Address Register Control

The memory address register should be clocked with the assertion request.

```cupl
MAR_Cp = CTR_CLK & CTR_MI;
```

| CTR CLK | /CTR_MI   | | MAR Cp   |
| -------:| ---------:|-| --------:|
|       1 |         1 | |        1 |
|       0 |         1 | |        0 |
|       1 |         0 | |        0 |
|       0 |         0 | |        0 |

### Memory Read Control

When the memory is not in program mode the control assertions should control access to the memory.  `CE` is chip enable, `RI` is RAM in, `RO` is RAM out.  

When memory is in program mode the control for RAM access will be provided by the User input. If additional in program and inspect the current value of the memory will be output from the RAM control.  When not in inspect the mode is `preview` at which point the value from the user transceiver will be passed to the RAM chip.  While in preview it is also possible to assert a write which will save the user value to the current memory address.

```cupl
RAM_CE = (!CTR_RI & !CTR_RO & !U_Program) # (CTR_RI & CTR_RO & !U_Program);
RAM_OE = (CTR_RI & !U_Program) # (!CTR_RO & !U_Program) # (!U_Inspect & U_Program);
RAM_WE = (!CTR_RI & !U_Program) # (CTR_RO & !U_Program) # (U_Inspect & U_Program) # (U_Program & !U_Write);
U_OE = U_Inspect # !U_Program;
```

#### Run Mode

| /CTR RI | /CTR RO | U Program | | /RAM CE | /RAM OE | /RAM WE |
| -------:| -------:| ---------:|-| -------:| -------:| -------:|
|       1 |       1 |         0 | |       X |       1 |       1 |
|       0 |       1 |         0 | |       X |       1 |       1 |
|       1 |       0 |         0 | |       X |       1 |       1 |
|       0 |       0 |         0 | |       X |       1 |       1 |

## Design Tools

- [Digital](https://github.com/hneemann/Digital)
- [WinCUPL](https://www.microchip.com/en-us/development-tool/WinCUPL)
- [](https://truthtablemaker.com/)