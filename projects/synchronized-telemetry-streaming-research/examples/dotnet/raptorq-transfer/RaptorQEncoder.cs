using System;
using System.Collections.Generic;
using System.Linq;

/// <summary>
/// RaptorQ Fountain Code Encoder (RFC 6330 simplified implementation)
/// </summary>
public class RaptorQEncoder
{
    private readonly byte[] _sourceData;
    private readonly int _symbolSize;
    private readonly int _sourceSymbolCount;
    private readonly Random _random;
    private int _symbolCounter = 0;

    public int SourceSymbolCount => _sourceSymbolCount;

    public RaptorQEncoder(byte[] sourceData, int symbolSize)
    {
        _sourceData = sourceData ?? throw new ArgumentNullException(nameof(sourceData));
        _symbolSize = symbolSize;
        _sourceSymbolCount = (sourceData.Length + symbolSize - 1) / symbolSize;
        _random = new Random();
    }

    /// <summary>
    /// Generate fountain code symbols
    /// </summary>
    public IEnumerable<FountainSymbol> GenerateSymbols(int count)
    {
        for (int i = 0; i < count; i++)
        {
            yield return GenerateSymbol();
        }
    }

    /// <summary>
    /// Generate a single fountain code symbol
    /// </summary>
    private FountainSymbol GenerateSymbol()
    {
        byte[] symbol = new byte[_symbolSize];

        // Simple linear combination: weighted sum of source symbols
        // In real RFC 6330, uses more sophisticated LT code generation
        for (int si = 0; si < _sourceSymbolCount; si++)
        {
            byte weight = (byte)_random.Next(256);

            int sourceOffset = si * _symbolSize;
            int sourceLen = Math.Min(_symbolSize, _sourceData.Length - sourceOffset);

            for (int i = 0; i < _symbolSize; i++)
            {
                if (sourceOffset + i < _sourceData.Length)
                {
                    // Simple GF(256) multiplication and addition (XOR)
                    byte sourceVal = _sourceData[sourceOffset + i];
                    symbol[i] ^= (byte)(GF256Multiply(sourceVal, weight) & 0xFF);
                }
            }
        }

        return new FountainSymbol
        {
            EncodingSymbolId = _symbolCounter++,
            Data = symbol,
            Coefficients = GenerateCoefficients()
        };
    }

    /// <summary>
    /// Generate coefficient vector for this symbol
    /// </summary>
    private byte[] GenerateCoefficients()
    {
        byte[] coeffs = new byte[_sourceSymbolCount];
        for (int i = 0; i < coeffs.Length; i++)
        {
            coeffs[i] = (byte)_random.Next(256);
        }
        return coeffs;
    }

    /// <summary>
    /// Simple GF(256) multiplication (Galois Field)
    /// </summary>
    private static byte GF256Multiply(byte a, byte b)
    {
        if (a == 0 || b == 0) return 0;

        int result = 0;
        int highBit = 0x80;

        for (int i = 0; i < 8; i++)
        {
            if ((b & (1 << i)) != 0)
            {
                result ^= (a << i);
            }
        }

        // Reduction modulo irreducible polynomial x^8 + x^4 + x^3 + x^2 + 1 (0x11D)
        while (result > 0xFF)
        {
            int shift = 7;
            while ((result & (1 << (shift + 8))) == 0) shift--;

            result ^= (0x11D << shift);
        }

        return (byte)result;
    }
}

/// <summary>
/// Represents a single fountain code symbol
/// </summary>
public class FountainSymbol
{
    public int EncodingSymbolId { get; set; }
    public byte[] Data { get; set; } = Array.Empty<byte>();
    public byte[] Coefficients { get; set; } = Array.Empty<byte>();

    public FountainSymbol Clone()
    {
        return new FountainSymbol
        {
            EncodingSymbolId = EncodingSymbolId,
            Data = (byte[])Data.Clone(),
            Coefficients = (byte[])Coefficients.Clone()
        };
    }
}
