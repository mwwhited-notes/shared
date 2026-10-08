# Draft: a seekable, losslessly compressed multichannel format

Status: **design sketch only.** Nothing here is implemented or tested, and no `.ksy` exists for it yet. Compression ratio figures are **[memory]**.

## Goals

- Byte-aligned sample widths (8/16/24/32 bits, up to 8 bytes allowed).
- Streamed (append-only) writing with lossless compression.
- Jump to a time index with bounded decompression work.
- Survive crashes and data loss, and represent gaps honestly.
- Support several amplifiers, mixed rates and widths, and external media.

## First check existing options

- **Zarr or HDF5/NWB with Blosc (shuffle + zstd):** chunk as all channels x about 1,000 samples; seek by computing the chunk index. Most tooling.
- **miniSEED v3:** already has time-indexed records with lossless delta compression. Read its spec before inventing anything.
- Build a custom format only if you need simple append-only writes, crash recovery, or no heavy dependencies.

## Layout sketch

```
Header | Block | Block | Block | ... | Footer index | Footer pointer (last 8 bytes)
```

**Header**
- Magic and version.
- Metadata (channel labels, etc.) as a block or JSON/CBOR section.
- Channel groups. For each group: stored width, ADC bit depth, sample rate (rational), scale and offset to physical units, justification flag.

**Data block** (independently decodable)
- Sync marker, first sample index (u64) per group, frame count, compressed size, codec id, CRC32.
- Flags: discontinuity before this block.
- Body: channel-major within each group.

**Block encoding pipeline**
1. Widen to int32 (a delta of 24-bit values needs 25 bits).
2. Per-channel delta (first or second order), then zigzag.
3. Byte-plane shuffle.
4. zstd or LZ4.

**Footer index:** list of (first sample index, file offset) per block, plus a pointer to it in the final 8 bytes.

**Time seek:** convert time to sample index, binary-search the index, decompress one block. With about one second per block, a seek decompresses at most one second of data. Smaller blocks give finer seeks but worse ratios.

**Crash recovery:** blocks are self-describing (sync marker plus CRC), so a lost index can be rebuilt by scanning. Concatenating files also works. Option: periodic index blocks. A crash loses at most one block.

## Time

- Per group: start time as int64 nanoseconds since the UTC epoch, plus first-sample index per block.
- Sample rate as a rational (for example 1000000/1001) to avoid float drift. Real sample clocks also differ slightly from nominal.
- Optional explicit timestamp stream for irregular data.
- Clock-offset records (device clock to common timebase), in the style of XDF.

## Gaps and data loss

- A gap is `next_block_first_index - (prev_block_first_index + prev_frame_count)`. No fill needed.
- "Discontinuity before block" flag.
- Optional compressed validity bitmap per channel group for invalid samples inside a block.
- Cause code: packet loss, buffer overrun, clipping.
- Keep the hardware packet or sample counter channel when the amplifier has one. It is the most direct evidence of loss.
- Do not silently interpolate across gaps. Be careful when filtering across them.

## Other record types

- Events and annotations (separate block type, like XDF chunk tags).
- Sync pulse and rolling-code channels (see `05-time-and-sync.md`).
- Clock-offset records.
- External media references: file path plus start offset and clock map (NWB's image series with external file, start frame and timestamps is a precedent).

## Open decisions

- Block size and whether it varies.
- Codec set (zstd only, or also LZ4 and a FLAC-style Rice coder).
- Endianness (little-endian is the obvious choice).
- Metadata encoding (JSON vs CBOR).
- Versioning and extension mechanism.
- Whether per-channel-group blocks are separate or interleaved in one block.
- Whether to write a `.ksy` description for it.
