# Riglol - Rigol Instrument Option Unlock Tool

Reference note for [rigol.eccentricworkshop.com](http://rigol.eccentricworkshop.com/) ("Riglol"),
a third-party tool that generates unlock codes for paid Rigol firmware options using the
instrument's serial number.

## What It Unlocks

Documented support (per [nyctomachia's Riglol writeup](https://nyctomachia.wordpress.com/2018/09/02/riglol-unlock-extra-features-on-rigol-oscilloscopes/)
and the tool's own model list) covers:

- **DS1000Z-series oscilloscopes**: options like DSAB (advanced triggers), DSAC (decoders), DSAE
  (memory expansion), DSAJ (recorder), and a combined "DSER" option that bumps bandwidth to 100MHz,
  expands memory 12Mpts → 24Mpts, and unlocks advanced triggers/decoders/recording in one shot
- **DS2000 and DS4000 series** oscilloscopes
- **DP832** programmable power supply
- **DSA815** spectrum analyzer

**DG-series arbitrary waveform generators (e.g. the owned [DG1022](../../.personal/incoming/test-equipment.md)):
support not confirmed.** Research turned up no documented DG1022/DG-series option list for this
tool — check the tool's site directly for current model coverage before assuming it applies.

## How It Works

Enter the instrument's serial number into the web tool, select the desired option code, and it
generates an unlock key entered via the instrument's menu — no firmware flashing involved.

## Notes

- Third-party tool, not Rigol-sanctioned — unlocking paid options this way likely voids any
  official support/warranty path for those features
- Relevant test equipment already owned: [DSA815 is on the workshop wishlist](../../workshop-capabilities.md#wishlist-would-expand-capabilities) — if acquired, this tool may be directly useful for it

## References

- [Riglol - Rigol Unlocker](http://rigol.eccentricworkshop.com/)
- [Riglol hack: unlock extra features on Rigol oscilloscopes - nyctomachia](https://nyctomachia.wordpress.com/2018/09/02/riglol-unlock-extra-features-on-rigol-oscilloscopes/)
- [Rigol Scope Hack - N5DUX](http://www.n5dux.com/ham/riglol/)

---

*Last updated: 2026-07-24*
