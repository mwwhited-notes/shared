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
Date     16.01.2025 ;
Revision 01 ;
Designer mwwhi ;
Company  unknown ;
Assembly None ;
Location unknown ;
Device   g16v8a ;

/* inputs */
PIN 2 = Control_Clock;
PIN 3 = Control_Halt_In;
PIN 4 = Control_MAR_In;
PIN 5 = Control_RAM_In;
PIN 6 = Control_RAM_Out;
PIN 7 = User_Inspect;
PIN 8 = User_Program;
PIN 9 = User_Write;

/* outputs */
PIN 13 = RAM_Write;
PIN 14 = RAM_Output_Enable;
PIN 15 = User_Output_Enable;
PIN 16 = Databus_Output_Enable;
PIN 17 = Databus_Direction;
PIN 18 = Halt_Out;
PIN 19 = MAR_Clock;

/* combinatorial logic */
Databus_Direction = !Control_RAM_Out & !User_Program;
Databus_Output_Enable = (Control_RAM_In & Control_RAM_Out) # User_Program;
Halt_Out = Control_Halt_In # User_Program;
MAR_Clock = !Control_MAR_In & Control_Clock;
RAM_Output_Enable = (Control_RAM_Out & !User_Program) # (!User_Inspect & User_Program);
RAM_Write = (Control_RAM_In & !User_Program) # (User_Program & !User_Write);
User_Output_Enable = User_Inspect # !User_Program;
```

## Rules

```logic
/RAM_Write = (/ControlRAMIn ∧ ¬UserProgram) ∨ (UserProgram ∧ ¬UserWrite)
/RAM_Output_Enable = (/ControlRAMOut ∧ ¬UserProgram) ∨ (¬UserInspect ∧ UserProgram)
/User_Output_Enable = UserInspect ∨ ¬UserProgram
/Databus_Output_Enable = (/ControlRAMIn ∧ /ControlRAMOut) ∨ UserProgram
Databus_Direction = ¬(/ControlRAMOut) ∧ ¬UserProgram
Halt_Out = ControlHaltIn ∨ UserProgram
MAR_Clock = ¬(/ControlMARIn) ∧ ControlClock
```

### Data Bus

When the memory is in program mode direct access to memory should be allowed and isolated from the databus.  This may be acomplished by disabling the output on the databus transceiver.  

### Halt Control

Then the memory is in program mode the CPU should be halted.

### Memory Address Register Control

The memory address register should be clocked with the assertion request.

### Memory Read Control

When the memory is not in program mode the control assertions should control access to the memory.  `CE` is chip enable, `RI` is RAM in, `RO` is RAM out.  

When memory is in program mode the control for RAM access will be provided by the User input. If additional in program and inspect the current value of the memory will be output from the RAM control.  When not in inspect the mode is `preview` at which point the value from the user transceiver will be passed to the RAM chip.  While in preview it is also possible to assert a write which will save the user value to the current memory address.

## Design Tools

- [Digital](https://github.com/hneemann/Digital)
- [WinCUPL](https://www.microchip.com/en-us/development-tool/WinCUPL)
- [Truth Table Maker](https://truthtablemaker.com/)