# FT232H Breakout Board

**USB to Multi-Protocol Interface (GPIO/SPI/I2C/JTAG/UART)**

## Unit Information

| Field | Value |
|-------|-------|
| Manufacturer | Generic (sold as "TXS0108E 8-channel logger") |
| Model | FT232H Breakout |
| Chip | FTDI FT232H (appears genuine) |
| PCB Color | Purple |
| Condition | Working |

## Specifications

| Specification | Value |
|--------------|-------|
| Interface Chip | FTDI FT232H |
| USB | USB 2.0 High Speed (480 Mbps) |
| I/O Voltage | 3.3V (5V tolerant inputs) |
| GPIO | Up to 16 pins |
| Clock Output | 6 MHz max (MPSSE mode) |
| UART Speed | Up to 12 Mbaud |

## Supported Protocols

| Protocol | Max Speed | Notes |
|----------|-----------|-------|
| UART/Serial | 12 Mbaud | TX, RX, RTS, CTS |
| SPI Master | 30 MHz | Full duplex |
| I2C Master | 3.4 MHz | With clock stretching |
| JTAG | 30 MHz | 4-wire |
| GPIO | N/A | 16 pins available |

## Connectors

| Connector | Pins | Purpose |
|-----------|------|---------|
| Header 1 | 1x10 | Primary I/O (AD0-AD7, etc.) |
| Header 2 | 1x10 | Secondary I/O (AC0-AC7, etc.) |
| Header 3 | 1x4 | Likely power/aux |
| USB | Type-B/Mini | Host connection |

## FT232H Pin Functions

### MPSSE Mode (SPI/I2C/JTAG)

| Pin | SPI Function | I2C Function | JTAG Function |
|-----|--------------|--------------|---------------|
| AD0 | SCK | SCL | TCK |
| AD1 | MOSI | SDA (out) | TDI |
| AD2 | MISO | SDA (in) | TDO |
| AD3 | CS | N/A | TMS |
| AD4-7 | GPIO | GPIO | GPIO |

### UART Mode

| Pin | Function |
|-----|----------|
| AD0 | TXD |
| AD1 | RXD |
| AD2 | RTS# |
| AD3 | CTS# |
| AD4 | DTR# |
| AD5 | DSR# |
| AD6 | DCD# |
| AD7 | RI# |

## Documentation

- [FT232H Datasheet (FTDI)](https://ftdichip.com/wp-content/uploads/2020/07/DS_FT232H.pdf)
- [MPSSE Command Reference (AN 108)](https://ftdichip.com/wp-content/uploads/2020/08/AN_108_Command_Processor_for_MPSSE_and_MCU_Host_Bus_Emulation_Modes.pdf)
- [FT232H as I2C Master (AN 255)](https://ftdichip.com/wp-content/uploads/2020/08/AN_255_USB-to-I2C-Example-Using-FT232H.pdf)
- [FT232H as SPI Master (AN 114)](https://ftdichip.com/wp-content/uploads/2020/08/AN_114_FTDI_Hi_Speed_USB_To_SPI_Example.pdf)

## Software

### Libraries
- **pyftdi** (Python) - Pure Python FTDI library
  - `pip install pyftdi`
- **libftdi** (C) - Open source FTDI library
- **Adafruit Blinka** - CircuitPython on desktop via FT232H
  - `pip install adafruit-blinka`

### Tools
- **FT_PROG** (Windows) - FTDI EEPROM programmer
- **flashrom** - Can use FT232H for SPI flash programming

## Driver Setup

### Windows
- Install [FTDI D2XX drivers](https://ftdichip.com/drivers/d2xx-drivers/)
- Or use Zadig for libusb (required for pyftdi)

### Linux
```bash
# Install libftdi
sudo apt install libftdi1-dev

# Add udev rule for non-root access
echo 'SUBSYSTEM=="usb", ATTR{idVendor}=="0403", ATTR{idProduct}=="6014", MODE="0666"' | sudo tee /etc/udev/rules.d/99-ftdi.rules
sudo udevadm control --reload-rules
```

## Example: pyftdi SPI

```python
from pyftdi.spi import SpiController

spi = SpiController()
spi.configure('ftdi://ftdi:232h/1')
slave = spi.get_port(cs=0, freq=1E6, mode=0)

# Transfer data
response = slave.exchange([0x9F], 3)  # Read JEDEC ID
print(f"JEDEC ID: {response.hex()}")
```

## Example: pyftdi I2C

```python
from pyftdi.i2c import I2cController

i2c = I2cController()
i2c.configure('ftdi://ftdi:232h/1')
slave = i2c.get_port(0x50)  # EEPROM at address 0x50

# Read from device
data = slave.read(16)
```

## Example: pyftdi GPIO

```python
from pyftdi.gpio import GpioAsyncController

gpio = GpioAsyncController()
gpio.configure('ftdi://ftdi:232h/1', direction=0xFF)  # All outputs

gpio.write(0x01)  # Set AD0 high
gpio.write(0x00)  # Set AD0 low
```

## Notes

- Sold as "TXS0108E 8-channel logger" but actually FT232H based
- Purple PCB with genuine FTDI FT232H chip
- Very versatile - can emulate many protocols
- The FT232H is a single-channel device (unlike FT2232H dual)

## Local Files

- `FT232H_Datasheet.pdf` - Device datasheet
- `AN_108_MPSSE_Commands.pdf` - MPSSE programming reference
