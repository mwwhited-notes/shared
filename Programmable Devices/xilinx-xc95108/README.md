# Xilinx XC95108

**CPLD (Complex Programmable Logic Device)**

## Device Information

| Field | Value |
|-------|-------|
| Manufacturer | Xilinx (now AMD) |
| Part Number | XC95108 |
| Family | XC9500 |
| Package | PLCC-84, TQFP-100, PQ160 |
| Status | Working |
| Date Acquired | - |
| Purchase Price | $0.00 (college) |
| Source | College |

## Specifications

| Specification | Value |
|--------------|-------|
| Architecture | CPLD |
| Macrocells | 108 |
| Function Blocks | 6 |
| I/O Pins | 81 (package dependent) |
| Registers | 108 |
| Product Terms | 540 (90 per FB) |
| tPD (pin-to-pin) | 7.5 ns |
| fMAX | 125 MHz |
| Operating Voltage | 5V |
| Technology | Flash (ISP) |

## XC9500 Family Comparison

| Part | Macrocells | I/O | Speed (ns) |
|------|------------|-----|------------|
| XC9536 | 36 | 34 | 5 |
| XC9572 | 72 | 52 | 5 |
| XC95108 | 108 | 81 | 7.5 |
| XC95144 | 144 | 81 | 7.5 |
| XC95216 | 216 | 166 | 10 |
| XC95288 | 288 | 192 | 10 |

## Architecture

### Function Block (FB)
- 18 macrocells per block
- 54 inputs (from interconnect)
- 18 outputs
- 90 product terms (5 per macrocell)

### Macrocell
- Configurable as combinatorial or registered
- D-type flip-flop with async preset/reset
- XOR gate for polarity control
- Individual output enable

## Block Diagram

```plantuml
@startuml
skinparam backgroundColor #FEFEFE
skinparam componentStyle rectangle

package "XC95108 CPLD" {
    package "Function Blocks (6)" {
        [FB1\n18 Macrocells] as FB1
        [FB2\n18 Macrocells] as FB2
        [FB3\n18 Macrocells] as FB3
        [FB4\n18 Macrocells] as FB4
        [FB5\n18 Macrocells] as FB5
        [FB6\n18 Macrocells] as FB6
    }
    
    [Fast CONNECT\nSwitch Matrix] as FSM
    
    [I/O Blocks\n81 pins] as IOB
    
    [JTAG\nTAP Controller] as JTAG
}

' Interconnections
FB1 <--> FSM
FB2 <--> FSM
FB3 <--> FSM
FB4 <--> FSM
FB5 <--> FSM
FB6 <--> FSM

FSM <--> IOB

' JTAG
JTAG --> FB1 : ISP
JTAG --> FB2 : ISP
JTAG --> FB3 : ISP
JTAG --> FB4 : ISP
JTAG --> FB5 : ISP
JTAG --> FB6 : ISP

' External
[JTAG\nTDI/TDO/TMS/TCK] as JTAG_EXT
JTAG_EXT --> JTAG

[I/O Pins\n(81 max)] as IO_EXT
IO_EXT <--> IOB

@enduml
```

## JTAG Programming Interface

| Pin | Function |
|-----|----------|
| TDI | Test Data In |
| TDO | Test Data Out |
| TMS | Test Mode Select |
| TCK | Test Clock |

### JTAG Wiring

| Programmer | XC95108 |
|------------|---------|
| TDI | TDI pin |
| TDO | TDO pin |
| TMS | TMS pin |
| TCK | TCK pin |
| VCC | VCCIO |
| GND | GND |

## Programming

| Method | Tools |
|--------|-------|
| JTAG/ISP | Xilinx Platform Cable, generic JTAG |
| Parallel Port | Xilinx Parallel Cable III (legacy) |

### Programming Software

| Software | Status |
|----------|--------|
| Xilinx ISE WebPACK | Free, supports XC9500 |
| Xilinx iMPACT | Programming utility |
| UrJTAG | Open-source JTAG |
| xc3sprog | Open-source Xilinx programmer |

## Design Flow

```
1. Write HDL (Verilog/VHDL) or schematic
          ↓
2. Synthesize (ISE XST)
          ↓
3. Implement (Fit to CPLD)
          ↓
4. Generate programming file (.jed)
          ↓
5. Program via JTAG (iMPACT)
```

## Verilog Example

```verilog
module counter (
    input  clk,
    input  reset,
    output reg [7:0] count
);

always @(posedge clk or posedge reset) begin
    if (reset)
        count <= 8'b0;
    else
        count <= count + 1;
end

endmodule
```

## VHDL Example

```vhdl
library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use IEEE.STD_LOGIC_ARITH.ALL;

entity counter is
    Port ( clk   : in  STD_LOGIC;
           reset : in  STD_LOGIC;
           count : out STD_LOGIC_VECTOR(7 downto 0));
end counter;

architecture Behavioral of counter is
    signal cnt : STD_LOGIC_VECTOR(7 downto 0) := "00000000";
begin
    process(clk, reset)
    begin
        if reset = '1' then
            cnt <= "00000000";
        elsif rising_edge(clk) then
            cnt <= cnt + 1;
        end if;
    end process;
    count <= cnt;
end Behavioral;
```

## Documentation

- [XC9500 Family Datasheet](https://www.xilinx.com/support/documentation/data_sheets/ds063.pdf)
- [XC9500 In-System Programming Guide](https://www.xilinx.com/support/documentation/application_notes/xapp058.pdf)
- [CPLD Design Techniques](https://www.xilinx.com/support/documentation/application_notes/xapp444.pdf)

## Software & Tools

### Official Tools (Synthesis)
- **Xilinx ISE WebPACK 14.7** - Free, last version to support XC9500
  - Download: https://www.xilinx.com/support/download/index.html/content/xilinx/en/downloadNav/vivado-design-tools/archive-ise.html
- **iMPACT** - Programming utility (part of ISE)

### Open-Source Programming Tools ✅

| Tool | XC95108 Support | Notes |
|------|-----------------|-------|
| [**xc3sprog**](https://xc3sprog.sourceforge.net/) | ✅ Full | Programs .jed directly, recommended |
| [OpenOCD](https://openocd.org/) | ⚠️ SVF only | Detect + SVF playback |
| [UrJTAG](http://urjtag.org/) | ⚠️ SVF only | SVF playback |

### xc3sprog (Recommended)

[xc3sprog](https://xc3sprog.sourceforge.net/) can program XC9500 CPLDs directly with .jed files - no commercial programmer needed!

**Compatible Hardware:**

| Hardware | Cable Type | Notes |
|----------|------------|-------|
| **FT232H** | `ft232h` | Works great! See wiring below |
| FT2232H | `ft2232` | Dual-channel version |
| Raspberry Pi GPIO | `sysfsgpio` | [Direct GPIO wiring](https://anastas.io/hardware/2020/09/29/xc9500-cpld-raspberry-pi-xc3sprog.html) |
| Bus Pirate | `bp` | Slower but works |
| Digilent JTAG-HS2 | `jtaghs2` | Commercial option |

### Programming with FT232H

**Wiring (FT232H → XC95108):**

| FT232H Pin | JTAG Function | XC95108 |
|------------|---------------|---------|
| AD0 | TCK | TCK |
| AD1 | TDI | TDI |
| AD2 | TDO | TDO |
| AD3 | TMS | TMS |
| GND | GND | GND |
| 3.3V | VCCIO | VCCIO |

**xc3sprog Commands:**

```bash
# Install xc3sprog (Linux)
git clone https://github.com/matrix-io/xc3sprog
cd xc3sprog && mkdir build && cd build
cmake .. && make
sudo make install

# Detect device
xc3sprog -c ft232h -j

# Expected output:
# JTAG loc.: 0  IDCODE: 0x59604093  Desc: XC95108

# Program JEDEC file
xc3sprog -c ft232h -v design.jed

# Verify programming
xc3sprog -c ft232h -c design.jed
```

### Open-Source Synthesis (Work in Progress)

| Tool | Status | Link |
|------|--------|------|
| XC9500 Reverse Engineering | 🚧 WIP | [GitHub](https://github.com/anuejn/XC9500) |
| Yosys → XC9500 | 🚧 Early | Goal: Full open source flow |

The [XC9500 project](https://github.com/anuejn/XC9500) aims to create a fully open source synthesis flow from Yosys to JEDEC bitstream, but it's still early-stage (focused on XC9572XL first).

**Current practical flow:**
```
Verilog/VHDL → ISE 14.7 (free, closed) → .jed → xc3sprog (open source)
                                              ↑
                                     Use FT232H or Raspberry Pi
```

### JTAG Programmers (Commercial)

| Option | Price | Source |
|--------|-------|--------|
| Xilinx Platform Cable USB II | ~$250 | [AMD/Xilinx](https://www.xilinx.com/products/boards-and-kits/hw-usb-ii-g.html) |
| Platform Cable Clone (DLC10) | ~$15-30 | [eBay](https://www.ebay.com/itm/124443394214) |
| Waveshare Platform Cable | ~$25 | [Waveshare](https://www.waveshare.com/platform-cable-usb.htm) |

**Note:** Clones work identically to official cables for CPLD programming.

### ISE Installation Notes

ISE 14.7 is the last version supporting XC9500:
1. Download ISE WebPACK 14.7 from Xilinx archive
2. Install on Windows 7/10 or Linux
3. Get free WebPACK license
4. Use iMPACT or xc3sprog for programming

## Common Uses

- Glue logic
- Address decoding
- Interface bridging
- State machines
- Prototyping before FPGA
- Legacy system maintenance

## XC9500 vs XC9500XL vs XC9500XV

| Feature | XC9500 | XC9500XL | XC9500XV |
|---------|--------|----------|----------|
| Voltage | 5V | 3.3V | 2.5V |
| Speed | 5-15ns | 5-15ns | 4-10ns |
| Power | Higher | Lower | Lowest |
| ISP | Yes | Yes | Yes |

## Notes

- **5V device** - XC9500XL (3.3V) more common now
- **Legacy** - Newer designs use XC2C (CoolRunner) or FPGAs
- **ISE required** - Vivado doesn't support XC9500
- **ISP capable** - Program in-circuit via JTAG
- **Deterministic timing** - All paths have same delay
- **Non-volatile** - Retains configuration without power

## Alternatives

For new designs:
- **Xilinx XC2C** (CoolRunner-II) - Lower power, 1.8V core
- **Lattice MachXO** - Modern CPLD/FPGA hybrid
- **Intel MAX II/V/10** - Modern CPLDs
- **Microchip ATF15xx** - 5V compatible

## Local Files

### Documentation
- `XC9500_Datasheet.pdf` - Family datasheet
- `XC95108_Pinout.pdf` - Package pinouts
