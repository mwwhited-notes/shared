#!/usr/bin/env dotnet
"""
RaptorQ Fountain Code Transfer Example
Demonstrates erasure-coded file transfer with high packet loss tolerance.
RFC 6330 compliant implementation.
"""

using System;
using System.Diagnostics;
using System.Linq;

// Example main entry point
class Program
{
    static void Main(string[] args)
    {
        Console.WriteLine("RaptorQ Fountain Code Transfer Example");
        Console.WriteLine("=====================================\n");

        if (args.Length > 0 && args[0] == "benchmark")
        {
            RunBenchmark();
        }
        else
        {
            RunDemo();
        }
    }

    static void RunDemo()
    {
        Console.WriteLine("Demo: File transfer with packet loss\n");

        // Create source data
        byte[] sourceData = System.Text.Encoding.UTF8.GetBytes(
            "This is test data for RaptorQ encoding. " +
            "It will be encoded into fountain code symbols and recovered even with packet loss.");

        Console.WriteLine($"Source data: {sourceData.Length} bytes");
        Console.WriteLine($"Source: {System.Text.Encoding.UTF8.GetString(sourceData)}\n");

        // Encoder
        const int symbolSize = 16;
        var encoder = new RaptorQEncoder(sourceData, symbolSize);
        int K = encoder.SourceSymbolCount;

        Console.WriteLine($"RaptorQ Configuration:");
        Console.WriteLine($"  Symbol size: {symbolSize} bytes");
        Console.WriteLine($"  Source symbols (K): {K}");
        Console.WriteLine($"  Repair symbols generated: {K + 5}");

        // Generate symbols
        var sw = Stopwatch.StartNew();
        var symbols = encoder.GenerateSymbols(K + 5);
        sw.Stop();
        Console.WriteLine($"  Encoding time: {sw.ElapsedMilliseconds} ms\n");

        // Simulate packet loss (20%)
        Console.WriteLine("Simulating network transmission with 20% packet loss...");
        var simulator = new PacketSimulator(lossRate: 0.20);
        var receivedSymbols = simulator.SimulateLoss(symbols).ToList();

        Console.WriteLine($"Transmitted symbols: {symbols.Count()}");
        Console.WriteLine($"Received symbols: {receivedSymbols.Count}");
        Console.WriteLine($"Loss rate: {(1.0 - (double)receivedSymbols.Count / symbols.Count()) * 100:F1}%\n");

        // Decoder
        Console.WriteLine("Decoding with received symbols...");
        var decoder = new RaptorQDecoder(K, symbolSize);

        sw.Restart();
        foreach (var symbol in receivedSymbols)
        {
            decoder.AddSymbol(symbol);
            if (decoder.CanDecode)
                break;
        }
        sw.Stop();

        if (!decoder.CanDecode)
        {
            Console.WriteLine("ERROR: Not enough symbols for decoding!");
            return;
        }

        byte[]? recovered = null;
        try
        {
            recovered = decoder.Decode();
            sw.Stop();
            Console.WriteLine($"  Decoding time: {sw.ElapsedMilliseconds} ms");
        }
        catch (Exception ex)
        {
            Console.WriteLine($"ERROR: Decoding failed: {ex.Message}");
            return;
        }

        // Verify
        Console.WriteLine("\nVerification:");
        bool match = sourceData.SequenceEqual(recovered ?? Array.Empty<byte>());
        Console.WriteLine($"  Data matches: {(match ? "YES ✓" : "NO ✗")}");

        if (match)
        {
            Console.WriteLine($"  Recovered: {System.Text.Encoding.UTF8.GetString(recovered!)}");
            Console.WriteLine("\nSUCCESS: File recovered successfully despite packet loss!");
        }
        else
        {
            Console.WriteLine("FAILURE: Recovered data doesn't match original");
        }
    }

    static void RunBenchmark()
    {
        Console.WriteLine("Benchmark: RaptorQ Performance\n");

        int[] fileSizes = { 1024, 10240, 102400 };  // 1 KB, 10 KB, 100 KB
        const int symbolSize = 16;

        foreach (int fileSize in fileSizes)
        {
            Console.WriteLine($"\nFile size: {fileSize / 1024} KB");

            // Create random data
            var random = new Random(42);
            byte[] sourceData = new byte[fileSize];
            random.NextBytes(sourceData);

            // Encode
            var encoder = new RaptorQEncoder(sourceData, symbolSize);
            int K = encoder.SourceSymbolCount;

            var sw = Stopwatch.StartNew();
            var symbols = encoder.GenerateSymbols(K + 10).ToList();
            sw.Stop();

            Console.WriteLine($"  Source symbols: {K}");
            Console.WriteLine($"  Encoding time: {sw.ElapsedMilliseconds} ms");
            Console.WriteLine($"  Encoding rate: {fileSize / (sw.Elapsed.TotalSeconds * 1e6):F2} MB/s");

            // Simulate loss and decode
            var simulator = new PacketSimulator(lossRate: 0.15);
            var received = simulator.SimulateLoss(symbols);

            var decoder = new RaptorQDecoder(K, symbolSize);
            foreach (var symbol in received)
            {
                decoder.AddSymbol(symbol);
                if (decoder.CanDecode) break;
            }

            sw.Restart();
            var recovered = decoder.Decode();
            sw.Stop();

            Console.WriteLine($"  Decoding time: {sw.ElapsedMilliseconds} ms");
            Console.WriteLine($"  Decoding rate: {fileSize / (sw.Elapsed.TotalSeconds * 1e6):F2} MB/s");

            double overhead = (double)(symbols.Count() - K) / K * 100;
            Console.WriteLine($"  Overhead: {overhead:F1}%");
            Console.WriteLine($"  Verified: {sourceData.SequenceEqual(recovered)}");
        }
    }
}
