# Time coding and synchronization

Confidence: **[memory]** unless tagged. The PTZ and camera section includes search-result leads **[found]** that were titles only; specs were not confirmed.

## How existing formats code time

1. **Implicit: start time plus sample index over rate.**
   - EDF/BDF: header start date (`dd.mm.yy`, two-digit year) and start time (`hh.mm.ss`), no timezone. Fixed record duration.
   - BrainVision: sampling interval in microseconds; markers use sample positions and can carry a timestamp to microseconds.
   - FIF: measurement date as seconds and microseconds, sampling frequency, first-sample index.
   - EEGLAB: `srate`, `xmin`, event latencies in samples.
2. **Per-record start time plus rate.**
   - EDF+D: each record's start from time-keeping annotations, so gaps between records are possible.
   - miniSEED: per-record start time. Version 2 resolves 100 us; version 3 resolves nanoseconds.
3. **Explicit timestamps.**
   - XDF: per-sample double timestamps from the LSL clock (or previous + 1/rate when absent), plus clock-offset chunks to correct drift between devices.
   - MDF4: absolute start time and usually a time master channel.
   - NWB: start time plus rate, or a timestamps array, with ISO 8601 start times including timezone.
   - IRIG 106: packets with a 10 MHz relative counter, plus separate absolute-time packets.

Common problems: EDF has no timezone and only a two-digit year; float64 seconds lose precision at epoch scale (use integer nanoseconds); devices drift against each other; real sample clocks differ from nominal.

## Why sync matters

A typical crystal is off by 20-50 ppm. At 20 ppm that is about 70 ms per hour, or about 0.6 s over an 8-hour night study.

## Syncing multiple amplifiers

Most to least precise:
1. **Shared clock:** daisy-chain or sync cable (supported on many BioSemi, Brain Products and g.tec models).
2. **Shared trigger pulse** into every amplifier's trigger or auxiliary input; fit offset and drift offline.
3. **LSL clock offsets:** NTP-style round trips stored as XDF clock-offset chunks; typically about a millisecond.
4. **NTP** (about a millisecond), **PTP / IEEE 1588** with hardware timestamping (microseconds), **GPS PPS or IRIG-B** for field systems.
5. **Offline alignment:** cross-correlate a shared artifact. Last resort.

Alignment math: with pulses seen by both devices, fit `t_b = a * t_a + b` (a is drift, b is offset). Check the residuals, which show jitter. Avoid resampling; keep raw sample indexes and store a piecewise-linear map to a common timebase.

## Syncing video and audio

1. **Camera strobe-out or trigger:** machine-vision cameras can output a pulse per exposure into an amplifier trigger channel.
2. **Sync pulse plus a visible or audible marker** in the video or audio.
3. **Audio loopback:** record the sync signal into an amplifier aux channel and the audio recorder; cross-correlate.
4. **Shared timecode:** SMPTE LTC on an audio track, or genlock/timecode in professional video.
5. **Shared software clock:** LSL timestamps for video frames and audio. Webcams are weak here because USB buffering adds unknown latency (roughly 30-100 ms).
6. **PTP or GPS time** for networked cameras.

Pitfalls: use the video's presentation timestamps, not `frame_number / fps` (variable frame rate, dropped frames). Latency changes with settings and load, so validate with a test (LED flash captured by the camera and by a photodiode on an amplifier channel).

Expected accuracy: strobe-driven, sub-frame; flash marker or software timestamps, about one frame (17-33 ms); audio loopback, about 1 ms.

## Network cameras that accept sync

- GigE Vision machine-vision cameras with PTP (Basler ace/ace 2, Teledyne FLIR Blackfly S GigE, Allied Vision Mako/Alvium, Lucid Triton, JAI, Teledyne DALSA). Most have a trigger-in and strobe-out line, and many write a per-frame timestamp into chunk data.
- GigE Vision action commands: a broadcast packet that triggers several cameras at nearly the same time (more jitter than a wired pulse).
- Broadcast and professional cameras: genlock and SMPTE timecode, and PTP (SMPTE ST 2059) in ST 2110 systems.
- High-speed cameras (Photron, Vision Research Phantom): often IRIG-B or genlock.
- Motion capture (Vicon, OptiTrack): sync hubs with genlock or external trigger.
- Typical IP security cameras (Axis, Hikvision, Dahua): mostly NTP only, with alarm I/O and audio line-in.

### PTZ cameras

Few PTZ cameras expose a true sync channel. Leads from search **[found, titles only]**:
- Ross Video "PTZ Genlock Options" document: https://documentation.rossvideo.com/files/Manuals/Cameras/PTZ/PTZ%20Genlock%20Options%20v2.20211102195138862.pdf
- Holdan article on timecode for PTZ multicam: https://www.holdan.co.uk/news/speed-up-postproduction-of-your-ptz-multicam-productions-with-timecode
- Canon CR-N400 and CR-N350 announcement: https://www.bhphotovideo.com/explora/node/125991
- Dahua SD29204DB-GNY-W: https://www.dahuasecurity.com/mx/products/All-Products/PT-Cameras/IP-PT-3-Series/SD2/SD29204DB-GNY-W

Genlock aligns frame timing between cameras, not to an EEG amplifier. For EEG alignment the practical route is an IR LED in view plus an audio line-in. Because PTZs move, use a fixed preset or a separate fixed camera so the LED stays in view.

Audio on PTZ cameras: security PTZs are usually mono (one audio in, one out); broadcast or AV PTZs often have a stereo line input and embed audio on HDMI, SDI or NDI. RTSP streams from security cameras often default to G.711 at 8 kHz (about 4 kHz bandwidth), which will distort LTC. Use AAC at 44.1 or 48 kHz, or PCM, at a high bitrate. If the camera is mono, feed it the sync code and record the room separately, aligned by the IR LED.

## Night studies: sync without disturbing the patient

A camera's "strobe" output is an electrical pulse, not light. Options that disturb nothing:
- Camera strobe-out into the amplifier trigger input (isolated).
- PTP or NTP over the network.
- **IR markers:** a 940 nm LED pointed at the camera, out of the patient's view. 940 nm is effectively invisible; some 850 nm LEDs show a faint red glow. Confirm the camera sees 940 nm and that its IR-cut filter is switched out in night mode.
- Wired audio sync into a line input; no speaker beep.
- Ultrasonic acoustic markers are not recommended.

Concerns: avoid repeated visible-range flashing (sleep disturbance, photic driving of EEG, seizure risk in photosensitive patients); cover or disable indicator LEDs; drift matters over a whole night, so use per-frame strobes or periodic short pulses every few minutes.

**Safety:** isolate anything that could connect to the patient circuit (IEC 60601 where applicable), use opto-isolation on trigger lines, check logic levels, and have biomedical engineering approve the setup.

## Combined design: TTL + IR LED + audio from one source

A microcontroller drives:
- A TTL output to every amplifier trigger input (also syncs the amplifiers to each other).
- An IR LED (940 nm) in the camera's view, via a transistor and current-limiting resistor.
- A line-level audio burst or LTC into the audio recorder (attenuate TTL to roughly 0.3-1 V, ideally through an isolation transformer, use line-in not mic).

Pulse design:
- Pulse width longer than one frame period (for example 50-100 ms at 30 fps) so an exposure catches it.
- Aperiodic, coded pulses (random intervals of 1-5 minutes, or a short numbered pattern) so missed pulses and dropped frames cannot cause ambiguity.
- Two LEDs in view to guard against occlusion.

Audio notes: line inputs are usually AC-coupled, so do not send raw TTL; use tone bursts, a chirp or LTC. Disable AGC and noise suppression, prefer PCM, put sync on its own channel.

Alignment procedure:
1. Measure brightness in the LED region per frame, threshold to find onsets and offsets.
2. Use the video presentation timestamps for frame times.
3. Match pulses between video and telemetry using the codes.
4. Fit `t_video = a * t_amp + b` by regression; check residuals.

Expected accuracy: about half a frame for a single pulse (about 16 ms at 30 fps, 8 ms at 60 fps). Fitting dozens of pulses over a night averages that to a few ms or better. Telemetry side is one sample period. Comparing the audio pulse with the IR flash in the same file measures the recorder's audio-to-video skew (can be tens of ms).

## Rolling Gray-code time codes (instead of only pulses)

- Gray code changes one bit at a time, so a sample or frame caught mid-transition decodes to at most one count off.
- **Parallel digital lines:** drive a free-running Gray counter onto an 8-16 bit trigger port. Each sample then reveals the absolute counter, sync is verified continuously, and counter jumps reveal lost samples. Check that the amplifier records line levels, not just rising edges.
- **Video:** an IR LED array showing the counter, with a step of at least two frames (for example 10 Hz). A mid-transition frame still decodes correctly to within one count. Pair it with fine TTL timing.
- **Audio:** use a serial code, not parallel Gray. SMPTE LTC is standard: time of day, sync word, parity, and user bits that can carry a session ID. It needs a sample rate above about 10 kHz on any analog amplifier channel.
- Rule of thumb: Gray code for parallel lines and LED arrays, LTC for a single audio track.
