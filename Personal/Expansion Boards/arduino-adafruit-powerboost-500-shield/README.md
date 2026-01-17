# Adafruit PowerBoost 500 Shield

**Arduino Shield - Rechargeable 5V Power Supply**

## Board Information

| Field | Value |
|-------|-------|
| Manufacturer | Adafruit Industries |
| Board | PowerBoost 500 Shield |
| Product ID | 2078 |
| Platform | Arduino (Uno/Mega/Leonardo/Due) |
| Form Factor | Arduino Shield (stackable) |
| Primary Function | Rechargeable battery power supply with boost converter and charger |
| Date Acquired | 2026-01 |
| Quantity | 1 |
| Price | $19.95 |

## Compatibility

| Compatible With | Notes |
|-----------------|-------|
| Arduino Uno | Full compatibility |
| Arduino Mega | Full compatibility |
| Arduino Leonardo | Full compatibility |
| Arduino Due | Full compatibility |
| Arduino Duemilanove | Full compatibility |

**Note:** Compatible with any Arduino-pinout-shaped Arduino as only the GND and 5V pins are used.

## Specifications

| Specification | Value |
|--------------|-------|
| Input Voltage | 3.7V LiPo/LiIon battery (3.7/4.2V nominal) |
| Output Voltage | 5.2V (5.0V after protection diode) |
| Output Current (Sustained) | 500mA minimum |
| Output Current (Peak) | 1A |
| Charge Input | MicroUSB 5V |
| Charge Current | Up to 500mA (battery dependent) |
| Protection | 500mA fuse on boost output |
| Dimensions | 53mm x 69mm x 2mm (2.1" x 2.7" x 0.08") |
| Requires Assembly | Yes (soldering required) |

## Pin Mapping

### Power Connection

| Shield Pin | Arduino Pin | Function | Notes |
|-----------|-------------|----------|-------|
| 5V | 5V | Power output | Connected through Schottky diode |
| GND | GND | Ground | Common ground |

### Pin Passthrough

- **Digital Pins (D0-D13):** Passed through via stacking headers
- **Analog Pins (A0-A5):** Passed through via stacking headers
- **ICSP Header:** NOT passed through (battery occupies space)

### Stacking Compatibility

- [x] Passes through digital and analog pins
- [x] Stackable with other shields
- [ ] Does NOT pass through ICSP header
- [x] Can be used with multiple stacked shields

## Features

- Rechargeable LiPo/LiIon battery power for Arduino
- Built-in boost converter (3.7V → 5V)
- Built-in battery charger circuit
- MicroUSB charging port
- Status LEDs:
  - Charging indicator
  - Battery status/power indicator
- Protection fuse (500mA continuous, trips >1A)
- Schottky diode for voltage protection
- Optional power switch (requires soldering)
- Slim form factor fits 1200mAh battery

## Kit Contents

- PowerBoost 500 Shield PCB
- Stacking headers (requires soldering)
- Optional: Power switch component

**Not Included:**
- Arduino board
- LiPo/LiIon battery (sold separately)
- Battery must have protection circuitry

## Recommended Battery

- **Type:** Lithium Ion Polymer Battery
- **Voltage:** 3.7V nominal (4.2V max)
- **Capacity:** 1200mAh (Adafruit PID 258) - fits within shield dimensions
- **Connector:** JST 2-pin connector
- **Protection:** Must have built-in protection circuitry

## Assembly

### Required Tools
- Soldering iron
- Solder
- Flush cutters (for trimming header pins)

### Assembly Steps

1. Solder stacking headers to shield PCB
2. (Optional) Solder power switch if desired
3. Connect LiPo battery to JST connector
4. Mount battery using included adhesive or mounting method
5. Stack shield onto Arduino
6. Connect microUSB to charge battery

**Note:** Shield comes as a kit requiring soldering. Estimated assembly time: 15-30 minutes.

## Usage Notes

### Recommended Applications
- Portable Arduino projects
- Low-power sensors and data loggers
- Wearable electronics
- Battery-powered IoT devices
- Projects requiring mobility

### NOT Recommended For
- **Motor control** - Stall current can trip fuse
- **Robotics** - Current spikes from motors problematic
- **High-current applications** - 500mA sustained limit
- **Servo-heavy projects** - Multiple servos may exceed current limit

### Power Considerations

- **Voltage Drop:** Output can dip to 4.8V when drawing >1A
- **Fuse Protection:** Fuse trips at sustained >1A draw
- **Battery Life:** Depends on current draw and battery capacity
  - 1200mAh battery @ 100mA draw ≈ 12 hours
  - 1200mAh battery @ 500mA draw ≈ 2.4 hours

## Charging

- **Charge Port:** MicroUSB jack only
- **Charge Current:** Up to 500mA (varies by battery state)
- **Charge Time:** ~2-3 hours for 1200mAh battery (from empty)
- **Charging LED:** Indicates charging status
- **Can operate while charging:** Yes

## Documentation

### Board Documentation
- [Product Page](https://www.adafruit.com/product/2078)
- [Adafruit Learning Guide](https://learn.adafruit.com/adafruit-powerboost-500-shield-rechargeable-battery-pack)
- [Pinout Documentation](https://learn.adafruit.com/adafruit-powerboost-500-shield-rechargeable-battery-pack/pinouts)

### Downloads
- [PDF Guide](https://cdn-learn.adafruit.com/downloads/pdf/adafruit-powerboost-500-shield-rechargeable-battery-pack.pdf)

## Software & Libraries

No specific libraries required - this is a hardware power supply shield. Works transparently with any Arduino sketch.

## Example Use Cases

### Low-Power Data Logger
```cpp
// PowerBoost provides clean 5V power
// Arduino runs normally from shield
// Battery provides portable power
void setup() {
  Serial.begin(9600);
  // Normal Arduino code
}
```

### Battery Monitor Sketch
```cpp
// Read battery voltage via analog pin
// (Requires voltage divider circuit)
void loop() {
  int battLevel = analogRead(A0);
  // Process battery level
}
```

## Troubleshooting

| Issue | Solution |
|-------|----------|
| Won't charge | Check USB cable, verify battery connection |
| Fuse tripping | Reduce current draw, check for shorts |
| Low voltage | Battery may be depleted, charge via USB |
| Won't power Arduino | Check battery is charged, verify connections |

## Notes

- **Product Status:** No longer stocked by Adafruit (as of last check)
- **ICSP Limitation:** Battery physically blocks ICSP header access
- **Battery Requirement:** Must use battery with protection circuitry
- **Fuse Rating:** 500mA continuous, trips at >1A sustained
- Designed for low-to-moderate power Arduino projects
- Not suitable for high-current or motor-driven applications

### User Experience Notes

**Limitations Encountered:**
- **Insufficient Power:** 500mA output limit too restrictive for many projects
- **Non-Replaceable Fuse:** Fuse is not replaceable or resettable - permanent failure if tripped
- **Recommendation:** Consider PowerBoost 1000C for higher current applications (1A sustained, 2A peak) with better fuse accessibility

## Safety Warnings

- Use only batteries with protection circuitry
- Do not short circuit battery connections
- Monitor battery temperature during charging
- Dispose of damaged batteries properly
- Do not exceed 1A continuous current draw

## Local Files

Documentation to be downloaded from Adafruit Learning System.
