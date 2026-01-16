using System;
using System.Collections.Generic;
using System.Linq;

/// <summary>
/// Network packet simulator for testing erasure recovery
/// </summary>
public class PacketSimulator
{
    private readonly double _lossRate;  // 0.0 to 1.0
    private readonly Random _random;
    private readonly bool _reorderPackets;

    /// <summary>
    /// Create a packet simulator
    /// </summary>
    /// <param name="lossRate">Packet loss rate (0.0 = no loss, 1.0 = all loss)</param>
    /// <param name="reorderPackets">Whether to randomly reorder packets</param>
    public PacketSimulator(double lossRate, bool reorderPackets = false)
    {
        if (lossRate < 0.0 || lossRate > 1.0)
            throw new ArgumentOutOfRangeException(nameof(lossRate));

        _lossRate = lossRate;
        _reorderPackets = reorderPackets;
        _random = new Random();
    }

    /// <summary>
    /// Simulate transmission with packet loss and optional reordering
    /// </summary>
    public IEnumerable<FountainSymbol> SimulateLoss(IEnumerable<FountainSymbol> symbols)
    {
        var symbolList = symbols.ToList();
        var received = new List<FountainSymbol>();

        // Apply packet loss
        foreach (var symbol in symbolList)
        {
            if (_random.NextDouble() > _lossRate)
            {
                received.Add(symbol.Clone());
            }
        }

        // Apply reordering
        if (_reorderPackets && received.Count > 1)
        {
            received = ShuffleList(received);
        }

        return received;
    }

    /// <summary>
    /// Simulate transmission with specific loss pattern
    /// </summary>
    public IEnumerable<FountainSymbol> SimulateLossPattern(
        IEnumerable<FountainSymbol> symbols,
        int[] lossIndices)
    {
        var symbolList = symbols.ToList();
        var lossSet = new HashSet<int>(lossIndices);
        var received = new List<FountainSymbol>();

        for (int i = 0; i < symbolList.Count; i++)
        {
            if (!lossSet.Contains(i))
            {
                received.Add(symbolList[i].Clone());
            }
        }

        return received;
    }

    /// <summary>
    /// Shuffle list using Fisher-Yates algorithm
    /// </summary>
    private List<T> ShuffleList<T>(List<T> list)
    {
        var shuffled = new List<T>(list);

        for (int i = shuffled.Count - 1; i > 0; i--)
        {
            int randomIndex = _random.Next(i + 1);

            // Swap
            (shuffled[randomIndex], shuffled[i]) = (shuffled[i], shuffled[randomIndex]);
        }

        return shuffled;
    }

    /// <summary>
    /// Get statistics about a transmission
    /// </summary>
    public static TransmissionStats GetStats(
        IEnumerable<FountainSymbol> sent,
        IEnumerable<FountainSymbol> received)
    {
        var sentList = sent.ToList();
        var receivedList = received.ToList();

        int sentCount = sentList.Count;
        int receivedCount = receivedList.Count;
        int lossCount = sentCount - receivedCount;
        double lossRate = sentCount > 0 ? (double)lossCount / sentCount : 0;

        return new TransmissionStats
        {
            SentCount = sentCount,
            ReceivedCount = receivedCount,
            LossCount = lossCount,
            LossRate = lossRate
        };
    }
}

/// <summary>
/// Statistics about a simulated transmission
/// </summary>
public class TransmissionStats
{
    public int SentCount { get; set; }
    public int ReceivedCount { get; set; }
    public int LossCount { get; set; }
    public double LossRate { get; set; }

    public override string ToString()
    {
        return $"Sent: {SentCount}, Received: {ReceivedCount}, Loss: {LossCount} ({LossRate:P1})";
    }
}
