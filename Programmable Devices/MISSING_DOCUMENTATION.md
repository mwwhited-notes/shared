# Missing Documentation

This file tracks documentation that couldn't be automatically downloaded and requires manual action.

---

## Pending Downloads

### RedBear Blend Micro

- [ ] **nRF8001 Datasheet** - BLE module datasheet
  - Source: https://infocenter.nordicsemi.com/pdf/nRF8001_PS_v1.3.pdf
  - Issue: Nordic website blocks direct downloads, requires JavaScript navigation
  - Manual download: Visit Nordic InfoCenter, navigate to nRF8001 product page, download Product Specification PDF
  - Alternative: Search "nRF8001 datasheet PDF" for cached versions

### ATmega32A

- [ ] **ATmega32A Datasheet** - Main MCU datasheet
  - Source: https://ww1.microchip.com/downloads/en/DeviceDoc/Atmel-8155-8-bit-Microcontroller-AVR-ATmega32A_Datasheet.pdf
  - Issue: Microchip website blocks automated downloads
  - Manual download: Visit Microchip.com, search "ATmega32A datasheet", download PDF
  - File: `atmega32/ATmega32A_Datasheet.pdf`

### ATF16V8B

- [ ] **ATF16V8B Datasheet** - GAL/SPLD datasheet
  - Source: https://ww1.microchip.com/downloads/en/DeviceDoc/Atmel-0364-PLD-ATF16V8B-Datasheet.pdf
  - Issue: Microchip website blocks automated downloads
  - Manual download: Visit Microchip.com, search "ATF16V8B datasheet"
  - File: `atf16v8b/ATF16V8B_Datasheet.pdf`

### Xilinx XC95108

- [ ] **XC9500 Family Datasheet** - CPLD datasheet
  - Source: https://docs.amd.com/v/u/en-US/ds063
  - Issue: AMD/Xilinx website requires JavaScript navigation
  - Manual download: Visit AMD/Xilinx docs, search "XC9500 datasheet"
  - File: `xilinx-xc95108/XC9500_Datasheet.pdf`

### Velleman K8048RS

- [ ] **K8048 User Manual** - PIC programmer manual
  - Source: https://www.velleman.eu/downloads/0/user/usermanual_k8048_vm111.pdf
  - Issue: Velleman website returns XML error for PDF links
  - Manual download: Visit velleman.eu, navigate to K8048 support page
  - File: `velleman-k8048rs/K8048_UserManual.pdf`

### Basic Stamp 2

- [ ] **PBASIC Reference Manual** - Programming manual
  - Source: https://www.parallax.com/package/basic-stamp-syntax-and-reference-manual/
  - Issue: Parallax website requires navigation to download
  - Manual download: Visit parallax.com, search "Basic Stamp manual", download PDF
  - File: `parallax-basic-stamp-2/BasicStamp2_Manual.pdf`

### Zilog Z8 Encore!

- [ ] **Z8F0822 Datasheet** - MCU datasheet
  - Source: https://www.zilog.com/docs/z8encore/PS0199.pdf
  - Issue: Zilog website may block direct downloads
  - Manual download: Visit zilog.com, navigate to Z8 Encore! documentation
  - File: `zilog-z8/Z8F0822_Datasheet.pdf`

### STC 89C52RC

- [ ] **STC89C52RC Datasheet (English)** - MCU datasheet
  - Source: http://www.stcmicro.com/datasheet/STC89C52RC-en.pdf
  - Issue: STC website may be unreliable; Chinese site
  - Manual download: Visit stcmicro.com or search for cached English datasheet
  - Alternative: Search "STC89C52RC datasheet english PDF"
  - File: `stc-89c52rc/STC89C52RC_Datasheet.pdf`

### Netduino Mini

- [ ] **Main Documentation** - Board reference, schematic, getting started guide
  - Source: Original Netduino site (netduino.com) is defunct
  - Issue: Company discontinued, documentation scattered across archive sources
  - Manual download:
    1. Try archive.org: https://web.archive.org/web/*/netduino.com/*
    2. Search GitHub for cached documentation
    3. Check Wilderness Labs (acquired Netduino assets)
  - Note: .NET Micro Framework is deprecated; documentation may be limited

- [ ] **AT91SAM7X512 Datasheet** - Main MCU datasheet
  - Source: Microchip/Atmel website
  - Issue: Product page may redirect to newer parts
  - Manual download: Search Microchip.com for "AT91SAM7X512 datasheet"

- [ ] **Pinout Image** - Board pinout diagram
  - Source: Unknown
  - Issue: No official pinout diagram found online
  - Manual download: May need to create from schematic or community resources

---

## Completed Downloads

*Move items here when manually downloaded and verified*

<!--
### Example Device
- [x] **Document Type** - Downloaded YYYY-MM-DD
  - Verified content matches device
  - File: `device-folder/filename.pdf`
-->

---

## Notes

- Check this file monthly for items that may have become available
- Archive.org Wayback Machine is often useful for discontinued products
- Community forums (EEVBlog, Reddit r/embedded) may have cached documentation
- When adding new entries, include all attempted sources and specific failure reasons
