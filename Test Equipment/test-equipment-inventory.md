# Test Equipment Inventory

Personal electronics lab equipment reference with specifications, documentation links, and software resources.

---

## Oscilloscopes

### Rigol DS1102E
**Digital Storage Oscilloscope**

| Specification | Value |
|--------------|-------|
| Bandwidth | 100 MHz |
| Channels | 2 + external trigger |
| Sample Rate | 1 GSa/s real-time, 25 GSa/s equivalent |
| Memory | 1 Mpts |
| Resolution | 8-bit |
| Display | 5.6" 64K color TFT |

**Features:** Edge/pulse/video/slope/pattern triggers, FFT, pass/fail testing, waveform record/replay, 20 auto measurements, USB host/device

**Documentation:**
- [User Manual (PDF)](https://cdn-shop.adafruit.com/datasheets/Users+Guide+DS1000E.pdf)
- [Service Manual](https://www.manualslib.com/manual/1255425/Rigol-Ds1102e.html)
- [Quick Manual](https://www.manualslib.com/manual/1393636/Rigol-Ds1102e.html)
- [Datasheet](https://www.manualslib.com/manual/571238/Rigol-Ds1102e.html)

**Software:** UltraScope PC software for remote control and waveform capture

---

### Tektronix TDS2024 + TDS2CMA Module
**Digital Storage Oscilloscope with Communications Module**

| Specification | Value |
|--------------|-------|
| Bandwidth | 200 MHz |
| Channels | 4 analog |
| Sample Rate | 1 GSa/s (2ch), 500 MSa/s (3-4ch) |
| Memory | 2.5 kpts per channel |
| Resolution | 8-bit |
| Display | Color TFT LCD |

**TDS2CMA Module adds:** FFT math, GPIB, RS-232, Centronics parallel printer port

**Features:** Edge/video/pulse width triggers, 11 auto measurements, roll mode, average mode, dual timebase

**Documentation:**
- [User Manual (PDF)](https://neurophysics.ucsd.edu/Manuals/Tektronix/TDS%201000B%20and%20TDS%202000B%20Manual.pdf)
- [Service Manual (PDF)](https://download.tek.com/manual/071107602.pdf)
- [Programmer Manual](https://7id.xray.aps.anl.gov/internal/hardware/units/tektronix/TDS2024/)

**Software:** OpenChoice PC Communications Software, National Instruments SignalExpress

---

### Hitachi V-1150
**Analog Oscilloscope**

| Specification | Value |
|--------------|-------|
| Bandwidth | 150 MHz |
| Channels | 4 |
| Display | 6" CRT, internal graticule (8×10 div) |
| Max Input | 400 V DC + peak AC (at 1 kHz) |

**Features:** Dual timebase, delayed sweep, X-Y mode, quad mode with independent positioning, CMRR ≥20 dB at 20 MHz

**Documentation:**
- [Service Manual](https://www.opweb.de/english/company/Hitachi/downloads/Hitachi--V-1150--service--ID1913.pdf)
- [Operation Manual](https://elektrotanya.com/hitachi_v-1150_operation_manual.pdf/download.html)

---

### DSO201 (DSO Nano)
**Pocket Digital Oscilloscope**

| Specification | Value |
|--------------|-------|
| Bandwidth | 0-1 MHz (usable ~100 kHz) |
| Channels | 1 analog |
| Sample Rate | 1 MSa/s |
| Resolution | 12-bit |
| Memory | 4096 points |
| Display | 2.8" color TFT (320×240) |
| Max Input | 80 Vpp (×1 probe) |

**Features:** Auto/normal/single trigger, built-in square wave generator (10 Hz-1 MHz), MicroSD storage, rechargeable Li-ion, open-source hardware/software

**Documentation:**
- [User Manual (PDF)](https://files.seeedstudio.com/wiki/DSO_Nano_v3/res/DS201V_4.22%20User%20Manual.pdf)
- [DSO Nano Wiki](https://seeeddoc.github.io/DSO_Nano_v2/)

**Firmware:**
- [BenF Firmware](https://enterthegeekcave.wordpress.com/2014/09/24/pocket-oscilloscope-dso201/)
- [Firmware Mirror](https://www.siliconinvestigations.com/Dsonano/Dsonano.html)
- [GitHub - DS201 PRO Firmware](https://github.com/diimdeep/DS201_PRO)

---

## Signal Generators

### Rigol DG1022
**Function/Arbitrary Waveform Generator**

| Specification | Value |
|--------------|-------|
| Channels | 2 |
| Frequency Range | 100 mHz to 20 MHz (sine) |
| Sample Rate | 100 MSa/s |
| Resolution | 14-bit |
| Arbitrary Memory | 4 kpts |
| Output | 2 mVpp to 10 Vpp (high-Z) |

**Waveforms:** Sine, square, ramp, pulse, noise, 48 built-in arbitrary

**Modulation:** AM, FM, PM, FSK, sweep, burst

**Built-in Counter:** 100 mHz to 200 MHz

**Documentation:**
- [User Manual (PDF)](http://pmaweb.caltech.edu/~phy003/DG1022_UserGuide_EN.pdf)
- [Service Manual](https://www.manualslib.com/manual/1602456/Rigol-Dg1000-Series.html)
- [Programming Manual](https://www.manualslib.com/products/Rigol-Dg1022-3512487.html)

**Software:** Rigol UltraSigma for remote control

---

## Multimeters

### HP/Agilent/Keysight 34401A
**6½ Digit Benchtop Digital Multimeter**

| Specification | Value |
|--------------|-------|
| Resolution | 6½ digits |
| DC Voltage | 100 mV to 1000 V (0.0035% accuracy) |
| AC Voltage | 100 mV to 750 V (True RMS, 3 Hz-300 kHz) |
| DC Current | 10 µA to 3 A |
| Resistance | 100 Ω to 100 MΩ (2/4-wire) |
| Reading Rate | Up to 1000/s to GPIB |
| Interfaces | GPIB, RS-232 |

**Features:** Frequency/period measurement, diode test, continuity, min/max/avg, dB/dBm, limit testing, 512 reading memory

**Documentation:**
- [User's Guide (PDF)](http://instructor.physics.lsa.umich.edu/adv-labs/Tools_Resources/HP%2034401A%20user's%20guide.pdf)
- [Service Guide (PDF)](https://www.keysight.com/us/en/assets/9018-05613/service-manuals/9018-05613.pdf)
- [Service Manual (ManualsLib)](https://www.manualslib.com/manual/1306273/Keysight-34401a.html)

**Software:** Keysight BenchVue, IntuiLink

---

### Rigol DM3058E
**5½ Digit Benchtop Digital Multimeter**

| Specification | Value |
|--------------|-------|
| Resolution | 5½ digits (240,000 counts) |
| DC Voltage | 200 mV to 1000 V (0.015% accuracy) |
| AC Voltage | 200 mV to 750 V (True RMS) |
| DC/AC Current | 200 µA to 10 A |
| Resistance | 200 Ω to 100 MΩ (2/4-wire) |
| Capacitance | 2 nF to 10 mF |
| Frequency | 20 Hz to 1 MHz |
| Reading Rate | Up to 123/s |
| Interfaces | USB, RS-232 (no LAN/GPIB on E model) |

**Documentation:**
- [User Manual (PDF)](https://www.batronix.com/files/Rigol/Multimeter/DM3058/DM3058_UserGuide_EN.pdf)
- [Service Guide (PDF)](https://gotroot.ca/rigol/service%20manuals/DM3058_ServiceGuide_EN.pdf)
- [Programming Manual](https://www.manualslib.com/products/Rigol-Dm3058e-3634018.html)
- [Performance Verification Manual](https://www.manualslib.com/manual/1646371/Rigol-Dm3058.html)

**Software:** Rigol UltraDMM PC software

---

### Tenma 72-2055
**Handheld Digital Multimeter**

| Specification | Value |
|--------------|-------|
| Display | Digital LCD |
| Voltage Range | 0-600 V DC/AC |
| Functions | Voltage, current, resistance, capacitance, frequency, duty cycle, temperature |
| Power | 9V battery |

**Features:** Rubberized case, kickstand, large LCD display

---

## LCR Meters

### DER EE DE-5000
**Handheld LCR Meter**

| Specification | Value |
|--------------|-------|
| Display | 19,999/1,999 counts dual display |
| Test Frequencies | 100 Hz, 120 Hz, 1 kHz, 10 kHz, 100 kHz, DC |
| Inductance | 0.001 mH to 1000 H |
| Capacitance | 0.01 pF to 10 mF |
| Resistance | 0.001 Ω to 100 MΩ |
| Test Signal | 0.5 Vrms typical |

**Secondary Parameters:** D (dissipation), Q (quality), θ (phase), ESR, Rp

**Features:** 4-wire Kelvin measurement, component sorting, auto/manual range, open/short calibration

**Documentation:**
- [Instruction Manual (PDF)](http://benholmes.co.uk/files/DE-5000_manual_english.pdf)
- [User Manual (IET Labs)](https://www.ietlabs.com/pdf/Manuals/DE_5000_im.pdf)
- [Datasheet (PDF)](https://www.ietlabs.com/pdf/Datasheets/DE_5000.pdf)
- [ManualsLib](https://www.manualslib.com/manual/895462/Deree-De-5000.html)

**Accessories:** TL-21 alligator clips, TL-22 SMD tweezers, TL-23 guard lead, IR-USB interface (optional)

---

### Holdpeak HP-4070L
**Handheld LCR Meter**

| Specification | Value |
|--------------|-------|
| Display | 3½ digit (1999 counts) |
| Resistance | 20 Ω to 2000 MΩ (9 ranges) |
| Capacitance | 2000 pF to 200 µF (6 ranges) |
| Inductance | 20 mH to 20 H (4 ranges, 100 Hz test) |
| Dimensions | 143 × 75 × 32 mm |
| Power | 9V battery |

**Features:** Transistor hFE test, backlight, auto power-off, manual ranging

---

## Power Supplies

### Korad KA3005P
**Programmable DC Power Supply**

| Specification | Value |
|--------------|-------|
| Type | Linear regulated |
| Output | 0-30 V, 0-5 A, 150 W max |
| Display | Dual 4-digit LED |
| Resolution | 0.001 V / 0.001 A |
| Voltage Accuracy | ±0.5% + 20 mV |
| Current Accuracy | ±0.5% + 10 mA |
| Ripple | <2 mVrms voltage, <3 mArms current |
| Interfaces | USB, RS-232 |

**Features:** CV/CC modes, 4 programmable memory presets, OCP/OVP protection

**Documentation:**
- [User Manual (PDF)](https://static.eleshop.nl/mage/media/downloads/KA3005P_user_manual.pdf)
- [User Manual (Digikey)](https://mm.digikey.com/Volume0/opasdata/d220001/medias/docus/4151/KA3000_6000_Series_Man.pdf)
- [Programming Reference](https://www.sra-shops.com/pub/media/docs/srasolder/instructions/kd3005p-user-manual.pdf)

**Software:** KORAD PC software, compatible with sigrok

**SCPI Commands:** `*IDN?`, `VSET1:`, `ISET1:`, `VOUT1?`, `IOUT1?`, `OUT1`, `STATUS?`, `RCL1-4`, `SAV1-4`

---

### QE-MS305D (QW-MS305D)
**Adjustable DC Power Supply**

| Specification | Value |
|--------------|-------|
| Type | Linear regulated |
| Output | 0-30 V, 0-5 A |
| Display | 3-digit LED |
| Load Regulation | CV ≤0.1% + 5 mV, CC ≤0.1% + 10 mA |
| Ripple | CV ≤10 mVrms, CC ≤20 mArms |
| Input | 110 V AC |

**Features:** 4 potentiometers (coarse/fine voltage and current), CV/CC auto-switching

---

## Logic Analyzers

### Saleae Logic (Original 8-Channel)
**USB Logic Analyzer**

| Specification | Value |
|--------------|-------|
| Channels | 8 digital only (no analog) |
| Sample Rate | 24 MSa/s max (reduced channels), 12 MSa/s (all 8) |
| Bandwidth | ~3-6 MHz usable |
| Input Voltage | 0 to 5 V (5V tolerant) |
| Threshold | Fixed ~1.4 V (TTL-level) |
| Interface | USB 2.0 |
| Memory | PC-based (stream to disk) |

**Protocol Decoders:** SPI, I2C, UART, 1-Wire, CAN, and many more via software

**Documentation:**
- [User Guide (PDF)](https://www.batronix.com/files/Saleae/Saleae+Users+Guide.pdf)
- [User Manual (ManualsLib)](https://www.manualslib.com/manual/1414020/Saleae-Logic.html)
- [Support Documentation](https://support.saleae.com/)

**Software:**
- [Logic 2 Download](https://saleae.com/downloads) (Windows/Mac/Linux)
- Alternative: [PulseView/sigrok](http://sigrok.org/wiki/Downloads)

---

## Multi-Function Instruments

### Digilent Analog Discovery 2 (AD2)
**USB Multi-Instrument**

| Instrument | Specifications |
|-----------|---------------|
| Oscilloscope | 2-ch, ±25 V, 14-bit, 100 MSa/s, 30+ MHz BW |
| AWG | 2-ch, ±5 V, 14-bit, 100 MSa/s, 12+ MHz BW |
| Logic Analyzer | 16 channels, 100 MSa/s |
| Pattern Generator | 16 channels |
| Power Supplies | 0 to +5 V, 0 to -5 V |
| Other | Voltmeter, spectrum analyzer, network analyzer, impedance analyzer, protocol analyzer |

**Protocol Support:** UART, SPI, I2C, CAN, etc.

**Documentation:**
- [Reference Manual (PDF)](https://cdn-shop.adafruit.com/product-files/4652/4652_manual.pdf)
- [Analog Discovery Reference Manual](https://digilent.com/reference/_media/analog_discovery:analog_discovery_rm.pdf)
- [WaveForms SDK Reference (PDF)](https://s3-us-west-2.amazonaws.com/digilent/resources/instrumentation/waveforms/waveforms_sdk_rm.pdf)
- [Digilent Reference Wiki](https://digilent.com/reference/software/waveforms/waveforms-2/start)

**Software:**
- [WaveForms Download](https://digilent.com/reference/software/waveforms/waveforms-3/start) (Windows/Mac/Linux, free)

---

## Programmers

### XGecu TL866II Plus
**Universal USB Programmer**

| Specification | Value |
|--------------|-------|
| MCU | PIC24 |
| Interface | USB 1.1 |
| ZIF Socket | 40-pin |
| Supported ICs | 15,000+ |
| Max VPP | 18V |
| Operating Systems | Windows XP/7/8/10/11 |

**Supported Device Types:**
- **EEPROM/Flash:** 24/25/26/27/28/29/37/39/49/50 series (serial & parallel)
- **Microcontrollers:** 8051, Atmel AVR (ATmega, ATtiny, AT90), Microchip PIC (PIC10/12/16/18)
- **Programmable Logic:** GAL devices
- **Logic IC Testing:** 54/74 series, CD4000 CMOS

**Features:** ICSP interface, logic IC testing, SRAM testing, project file support

**Documentation:**
- [User Manual (PDF)](https://www.obdii365.com/upload/pro/tl866ii_plus_usb_programmer_user_manual.pdf)
- [User Manual (Alternative)](https://www.hadex.cz/spec/m545b.pdf)
- [T56/TL866II User Guide (PDF)](http://xgecu.com/MiniPro/T56_TL866II%20USER%20GUIDE.pdf)

**Software - Windows (Official):**
- [XGPro Download (Official)](http://www.xgecu.com/en)
- [Software Archive (GitHub Mirror)](https://github.com/Kreeblah/XGecu_Software)

**Software - Linux/macOS (Open Source):**
- [minipro (GitLab)](https://gitlab.com/DavidGriffith/minipro) - Command-line programmer
- [TL866 Utilities (GitHub)](https://github.com/radiomanV/TL866) - Firmware tools & Wine wrapper

**Linux Installation (minipro):**
```bash
sudo apt-get install build-essential pkg-config git libusb-1.0-0-dev
git clone https://gitlab.com/DavidGriffith/minipro.git
cd minipro
make
sudo make install
sudo cp udev/*.rules /etc/udev/rules.d/
sudo udevadm trigger
```

**Basic minipro Commands:**
```bash
minipro -L "CHIP"          # Search for chip
minipro -p "CHIP" -r out.bin   # Read chip to file
minipro -p "CHIP" -w in.bin    # Write file to chip
minipro -p "CHIP" -e           # Erase chip
minipro -p "CHIP" -c out.bin   # Verify chip against file
```

---

## Protocol Tools

### SparkFun Bus Pirate v3.6a
**Universal Serial Interface Tool**

| Specification | Value |
|--------------|-------|
| Supported Protocols | SPI, I2C, UART, 1-Wire, JTAG (limited), HD44780 LCD, raw 2-wire/3-wire |
| Voltage Modes | 3.3 V and 5 V I/O |
| On-board Supplies | 3.3 V and 5 V outputs (~150 mA) |
| Additional Features | Frequency measurement, PWM output, 10-bit ADC |
| Interface | USB (virtual COM port, FTDI-based) |
| Processor | PIC24FJ64 |

**Features:** Interactive command-line interface, binary scripting mode, bootloader for firmware updates

**Documentation:**
- [SparkFun Hookup Guide](https://learn.sparkfun.com/tutorials/bus-pirate-v36a-hookup-guide/all)
- [Dangerous Prototypes Manual](http://dangerousprototypes.com/docs/Bus_Pirate)
- [Bus Pirate Docs](https://docs.buspirate.com/)
- [GitHub Repository](https://github.com/sparkfun/Bus_Pirate)

**Software/Scripts:** Python (pyBusPirateLite), Perl, flashrom, AVRDUDE, OpenOCD

---

## Equipment Summary by Category

### Oscilloscopes (5)
| Model | Type | Bandwidth | Channels |
|-------|------|-----------|----------|
| Rigol DS1102E | DSO | 100 MHz | 2 |
| Tektronix TDS2024 | DSO | 200 MHz | 4 |
| Hitachi V-1150 | Analog | 150 MHz | 4 |
| DSO201 | Pocket DSO | 1 MHz | 1 |
| Analog Discovery 2 | USB | 30 MHz | 2 |

### Signal Generators (2)
| Model | Channels | Max Frequency |
|-------|----------|---------------|
| Rigol DG1022 | 2 | 20 MHz |
| Analog Discovery 2 | 2 | 12 MHz |

### Multimeters (3)
| Model | Type | Resolution |
|-------|------|------------|
| HP 34401A | Bench | 6½ digit |
| Rigol DM3058E | Bench | 5½ digit |
| Tenma 72-2055 | Handheld | 3½ digit |

### LCR Meters (2)
| Model | Type | Max Test Freq |
|-------|------|---------------|
| DER EE DE-5000 | Handheld | 100 kHz |
| Holdpeak HP-4070L | Handheld | 100 Hz |

### Power Supplies (2)
| Model | Output | Programmable |
|-------|--------|--------------|
| Korad KA3005P | 30V/5A | Yes (USB/RS-232) |
| QE-MS305D | 30V/5A | No |

### Logic Analyzers (2)
| Model | Channels | Max Sample Rate |
|-------|----------|-----------------|
| Saleae Logic Original | 8 digital | 24 MSa/s |
| Analog Discovery 2 | 16 digital | 100 MSa/s |

### Programmers (1)
| Model | Type | Supported ICs |
|-------|------|---------------|
| XGecu TL866II Plus | Universal | 15,000+ |

### Protocol Tools (1)
| Model | Protocols |
|-------|-----------|
| SparkFun Bus Pirate | SPI, I2C, UART, 1-Wire, JTAG |

---

## Software Resources

### Instrument Control
- **Rigol:** UltraScope, UltraSigma, UltraDMM
- **Keysight/Agilent:** BenchVue, IntuiLink
- **Digilent:** WaveForms
- **Saleae:** Logic 2
- **Universal:** sigrok/PulseView, PyVISA, NI-VISA

### Protocol Analysis & Debugging
- **OpenOCD** - JTAG/SWD debugging
- **AVRDUDE** - AVR programming
- **flashrom** - Flash chip programming
- **pyBusPirateLite** - Bus Pirate Python library

### Cross-Platform Tools
- **sigrok/PulseView** - Logic analyzer, oscilloscope, DMM support
- **PyVISA** - Python VISA instrument control
- **python-ivi** - IVI instrument drivers

---

*Document generated: December 2024*
