using BehaviorBlackboard.Engine;
using System.Reflection;
using System.Runtime.CompilerServices;
using System.Security.Cryptography;

namespace BehaviorBlackboard;

internal class Program
{
    static void Main(string[] args)
    {
        var control = new Control(new Blackboard())
            .Add(new KnowledgeSourceHasFullName())
            .Add(new KnowledgeSourceHasEmail())
            .Snapshot(out var empty)
            .Post("first", "Matt")
            .Snapshot(out var withFirst)
            .Post("last", "Whited")
            .Snapshot(out var withLast)
            ;

        Console.WriteLine($"{nameof(empty)}: {empty.WriteOut()}");
        Console.WriteLine($"{nameof(withFirst)}: {withFirst.WriteOut()}");
        Console.WriteLine($"{nameof(withLast)}: {withLast.WriteOut()}");
    }
}
