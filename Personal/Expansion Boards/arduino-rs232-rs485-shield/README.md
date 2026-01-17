# RS232/RS485 Shield

**Arduino Shield - Industrial Serial Communication**

## Board Information

| Field | Value |
|-------|-------|
| Manufacturer | Various |
| Board | RS232/RS485 Shield v1r1 |
| Platform | Arduino |
| Form Factor | Shield |
| Primary Function | UART to RS232/RS485 conversion |
| Main ICs | MAX232 (RS232), MAX485 (RS485) |
| Quantity | 1 |

## Compatibility

| Compatible With | Notes |
|-----------------|-------|
| Arduino UNO | Primary target |
| Arduino Mega | Compatible |
| Arduino Leonardo | Via software serial |

## Specifications

| Specification | Value |
|--------------|-------|
| RS232 Chip | MAX232 or equivalent |
| RS485 Chip | MAX485 or equivalent |
| RS232 Connector | DB9 Female |
| RS485 Connector | Screw terminal |
| RS232 Max Distance | ~50 feet (15m) |
| RS485 Max Distance | ~4000 feet (1200m) |
| RS485 Max Speed | 35 Mbps (cable dependent) |
| Serial Mode | Hardware UART or Software Serial |

## Pin Mapping

| Shield Function | Arduino Pin | Notes |
|-----------------|-------------|-------|
| TX | D1 (UART) or D3 (Soft) | Switch selectable |
| RX | D0 (UART) or D2 (Soft) | Switch selectable |
| RS485 DE/RE | D2 or other | Direction control (half-duplex) |

### Mode Switch Settings

| Switch | Position | Function |
|--------|----------|----------|
| UART/Soft | UART | Use hardware serial (D0/D1) |
| UART/Soft | Soft | Use software serial (D2/D3) |
| RS232/RS485 | RS232 | Route to DB9 connector |
| RS232/RS485 | RS485 | Route to screw terminal |

### Pins Used

- **Power:** 5V, GND
- **Serial:** D0/D1 (UART) or D2/D3 (Software Serial)
- **RS485 Direction:** Typically D2 (when using UART)

### Stacking Compatibility

- [x] Passes through unused pins
- [x] Can stack with: Non-serial shields
- [x] Conflicts with: Shields using serial pins

## Features

- Dual RS232 and RS485 interfaces
- DB9 connector for RS232 devices
- Screw terminal for RS485 bus
- Switch for UART/Software Serial selection
- Switch for RS232/RS485 selection
- Level shifting for proper voltage levels
- Prototyping area for custom circuits
- ESD protection (varies by manufacturer)

## RS232 vs RS485 Comparison

| Feature | RS232 | RS485 |
|---------|-------|-------|
| Topology | Point-to-point | Multi-drop bus |
| Max Devices | 2 | 32 (standard) |
| Max Distance | 15m | 1200m |
| Duplex | Full | Half (2-wire) or Full (4-wire) |
| Voltage | ±3V to ±15V | Differential ±1.5V to ±6V |
| Noise Immunity | Low | High |
| Common Use | Legacy PC, modems | Industrial, SCADA |

## Documentation

### Board Documentation
- [TinyOS Shop Product](https://www.tinyosshop.com/arduino-rs232-rs485-shield)
- [RobotShop Product](https://www.robotshop.com/products/rs232-485-shield-arduino)

### IC Datasheets
- [MAX232 Datasheet](https://www.ti.com/lit/ds/symlink/max232.pdf)
- [MAX485 Datasheet](https://www.analog.com/media/en/technical-documentation/data-sheets/MAX1487-MAX491.pdf)

## Software & Libraries

No special library required for basic serial communication. Use standard `Serial` or `SoftwareSerial`.

### RS485 Direction Control

For half-duplex RS485, you must control the DE (Driver Enable) and RE (Receiver Enable) pins:

```cpp
#define RS485_DE_PIN 2  // Direction control pin

void rs485Write(byte data) {
  digitalWrite(RS485_DE_PIN, HIGH);  // Enable transmit
  Serial.write(data);
  Serial.flush();  // Wait for transmission
  digitalWrite(RS485_DE_PIN, LOW);   // Enable receive
}
```

## Example Code

### RS232 Communication

```cpp
// Using hardware serial (switch in UART position)
// Connect to RS232 device at 9600 baud

void setup() {
  Serial.begin(9600);
}

void loop() {
  if (Serial.available()) {
    char c = Serial.read();
    // Process received character
    Serial.write(c);  // Echo back
  }
}
```

### RS485 Half-Duplex Communication

```cpp
#define RS485_DE 2  // Direction enable pin

void setup() {
  Serial.begin(9600);
  pinMode(RS485_DE, OUTPUT);
  digitalWrite(RS485_DE, LOW);  // Start in receive mode
}

void rs485Send(String message) {
  digitalWrite(RS485_DE, HIGH);  // Transmit mode
  delay(1);
  Serial.print(message);
  Serial.flush();
  delay(1);
  digitalWrite(RS485_DE, LOW);   // Receive mode
}

void loop() {
  // Send message every 2 seconds
  rs485Send("Hello RS485 Bus\n");
  delay(2000);

  // Check for incoming data
  while (Serial.available()) {
    char c = Serial.read();
    // Process received data
  }
}
```

## Notes

- Remove shield or switch to Soft Serial mode when uploading sketches
- RS485 requires proper termination resistors for long cables (120 ohm)
- RS485 is half-duplex with 2-wire connection; full-duplex requires 4 wires
- Common in industrial automation, PLC communication, Modbus
- Baud rate typically limited by cable length and quality
- Some shields have automatic direction control for RS485

## Local Files

- `MAX232_Datasheet.pdf` - RS232 level shifter datasheet (1.7 MB)

### Pending (Manual Download Required)
- `MAX485_Datasheet.pdf` - see [MISSING_DOCUMENTATION.md](../MISSING_DOCUMENTATION.md)
