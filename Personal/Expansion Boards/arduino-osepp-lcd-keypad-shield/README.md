# OSEPP LCD Keypad Shield V1.0

**Arduino Shield - 16x2 LCD with Navigation Buttons**

## Board Information

| Field | Value |
|-------|-------|
| Manufacturer | OSEPP |
| Board | LCD Keypad Shield V1.0 |
| Platform | Arduino |
| Form Factor | Shield |
| Primary Function | Display and user input |
| Main IC | HD44780 compatible LCD controller |
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
| Display Type | 16x2 character LCD |
| Display Controller | HD44780 compatible |
| Backlight | Blue with white text (typical) |
| Buttons | 5 (Select, Up, Down, Left, Right) |
| Button Interface | Single analog pin (resistor ladder) |
| Contrast | Adjustable via potentiometer |
| Interface | 4-bit parallel |

## Pin Mapping

| Shield Function | Arduino Pin | Notes |
|-----------------|-------------|-------|
| LCD RS | D8 | Register Select |
| LCD Enable | D9 | Enable |
| LCD D4 | D4 | Data bit 4 |
| LCD D5 | D5 | Data bit 5 |
| LCD D6 | D6 | Data bit 6 |
| LCD D7 | D7 | Data bit 7 |
| Backlight | D10 | PWM for brightness control |
| Buttons | A0 | Analog read (resistor ladder) |

### Button Analog Values

Each button connects to A0 through different resistors:

| Button | Typical ADC Value | Range |
|--------|-------------------|-------|
| Right | 0 | 0-50 |
| Up | 100 | 50-150 |
| Down | 255 | 150-300 |
| Left | 410 | 300-500 |
| Select | 640 | 500-750 |
| None | 1023 | >750 |

*Values may vary slightly between boards - calibrate for your specific shield*

### Pins Used

- **LCD:** D4, D5, D6, D7 (data), D8 (RS), D9 (Enable)
- **Backlight:** D10 (PWM)
- **Buttons:** A0 (analog)

### Stacking Compatibility

- [x] Passes through unused pins
- [x] Can stack with: I2C shields, A1-A5 analog shields
- [x] Conflicts with: Shields using D4-D10 or A0

## Features

- 16x2 character LCD display
- Blue backlight with white characters
- 5 navigation buttons (resistor ladder)
- Adjustable contrast potentiometer
- PWM backlight control
- Standard LiquidCrystal library compatible
- Reset button accessible

## Documentation

### Reference Documentation
- [OSEPP Product Page](https://osepp.com/electronic-modules/shields/45-16x2-lcd-display-keypad-shield)
- [HD44780 Controller Reference](https://www.sparkfun.com/datasheets/LCD/HD44780.pdf)

## Software & Libraries

### LiquidCrystal Library (Built-in)
```cpp
#include <LiquidCrystal.h>
```

No additional library needed - uses built-in Arduino library.

## Example Code

### Basic LCD Display

```cpp
#include <LiquidCrystal.h>

// Initialize LCD: RS, E, D4, D5, D6, D7
LiquidCrystal lcd(8, 9, 4, 5, 6, 7);

void setup() {
  lcd.begin(16, 2);          // 16 columns, 2 rows
  lcd.print("Hello World!");
  lcd.setCursor(0, 1);       // Column 0, Row 1
  lcd.print("OSEPP Shield");
}

void loop() {
  // Nothing here
}
```

### Reading Buttons

```cpp
#include <LiquidCrystal.h>

LiquidCrystal lcd(8, 9, 4, 5, 6, 7);

#define BTN_RIGHT  0
#define BTN_UP     1
#define BTN_DOWN   2
#define BTN_LEFT   3
#define BTN_SELECT 4
#define BTN_NONE   5

int readButton() {
  int adc = analogRead(A0);

  if (adc < 50)   return BTN_RIGHT;
  if (adc < 150)  return BTN_UP;
  if (adc < 300)  return BTN_DOWN;
  if (adc < 500)  return BTN_LEFT;
  if (adc < 750)  return BTN_SELECT;
  return BTN_NONE;
}

void setup() {
  lcd.begin(16, 2);
  lcd.print("Press a button");
}

void loop() {
  lcd.setCursor(0, 1);

  switch (readButton()) {
    case BTN_RIGHT:  lcd.print("RIGHT "); break;
    case BTN_UP:     lcd.print("UP    "); break;
    case BTN_DOWN:   lcd.print("DOWN  "); break;
    case BTN_LEFT:   lcd.print("LEFT  "); break;
    case BTN_SELECT: lcd.print("SELECT"); break;
    case BTN_NONE:   lcd.print("      "); break;
  }

  delay(100);
}
```

### Menu System Example

```cpp
#include <LiquidCrystal.h>

LiquidCrystal lcd(8, 9, 4, 5, 6, 7);

const char* menuItems[] = {"Option 1", "Option 2", "Option 3", "Option 4"};
int menuIndex = 0;
int numItems = 4;

int readButton() {
  int adc = analogRead(A0);
  if (adc < 50)  return 0;  // RIGHT
  if (adc < 150) return 1;  // UP
  if (adc < 300) return 2;  // DOWN
  if (adc < 500) return 3;  // LEFT
  if (adc < 750) return 4;  // SELECT
  return -1;  // NONE
}

void displayMenu() {
  lcd.clear();
  lcd.print("> ");
  lcd.print(menuItems[menuIndex]);
  lcd.setCursor(0, 1);
  if (menuIndex + 1 < numItems) {
    lcd.print("  ");
    lcd.print(menuItems[menuIndex + 1]);
  }
}

void setup() {
  lcd.begin(16, 2);
  displayMenu();
}

void loop() {
  int btn = readButton();

  if (btn == 1) {  // UP
    if (menuIndex > 0) {
      menuIndex--;
      displayMenu();
    }
    delay(200);
  }

  if (btn == 2) {  // DOWN
    if (menuIndex < numItems - 1) {
      menuIndex++;
      displayMenu();
    }
    delay(200);
  }

  if (btn == 4) {  // SELECT
    lcd.clear();
    lcd.print("Selected:");
    lcd.setCursor(0, 1);
    lcd.print(menuItems[menuIndex]);
    delay(1000);
    displayMenu();
  }
}
```

### Backlight Control

```cpp
#include <LiquidCrystal.h>

LiquidCrystal lcd(8, 9, 4, 5, 6, 7);

#define BACKLIGHT_PIN 10

void setup() {
  pinMode(BACKLIGHT_PIN, OUTPUT);
  lcd.begin(16, 2);
  lcd.print("Backlight Test");
}

void loop() {
  // Fade backlight up
  for (int i = 0; i <= 255; i++) {
    analogWrite(BACKLIGHT_PIN, i);
    delay(10);
  }

  // Fade backlight down
  for (int i = 255; i >= 0; i--) {
    analogWrite(BACKLIGHT_PIN, i);
    delay(10);
  }
}
```

## Notes

- Adjust contrast potentiometer if display appears blank
- Button ADC values vary - calibrate readButton() thresholds
- Uses 4-bit mode to minimize pin usage
- Backlight draws significant current - use PWM to reduce power
- Great for standalone Arduino projects needing user interface
- Compatible with other "LCD Keypad Shield" variants (DFRobot, SainSmart)

## Local Files

- `HD44780_Datasheet.pdf` - LCD controller datasheet (323 KB)
