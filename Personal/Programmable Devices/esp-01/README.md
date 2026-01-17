# ESP-01

**Minimal WiFi Module**

## Board Information

| Field | Value |
|-------|-------|
| Manufacturer | AI-Thinker / Various |
| Module | ESP-01 |
| SoC | ESP8266EX |
| Date Acquired | |
| Quantity | |

## Specifications

| Specification | Value |
|--------------|-------|
| Processor | Tensilica L106 32-bit |
| Clock Speed | 80 MHz (160 MHz boost) |
| Flash | 1 MB (blue) / 512KB (black) |
| RAM | 80 KB user available |
| WiFi | 802.11 b/g/n (2.4 GHz) |
| GPIO | 4 (GPIO0, GPIO2, TX, RX) |
| Operating Voltage | 3.3V |
| Current Draw | Up to 300mA |

## Pinout (2x4 Header)

```
        ESP-01 (Top View)
      +----------------+
      |   [antenna]    |
      |                |
      | O  O  O  O  O  |  <- 2 LEDs
      |                |
      +----------------+
        | | | | | | | |
       GND            VCC
       GPIO2          RST
       GPIO0          CH_PD
       RXD            TXD

Pin 1 (GND)    Pin 2 (GPIO2)
Pin 3 (GPIO0)  Pin 4 (RXD)
Pin 5 (VCC)    Pin 6 (RST)
Pin 7 (CH_PD)  Pin 8 (TXD)
```

## Pin Functions

| Pin | Function | Notes |
|-----|----------|-------|
| VCC | 3.3V Power | NOT 5V tolerant! |
| GND | Ground | |
| TX | UART TX / GPIO1 | Serial output |
| RX | UART RX / GPIO3 | Serial input |
| GPIO0 | Boot mode / General | LOW = flash mode |
| GPIO2 | General | Must be HIGH at boot |
| RST | Reset | Active LOW |
| CH_PD/EN | Chip Enable | Must be HIGH |

## Boot Modes

| GPIO0 | GPIO2 | Mode |
|-------|-------|------|
| LOW | HIGH | Programming (Flash) |
| HIGH | HIGH | Normal Boot |

## Features

- Smallest ESP8266 form factor
- PCB antenna
- 2 LEDs (power, activity)
- AT firmware by default
- Can run Arduino/custom firmware

## Programming

| Method | Tools |
|--------|-------|
| USB-ESP01 Adapter | Dedicated adapter (easier) |
| USB-Serial | FTDI, CP2102 (3.3V) |

### Wiring for Programming

| USB-Serial | ESP-01 |
|------------|--------|
| 3.3V | VCC, CH_PD |
| GND | GND, GPIO0 (for flash mode) |
| TX | RX |
| RX | TX |

**To enter flash mode:** Hold GPIO0 LOW while powering on or resetting.

## Documentation

- [ESP8266EX Datasheet](https://www.espressif.com/sites/default/files/documentation/0a-esp8266ex_datasheet_en.pdf)
- [ESP-01 Pinout Guide](https://randomnerdtutorials.com/esp8266-pinout-reference-gpios/)
- [ESP8266 AT Commands](https://www.espressif.com/sites/default/files/documentation/4a-esp8266_at_instruction_set_en.pdf)

## Software & Tools

- **Arduino IDE** - Select "Generic ESP8266 Module"
- **esptool.py** - Command-line flashing
- [ESP8266 Arduino Core](http://arduino.esp8266.com/stable/package_esp8266com_index.json)

### Arduino IDE Settings

- Board: Generic ESP8266 Module
- Flash Size: 1MB (or 512KB for older black PCB)
- Flash Mode: DOUT
- Upload Speed: 115200

## Common Uses

- WiFi-to-Serial bridge
- IoT sensors
- Smart home projects
- WiFi relay modules
- Adding WiFi to Arduino

## USB-ESP01 Adapter Notes

Dedicated USB adapters make programming much easier:
- Built-in 3.3V regulator
- Auto-reset circuit
- Switch or jumper for flash mode
- Some have GPIO0 breakout

## Limitations

- Only 2 GPIO pins available (GPIO0, GPIO2)
- GPIO0/GPIO2 have boot requirements
- No ADC pin broken out
- 3.3V only - will be damaged by 5V
- Limited to 1MB (or 512KB) flash
- Requires external adapter for programming

## Notes

- **Blue PCB** = 1MB flash (most common now)
- **Black PCB** = 512KB flash (older)
- CH_PD must be HIGH for chip to operate
- GPIO2 has internal pull-up
- Popular for adding WiFi to existing projects
- Can use with Arduino via serial (AT commands)

## Local Files

*Documentation to be downloaded*
