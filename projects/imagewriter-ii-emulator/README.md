# ImageWriter II Printer Emulator

## Overview

PC-based emulator/simulator that captures output from Apple II programs (The Print Shop, The Toy Shop, AppleWorks, etc.) and converts to modern printable formats (PDF, PNG) or routes to contemporary printers. Emulates an ImageWriter II dot-matrix printer over serial connection.

**Status:** Planning
**Hardware:** Serial connection between Apple II and modern PC
**Output:** PDF, PNG, modern USB/network printers

## Problem Statement

Classic Apple II software like The Print Shop creates output for ImageWriter/ImageWriter II dot-matrix printers. These printers:
- Are 40+ years old and increasingly rare/unreliable
- Use proprietary command sets
- Produce physical output only (no digital capture)
- Require special ribbons and paper

**Solution:** Intercept printer data stream, decode commands, render to modern formats.

## Use Cases

1. **Print Shop Banners** - Capture banner output as PDF or print on modern printer
2. **AppleWorks Documents** - Convert word processing documents to PDF
3. **Graphics Programs** - Capture hi-res graphics output
4. **Historical Preservation** - Archive printed output digitally
5. **Modern Workflow** - Use vintage software with contemporary printers

## Architecture

```
[Apple II] --Serial--> [PC Serial Port] --Software--> [Renderer] --> [PDF/PNG/Printer]
   |                        |                           |
   | ImageWriter           | Capture &                 | Modern
   | ESC codes             | Decode                    | Output
```

### Components

1. **Serial Capture** - Read data from Apple II serial port
2. **Protocol Decoder** - Parse ImageWriter II command set
3. **Rendering Engine** - Convert to bitmap/vector graphics
4. **Output Module** - Save as PDF/PNG or send to printer

## Hardware Requirements

### Apple II Side

**Connection Options:**

#### Option A: Serial Port (Recommended)
- Apple IIc/IIgs built-in serial ports
- Apple Super Serial Card (for II/II+/IIe)
- Settings: 9600 baud, 8-N-1 typical

#### Option B: Parallel Port
- Apple II Parallel Interface Card
- Requires parallel-to-USB adapter
- May need custom driver (see DeviceBridge project)

### PC Side

**Connection Options:**

#### Option A: USB-to-Serial Adapter
- Modern USB to RS-232 adapter (~$10-20)
- Null modem configuration may be needed
- Software reads from COM port (Windows) or /dev/ttyUSB (Linux)

#### Option B: Raspberry Pi Serial GPIO
- Direct GPIO serial connection
- Voltage level shifting (3.3V ↔ 5V)
- Lower latency than USB adapter

#### Option C: Network Bridge (ESP32)
- ESP32 captures serial, forwards over WiFi
- Allows wireless printing from Apple II
- More complex but very flexible

## ImageWriter II Protocol

### Command Set

The ImageWriter II uses an ESC/P-like command set with Apple-specific extensions.

#### Basic Commands

| Command | Hex | Description |
|---------|-----|-------------|
| **Text** | 0x20-0x7E | Printable ASCII characters |
| **Carriage Return** | 0x0D | Return print head to left margin |
| **Line Feed** | 0x0A | Advance paper one line |
| **Form Feed** | 0x0C | Eject page |
| **Backspace** | 0x08 | Move print head left one character |
| **Tab** | 0x09 | Advance to next tab stop |
| **Bell** | 0x07 | Sound buzzer (ignore in emulator) |

#### ESC Sequences

| Sequence | Description | Example |
|----------|-------------|---------|
| **ESC E** | Enable emphasized (bold) | `1B 45` |
| **ESC F** | Disable emphasized | `1B 46` |
| **ESC G** | Enable double-strike | `1B 47` |
| **ESC H** | Disable double-strike | `1B 48` |
| **ESC p 0** | Proportional spacing off | `1B 70 00` |
| **ESC p 1** | Proportional spacing on | `1B 70 01` |
| **ESC W 1** | Double-width on | `1B 57 01` |
| **ESC W 0** | Double-width off | `1B 57 00` |
| **ESC T** | Disable subscript/superscript | `1B 54` |
| **ESC S 0** | Enable superscript | `1B 53 00` |
| **ESC S 1** | Enable subscript | `1B 53 01` |
| **ESC B** | Set vertical tabs | `1B 42 [n1] [n2] ... 00` |
| **ESC D** | Set horizontal tabs | `1B 44 [n1] [n2] ... 00` |
| **ESC C** | Set page length | `1B 43 [n]` |
| **ESC l [n]** | Set left margin | `1B 6C [n]` |
| **ESC Q [n]** | Set right margin | `1B 51 [n]` |
| **ESC A [n]** | Set line spacing (n/72") | `1B 41 [n]` |

#### Graphics Mode

| Sequence | Description |
|----------|-------------|
| **ESC G [nL] [nH] [data...]** | Print graphics (n bytes of data) |
| **ESC K [nL] [nH] [data...]** | Single-density graphics (60 DPI) |
| **ESC L [nL] [nH] [data...]** | Double-density graphics (120 DPI) |
| **ESC Y [nL] [nH] [data...]** | High-speed double-density graphics |
| **ESC Z [nL] [nH] [data...]** | Quadruple-density graphics (240 DPI) |

**Notes:**
- `[nL]` and `[nH]` are low and high bytes of data count
- Graphics data is column-wise (8 vertical dots per byte)
- Bit 0 = top dot, Bit 7 = bottom dot

#### AppleWorks Specific

AppleWorks uses standard ImageWriter commands plus:
- Bold via ESC E/F
- Underline via continuous backspace + underscore
- Headers/footers via tab positioning

#### Print Shop Specific

The Print Shop (banners):
- Heavy use of graphics mode (ESC K/L/Z)
- Large bitmap images sent column-by-column
- May split across multiple sheets

## Software Architecture

### Platform: .NET Core / .NET 8

**Why .NET:**
- Cross-platform (Windows, Linux, macOS)
- Excellent serial port support (`System.IO.Ports`)
- PDF generation libraries (PdfSharp, iText)
- Image libraries (ImageSharp, System.Drawing)
- Builds on existing PrinterEmulator work

### Class Structure

```
ImageWriterEmulator/
├── SerialCapture/
│   ├── SerialPortReader.cs       # Read from COM port
│   └── DataStreamBuffer.cs       # Buffer incoming data
├── Protocol/
│   ├── CommandParser.cs          # Parse ESC sequences
│   ├── Commands/
│   │   ├── TextCommand.cs
│   │   ├── FormattingCommand.cs
│   │   └── GraphicsCommand.cs
│   └── PrinterState.cs           # Track current printer state
├── Rendering/
│   ├── VirtualPage.cs            # Bitmap representation of page
│   ├── FontRenderer.cs           # Render text with printer fonts
│   └── GraphicsRenderer.cs       # Render dot-matrix graphics
└── Output/
    ├── PdfExporter.cs            # Export to PDF
    ├── ImageExporter.cs          # Export to PNG/JPEG
    └── PrinterOutput.cs          # Send to modern printer
```

### Rendering Engine

**Page Model:**
- Virtual page: 8.5" × 11" @ 144 DPI (ImageWriter II resolution)
- Bitmap: 1224 × 1584 pixels
- Track print head position (X, Y in 1/144")
- Apply formatting (bold, double-width, etc.)

**Font Rendering:**
- ImageWriter II used a 9×9 dot matrix font
- Emulate with bitmap fonts or TrueType monospace
- Support: normal, bold, double-width, superscript, subscript

**Graphics Rendering:**
- Each byte represents 8 vertical dots
- Convert to bitmap scan lines
- Support multiple densities (60/120/240 DPI)

## Implementation Phases

### Phase 1: Serial Capture (Week 1-2)
- **Goal:** Read data from Apple II serial port
- **Deliverables:**
  - Console app that reads serial data
  - Hex dump output for analysis
  - Test with simple "HELLO WORLD" from Apple II

**Test Command (on Apple II):**
```basic
10 PR#2
20 PRINT "HELLO FROM APPLE II"
```

---

### Phase 2: Command Parser (Week 3-4)
- **Goal:** Parse ImageWriter II commands
- **Deliverables:**
  - Command parser class
  - State machine for ESC sequences
  - Unit tests for all commands

**Test:**
- Send pre-recorded ImageWriter data stream
- Verify all commands parsed correctly

---

### Phase 3: Text Rendering (Week 5-6)
- **Goal:** Render text to bitmap
- **Deliverables:**
  - Font renderer with 9×9 dot matrix font
  - Support for bold, double-width
  - Page buffer management

**Test:**
- Render simple text document
- Export to PNG

---

### Phase 4: Graphics Rendering (Week 7-8)
- **Goal:** Render graphics mode data
- **Deliverables:**
  - Graphics mode parser
  - Bitmap rendering for all densities
  - Line-by-line assembly

**Test:**
- Send simple bitmap (e.g., 8×8 checkerboard)
- Verify correct rendering

---

### Phase 5: PDF Export (Week 9)
- **Goal:** Export rendered pages as PDF
- **Deliverables:**
  - PDF generator using PdfSharp
  - Embed bitmap pages
  - Multi-page support

**Test:**
- Print AppleWorks document
- Verify PDF output

---

### Phase 6: Modern Printer Output (Week 10)
- **Goal:** Send to modern printers
- **Deliverables:**
  - Print dialog integration
  - Direct printer output
  - Platform-specific print APIs

**Test:**
- Print to USB/network printer
- Verify quality and formatting

---

### Phase 7: Print Shop Integration (Week 11-12)
- **Goal:** Perfect rendering of Print Shop banners
- **Deliverables:**
  - Banner assembly (multi-page)
  - High-quality graphics rendering
  - Proper scaling and DPI handling

**Test:**
- Create banner in Print Shop
- Verify digital output matches expected result

---

## Configuration

### App Settings (appsettings.json)

```json
{
  "Serial": {
    "PortName": "COM3",          // Windows
    // "PortName": "/dev/ttyUSB0", // Linux
    "BaudRate": 9600,
    "Parity": "None",
    "DataBits": 8,
    "StopBits": 1
  },
  "Rendering": {
    "DPI": 144,
    "PageWidth": 8.5,
    "PageHeight": 11.0,
    "Font": "ImageWriter9x9.ttf",
    "AutoEject": true
  },
  "Output": {
    "DefaultFormat": "PDF",       // PDF, PNG, Printer
    "OutputDirectory": "./output/",
    "FileNamePattern": "print_{date}_{time}.pdf"
  }
}
```

### CLI Usage

```bash
# Start emulator (listen on COM3)
dotnet run --project ImageWriterEmulator

# Specify different port
dotnet run --project ImageWriterEmulator --port COM4

# Save to PNG instead of PDF
dotnet run --project ImageWriterEmulator --format PNG

# Send directly to printer
dotnet run --project ImageWriterEmulator --format Printer
```

## Testing Strategy

### Unit Tests
- Command parsing (all ESC sequences)
- Text rendering (all formatting modes)
- Graphics decoding (all densities)

### Integration Tests
- Full document rendering (AppleWorks)
- Banner rendering (Print Shop)
- Multi-page documents

### Hardware Tests
- Connect to real Apple II
- Print from AppleWorks
- Print from The Print Shop
- Verify output quality

## Hardware Connection Guide

### Apple IIc to PC via Serial

**Equipment:**
- Apple IIc with built-in serial ports
- DIN-5 to DB-25 cable (or DB-9)
- USB-to-Serial adapter (if PC lacks serial port)
- Null modem adapter (may be needed)

**Wiring:**
```
Apple IIc DIN-5 Serial Port:
Pin 1: DTR (Data Terminal Ready)
Pin 2: DCD (Data Carrier Detect) or RX
Pin 3: TXD (Transmit Data)
Pin 4: GND (Ground)
Pin 5: RXD (Receive Data)

DB-9 (PC Serial):
Pin 2: RXD ← connects to Apple Pin 3 (TXD)
Pin 3: TXD → connects to Apple Pin 5 (RXD)
Pin 5: GND ← connects to Apple Pin 4 (GND)
```

**Software Setup (Apple IIc):**
```basic
REM Set serial port 2 as printer
PR#2

REM Configure for 9600 baud
<Ctrl-A> 9600 <Enter>
```

**Test:**
```basic
10 PR#2
20 PRINT "TEST PRINT"
30 PR#0
```

Should see "TEST PRINT" in emulator console.

---

### Apple IIe/II+ with Super Serial Card

**Slot:** Usually Slot 1 or 2
**Jumpers:** Set for 9600 baud, no parity, 8 data bits, 1 stop bit
**Cable:** Same as IIc above

**Software:**
```basic
PR#1  REM or PR#2 depending on slot
```

---

## Related Work

### Matt's GitHub Projects

- **[PrinterEmulator](https://github.com/mwwhited/PrinterEmulator)** - TDS2024 IEEE-1284 printer capture
  - Provides foundation for printer protocol handling
  - Parallel port capture experience

- **[DeviceBridge](https://github.com/mwwhited/DeviceBridge)** - Parallel-to-USB capture
  - Hardware bridge design patterns
  - Data stream buffering

### Integration Points

This project complements:
- **Apple II Disk Archival** - Preserve Print Shop disks, then print output digitally
- **Home Automation** - Could trigger prints from automation system
- **SCPI Instrument Control** - Similar serial protocol handling

## Future Enhancements

### Phase 2 Features
- **Wireless Printing** - ESP32-based WiFi bridge
- **Web Interface** - Monitor printer status, view queue
- **Cloud Storage** - Auto-upload PDFs to Google Drive/Dropbox
- **OCR Integration** - Extract text from rendered pages
- **Color Emulation** - ImageWriter Color support

### Advanced Features
- **Print Shop Companion** - Special handling for Screen Magic
- **AppleWorks Templates** - Pre-defined document types
- **Font Library** - Multiple dot-matrix fonts
- **Scaling Options** - Resize output for modern paper sizes

## Resources

### Documentation
- **ImageWriter II Technical Reference** - Apple Computer, Inc. (1985)
- **Apple II Reference Manual** - Serial port specifications
- **ESC/P Reference** - Epson printer commands (similar)

### Communities
- **/r/apple2** - Reddit community for testing
- **comp.sys.apple2** - Usenet group
- **VCF (Vintage Computer Federation)** - Hardware enthusiasts

### Software
- **PdfSharp** - .NET PDF generation (MIT license)
- **ImageSharp** - .NET image processing (Apache 2.0)
- **System.IO.Ports** - Built-in .NET serial port support

## Project Structure

```
imagewriter-ii-emulator/
├── README.md                           # This file
├── docs/
│   ├── protocol-specification.md      # ImageWriter II command reference
│   ├── hardware-setup.md              # Wiring diagrams
│   └── print-shop-banners.md          # Special handling for Print Shop
├── src/
│   └── ImageWriterEmulator/           # .NET Core project
│       ├── Program.cs
│       ├── SerialCapture/
│       ├── Protocol/
│       ├── Rendering/
│       └── Output/
├── tests/
│   ├── ImageWriterEmulator.Tests/    # Unit tests
│   └── TestData/                      # Sample printer streams
└── examples/
    ├── simple-text.txt                # Basic text output
    ├── apples-formatted.txt          # AppleWorks sample
    └── print-shop-banner.bin          # Graphics mode sample
```

## Next Steps

1. **Research Phase**
   - [x] Document ImageWriter II protocol
   - [ ] Find ImageWriter II technical manual (PDF)
   - [ ] Analyze Print Shop output samples

2. **Setup Phase**
   - [ ] Acquire USB-to-Serial adapter
   - [ ] Test Apple IIc serial port
   - [ ] Verify cable wiring

3. **Development Phase**
   - [ ] Create .NET Core project
   - [ ] Implement serial capture
   - [ ] Build command parser
   - [ ] Develop rendering engine

4. **Testing Phase**
   - [ ] Test with AppleWorks
   - [ ] Test with The Print Shop
   - [ ] Verify PDF output quality

## Success Criteria

- ✅ Captures all output from Apple II serial port
- ✅ Correctly parses ImageWriter II commands
- ✅ Renders text with proper formatting
- ✅ Renders graphics at all supported densities
- ✅ Exports high-quality PDFs
- ✅ Prints banners from The Print Shop
- ✅ Handles AppleWorks documents
- ✅ Cross-platform (Windows, Linux, macOS)

---

**Started:** 2026-01-19
**Target Completion:** 12 weeks
**Status:** Planning
**Author:** Matt Whited ([mwwhited](https://github.com/mwwhited))
**Organizations:** [mwwhited](https://github.com/mwwhited), [OutOfBandDevelopment](https://github.com/OutOfBandDevelopment)
