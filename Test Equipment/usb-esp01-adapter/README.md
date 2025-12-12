# USB to ESP-01 Adapter

**ESP8266 Programming and Serial Adapter**

## Unit Information

| Field | Value |
|-------|-------|
| Manufacturer | Generic |
| Model | USB to ESP-01 Adapter |
| Modifications | Reset button added |
| Condition | Working |

## Specifications

| Specification | Value |
|--------------|-------|
| Target Module | ESP-01 (ESP8266) |
| Interface | USB to Serial (likely CH340G or CP2102) |
| Voltage Regulator | 3.3V onboard |
| Programming Mode | Via UART/PROG switch |

## Features

- USB to 3.3V serial converter
- Built-in 3.3V regulator (powers ESP-01 directly)
- UART/PROG mode switch
- **User-added reset button**

## ESP-01 Socket Pinout

```
        ┌─────────────┐
   GND  │ 1         2 │  GPIO2
        │             │
  GPIO0 │ 3         4 │  RX
        │             │
        │   [ESP-01]  │
        │             │
   VCC  │ 5         6 │  TX
        │             │
  RESET │ 7         8 │  CH_PD
        └─────────────┘
```

## Mode Selection

| Mode | GPIO0 | Switch Position | Purpose |
|------|-------|-----------------|---------|
| Normal/Run | HIGH (floating) | UART | Normal operation |
| Flash/Program | LOW (GND) | PROG | Upload firmware |

## Programming Procedure

1. Set switch to **PROG** position
2. Insert ESP-01 module
3. Connect USB to computer
4. Press **reset button** (or power cycle)
5. Upload firmware via Arduino IDE or esptool
6. After upload, set switch back to **UART**
7. Press reset to run new firmware

## Documentation

- [ESP8266 Datasheet](https://www.espressif.com/sites/default/files/documentation/0a-esp8266ex_datasheet_en.pdf)
- [ESP8266 Technical Reference](https://www.espressif.com/sites/default/files/documentation/esp8266-technical_reference_en.pdf)
- [ESP-01 Module Pinout](https://randomnerdtutorials.com/esp8266-pinout-reference-gpios/)

## Software

### Arduino IDE Setup
1. File → Preferences → Additional Board Manager URLs:
   ```
   http://arduino.esp8266.com/stable/package_esp8266com_index.json
   ```
2. Tools → Board → Board Manager → Search "ESP8266" → Install
3. Tools → Board → ESP8266 Boards → "Generic ESP8266 Module"

### Arduino IDE Settings for ESP-01

| Setting | Value |
|---------|-------|
| Board | Generic ESP8266 Module |
| Flash Size | 1MB (FS:64KB OTA:~470KB) or 512KB |
| Upload Speed | 115200 |
| Reset Method | no dtr (aka ck) |
| Flash Mode | DOUT |

### esptool.py

```bash
# Install esptool
pip install esptool

# Erase flash
esptool.py --port COM3 erase_flash

# Flash firmware
esptool.py --port COM3 --baud 115200 write_flash 0x00000 firmware.bin

# Read flash
esptool.py --port COM3 read_flash 0x00000 0x100000 flash_dump.bin
```

## Troubleshooting

| Problem | Solution |
|---------|----------|
| "Failed to connect" | Ensure PROG mode, press reset, check wiring |
| Upload timeout | Try lower baud rate (9600), press reset during upload |
| Module not detected | Check CH340/CP2102 driver installed |
| Brownout/unstable | USB may not supply enough current, use powered hub |
| Wrong COM port | Check Device Manager for correct port |

## Serial Monitor Usage

After programming, switch to UART mode for serial debugging:

1. Set switch to **UART**
2. Press reset button
3. Open Serial Monitor at **115200 baud** (or your configured rate)
4. Boot messages and Serial.print() output will appear

## Notes

- Board has "USB to ESP-01 Adapter" markings
- UART/PROG switch selects GPIO0 state at boot
- User-added reset button for convenience (eliminates need to unplug/replug)
- Some adapters have CH340G, others have CP2102 - install appropriate driver

## Driver Downloads

- [CH340 Driver](http://www.wch-ic.com/downloads/CH341SER_ZIP.html)
- [CP2102 Driver (Silicon Labs)](https://www.silabs.com/developers/usb-to-uart-bridge-vcp-drivers)

## Local Files

*No official documentation for this generic adapter - see ESP8266 docs above.*
