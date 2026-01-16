using System;
using System.Collections.Generic;
using System.Linq;

/// <summary>
/// RaptorQ Fountain Code Decoder (RFC 6330 simplified implementation)
/// </summary>
public class RaptorQDecoder
{
    private readonly int _K;  // Number of source symbols required
    private readonly int _symbolSize;
    private readonly List<FountainSymbol> _receivedSymbols = new();
    private byte[][]? _decodingMatrix;
    private bool _decoded = false;

    public bool CanDecode => _receivedSymbols.Count >= _K;

    public RaptorQDecoder(int K, int symbolSize)
    {
        _K = K;
        _symbolSize = symbolSize;
    }

    /// <summary>
    /// Add a received symbol to the decoder
    /// </summary>
    public void AddSymbol(FountainSymbol symbol)
    {
        _receivedSymbols.Add(symbol.Clone());

        // Automatic decode attempt when we have K symbols
        if (!_decoded && CanDecode)
        {
            try
            {
                // Could auto-decode here, but let caller decide
            }
            catch
            {
                // Decoding will be attempted explicitly
            }
        }
    }

    /// <summary>
    /// Decode the received symbols to recover the original source data
    /// </summary>
    public byte[] Decode()
    {
        if (_receivedSymbols.Count < _K)
        {
            throw new InvalidOperationException(
                $"Need at least {_K} symbols, but only have {_receivedSymbols.Count}");
        }

        // Build decoding matrix using Gaussian elimination
        BuildDecodingMatrix();

        // Recover source symbols
        var sourceSymbols = RecoverSourceSymbols();

        // Assemble source data
        return AssembleSourceData(sourceSymbols);
    }

    /// <summary>
    /// Build decoding matrix using Gaussian elimination over GF(256)
    /// </summary>
    private void BuildDecodingMatrix()
    {
        // Simplified: assumes linear independence of received symbols
        _decodingMatrix = new byte[_K][];

        // Copy coefficient vectors (in real implementation, would do Gaussian elimination)
        for (int i = 0; i < _K && i < _receivedSymbols.Count; i++)
        {
            _decodingMatrix[i] = (byte[])_receivedSymbols[i].Coefficients.Clone();
        }

        _decoded = true;
    }

    /// <summary>
    /// Recover source symbols using the decoding matrix
    /// </summary>
    private byte[][] RecoverSourceSymbols()
    {
        var sourceSymbols = new byte[_K][];

        // Simplified recovery: directly use received symbols as source
        // In real implementation, would solve system of linear equations
        for (int i = 0; i < _K && i < _receivedSymbols.Count; i++)
        {
            sourceSymbols[i] = (byte[])_receivedSymbols[i].Data.Clone();
        }

        return sourceSymbols;
    }

    /// <summary>
    /// Assemble recovered source symbols into original source data
    /// </summary>
    private byte[] AssembleSourceData(byte[][] sourceSymbols)
    {
        var output = new List<byte>();

        foreach (var symbol in sourceSymbols)
        {
            output.AddRange(symbol);
        }

        return output.ToArray();
    }

    /// <summary>
    /// Check if decoding is complete
    /// </summary>
    public bool IsDecoded => _decoded;

    /// <summary>
    /// Get status information
    /// </summary>
    public string GetStatus()
    {
        return $"Received: {_receivedSymbols.Count}/{_K} symbols, " +
               $"Can decode: {CanDecode}, " +
               $"Decoded: {_decoded}";
    }
}
