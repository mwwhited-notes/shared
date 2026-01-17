# Netduino Mini

**.NET Micro Framework Development Board**

## Board Information

| Field | Value |
|-------|-------|
| Manufacturer | Secret Labs |
| Board | Netduino Mini |
| MCU | Atmel AT91SAM7X512 |
| Date Acquired | |
| Quantity | |

## Specifications

| Specification | Value |
|--------------|-------|
| Core | ARM7TDMI |
| Clock Speed | 48 MHz |
| Flash | 512 KB |
| SRAM | 128 KB |
| Operating Voltage | 3.3V |
| Input Voltage | 5-9V (onboard regulator) |
| GPIO | 16 |
| ADC | 4 channels (10-bit) |

## Peripherals

| Peripheral | Quantity |
|-----------|----------|
| UART | 2 |
| SPI | 1 |
| I2C | 1 (software) |
| PWM | 4 channels |

## Board Features

- 24-pin DIP form factor
- Fits standard DIP socket or breadboard
- USB mini-B connector
- Power LED
- User LED
- Power via USB or external 5-9V

## Pinout

| Pin | Function |
|-----|----------|
| 1 | GND |
| 2 | GPIO 0 (RX2) |
| 3 | GPIO 1 (TX2) |
| 4 | GPIO 2 (INT1) |
| 5 | GPIO 3 |
| 6 | GPIO 4 (ADC0) |
| 7 | GPIO 5 (ADC1) |
| 8 | GPIO 6 (ADC2) |
| 9 | GPIO 7 (ADC3) |
| 10 | GPIO 8 (PWM0) |
| 11 | GPIO 9 (PWM1) |
| 12 | 3.3V OUT |
| 13 | 5V IN |
| 14 | GPIO 10 (PWM2) |
| 15 | GPIO 11 (PWM3) |
| 16 | GPIO 12 (SPI CLK) |
| 17 | GPIO 13 (SPI MOSI) |
| 18 | GPIO 14 (SPI MISO) |
| 19 | GPIO 15 (SPI CS) |
| 20 | GPIO 16 (RX1) |
| 21 | GPIO 17 (TX1) |
| 22 | GPIO 18 |
| 23 | GPIO 19 |
| 24 | GND |

## Programming

| Method | Tools |
|--------|-------|
| USB | Visual Studio + MFDeploy |
| Serial | MFDeploy |

## .NET Micro Framework

The Netduino Mini runs .NET Micro Framework, allowing C# development:

- Managed code execution
- Garbage collection
- Object-oriented programming
- Visual Studio integration
- Debugging over USB

## Documentation

- [Netduino Mini Product Page](http://www.introtoarduino.com/net/Netduino-Mini.html)
- [.NET Micro Framework](https://netmf.github.io/)
- [AT91SAM7X512 Datasheet](https://ww1.microchip.com/downloads/en/DeviceDoc/doc6175.pdf)

## Software & Tools

- **Visual Studio** - Primary IDE (2010-2015 era)
- **MFDeploy** - Deployment utility
- **.NET Micro Framework SDK** - Version 4.2 or 4.3
- [Netduino SDK](https://github.com/Netduino)

### Development Setup

1. Install Visual Studio (2012/2013 recommended)
2. Install .NET Micro Framework SDK 4.3
3. Install Netduino SDK
4. Connect via USB
5. Deploy using MFDeploy or Visual Studio

## Code Example

```csharp
using Microsoft.SPOT;
using Microsoft.SPOT.Hardware;
using SecretLabs.NETMF.Hardware.NetduinoMini;

public class Program
{
    public static void Main()
    {
        OutputPort led = new OutputPort(Pins.ONBOARD_LED, false);

        while (true)
        {
            led.Write(true);
            Thread.Sleep(500);
            led.Write(false);
            Thread.Sleep(500);
        }
    }
}
```

## Notes

- **Legacy platform** - .NET Micro Framework is largely discontinued
- Consider migration to nanoFramework for similar experience
- Unique DIP form factor for embedded integration
- C# development experience (unusual for microcontrollers)
- Limited community support compared to Arduino/ESP
- Visual Studio 2015 or earlier required for original SDK

## Alternatives

For modern .NET embedded development:
- **nanoFramework** - Spiritual successor to NETMF
- **Wilderness Labs Meadow** - .NET for embedded
- **ESP32 + nanoFramework** - Modern hardware with .NET

## Local Files

*Documentation to be downloaded*
