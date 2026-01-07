# Tablet Dashboard Project - Context Prompt

## Background

I have a Samsung Galaxy Tab 4 Nook (SM-T230NU) currently running Android 4.4.2 that I want to repurpose as a home automation dashboard/console.

## Current Home Automation Setup

- Raspberry Pi with Homeseer
- Z-Wave devices
- Looking to replace this setup

## Goals

1. **Flash custom ROM on tablet** - LineageOS 14.1 (Android 7.1) is the recommended option for this device. Will need TWRP recovery first, flashed via Odin.

2. **Replace Homeseer** - Evaluating alternatives, likely Home Assistant running on a Pi.

3. **Use tablet as dedicated dashboard console** - Wall-mounted or tabletop display for home automation control.

## Key Technical Details

- Device: SM-T230NU (Samsung Galaxy Tab 4 Nook)
- Current OS: Android 4.4.2
- Target OS: LineageOS 14.1 (Android 7.1)
- Screen: 1280x800
- Architecture: ARM (not ARM64) - important for GApps selection

## Dashboard Software Options Being Considered

- Fully Kiosk Browser (kiosk mode, motion wake, battery management)
- Home Assistant Companion App
- WallPanel (open source Fully Kiosk alternative)

## Outstanding Decisions

- Final choice of home automation platform (Home Assistant vs Hubitat vs OpenHAB)
- Dashboard app selection
- Battery/charging management strategy for always-on tablet

## Next Steps

- Find TWRP and LineageOS downloads for SM-T230NU on XDA
- Plan the flashing process
- Decide on home automation platform replacement
