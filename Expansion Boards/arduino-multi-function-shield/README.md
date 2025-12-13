# Arduino Multi-Function Shield

**Arduino Shield - Learning/Prototyping Platform**

## Board Information

| Field | Value |
|-------|-------|
| Manufacturer | Various (Generic) |
| Board | Multi-Function Shield |
| Marking | 3118AY-ZZ K68641BS (Mulie-Function Shidle) |
| Platform | Arduino |
| Form Factor | Shield |
| Primary Function | Learning and prototyping |
| Quantity | 1 |

## Compatibility

| Compatible With | Notes |
|-----------------|-------|
| Arduino UNO | Primary target |
| Arduino Duemilanove | Compatible |
| Arduino Leonardo | Compatible |
| Arduino Mega | Compatible |

## Specifications

| Specification | Value |
|--------------|-------|
| 7-Segment Display | 4-digit, common cathode |
| Display Driver | 2x 74HC595 (cascaded) |
| LEDs | 4 (accent LEDs D1-D4) |
| Push Buttons | 3 (active LOW) |
| Potentiometer | 10K trim pot |
| Buzzer | Active piezo (PNP driven) |
| Sensor Interface | DS18B20 (temp), IR receiver |
| Display Part | 3118AY (4-digit 7-segment) |

## Pin Mapping

| Component | Arduino Pin | Notes |
|-----------|-------------|-------|
| LED D1 | D13 | Active LOW |
| LED D2 | D12 | Active LOW |
| LED D3 | D11 | Active LOW |
| LED D4 | D10 | Active LOW |
| Button S1 | A1 | Active LOW, needs INPUT_PULLUP |
| Button S2 | A2 | Active LOW, needs INPUT_PULLUP |
| Button S3 | A3 | Active LOW, needs INPUT_PULLUP |
| Buzzer | D3 | Active LOW (PNP transistor) |
| Potentiometer | A0 | 0-1023 analog reading |
| 7-Seg Latch | D4 | 74HC595 RCLK |
| 7-Seg Clock | D7 | 74HC595 SRCLK |
| 7-Seg Data | D8 | 74HC595 SER |
| Temp Sensor | A4 | DS18B20 (not included) |
| IR Receiver | D2 | 38kHz IR (not included) |

### 7-Segment Display Shift Register

The display uses two cascaded 74HC595 shift registers:
- First 595: Digit select (which digit is active)
- Second 595: Segment data (which segments are lit)

### Pins Used

- **LEDs:** D10, D11, D12, D13
- **Buttons:** A1, A2, A3
- **Display:** D4, D7, D8
- **Buzzer:** D3
- **Analog:** A0 (pot), A4 (temp sensor)
- **IR:** D2

### Stacking Compatibility

- [ ] Passes through unused pins - Limited
- [ ] Can stack with: Very few shields
- [x] Conflicts with: Most shields (uses many pins)

## Features

- 4-digit 7-segment LED display
- 4 indicator LEDs
- 3 tactile push buttons
- 10K potentiometer for analog input
- Active buzzer with transistor driver
- DS18B20 temperature sensor header
- IR receiver module header
- Servo/sensor headers
- Great for learning Arduino

## Component Details

### 7-Segment Display (3118AY)
- 4-digit common cathode display
- Controlled via 74HC595 shift registers
- Multiplexed (one digit at a time)

### Buzzer Operation
- Connected through PNP transistor Q1
- **Active LOW**: `digitalWrite(3, LOW)` = buzzer ON
- Active buzzer (contains oscillator) - no tone() needed

### Button Wiring
- All buttons are active LOW
- Use `pinMode(pin, INPUT_PULLUP)` or external pull-up

## Documentation

### Guides and Tutorials
- [Hackatronics Guide (PDF)](https://www.mpja.com/download/hackatronics-arduino-multi-function-shield.pdf)
- [Arduino Learning Examples](https://www.arduinolearning.com/code/multi-function-shield-examples.php)
- [EDN Getting Started](https://www.edn.com/getting-started-with-the-arduino-multifunction-shield/)

## Software & Libraries

### MultiFuncShield Library
```
# Arduino Library Manager
Search for: "MultiFuncShield"
```

Or use direct shift register control for the display.

## Example Code

### Basic LED and Button

```cpp
// Pin definitions
#define LED1 13
#define LED2 12
#define LED3 11
#define LED4 10
#define BTN1 A1
#define BTN2 A2
#define BTN3 A3
#define BUZZER 3
#define POT A0

void setup() {
  pinMode(LED1, OUTPUT);
  pinMode(LED2, OUTPUT);
  pinMode(LED3, OUTPUT);
  pinMode(LED4, OUTPUT);
  pinMode(BUZZER, OUTPUT);

  pinMode(BTN1, INPUT_PULLUP);
  pinMode(BTN2, INPUT_PULLUP);
  pinMode(BTN3, INPUT_PULLUP);

  digitalWrite(BUZZER, HIGH);  // Buzzer off
}

void loop() {
  // LEDs are active LOW
  digitalWrite(LED1, !digitalRead(BTN1));
  digitalWrite(LED2, !digitalRead(BTN2));
  digitalWrite(LED3, !digitalRead(BTN3));

  // Read potentiometer
  int potValue = analogRead(POT);
  // Map to LED4 blink rate
  digitalWrite(LED4, LOW);
  delay(potValue);
  digitalWrite(LED4, HIGH);
  delay(potValue);
}
```

### 7-Segment Display

```cpp
#define LATCH 4
#define CLK 7
#define DATA 8

// Segment patterns for 0-9 (common cathode)
byte digits[] = {
  0x3F, 0x06, 0x5B, 0x4F, 0x66,
  0x6D, 0x7D, 0x07, 0x7F, 0x6F
};

// Digit select (active high, bits 0-3)
byte digitSelect[] = {0x01, 0x02, 0x04, 0x08};

void setup() {
  pinMode(LATCH, OUTPUT);
  pinMode(CLK, OUTPUT);
  pinMode(DATA, OUTPUT);
}

void displayDigit(int position, int value) {
  digitalWrite(LATCH, LOW);
  shiftOut(DATA, CLK, MSBFIRST, digits[value]);
  shiftOut(DATA, CLK, MSBFIRST, digitSelect[position]);
  digitalWrite(LATCH, HIGH);
}

void loop() {
  // Display "1234" by multiplexing
  for (int i = 0; i < 4; i++) {
    displayDigit(i, i + 1);
    delay(5);
  }
}
```

### Buzzer

```cpp
#define BUZZER 3

void setup() {
  pinMode(BUZZER, OUTPUT);
  digitalWrite(BUZZER, HIGH);  // Off
}

void beep(int duration) {
  digitalWrite(BUZZER, LOW);   // On (active LOW)
  delay(duration);
  digitalWrite(BUZZER, HIGH);  // Off
}

void loop() {
  beep(100);
  delay(1000);
}
```

## Notes

- The silkscreen misspelling "Mulie-Function Shidle" is common on clone boards
- Buzzer is LOUD - consider adding a resistor in series
- Display requires multiplexing - refresh frequently to avoid flicker
- LEDs are active LOW (write LOW to turn ON)
- Buttons are active LOW (read LOW when pressed)
- DS18B20 and IR modules not included - solder headers to use
- Great for beginners learning Arduino

## Local Files

*To be downloaded*

- `74HC595_Datasheet.pdf` - Shift register datasheet
