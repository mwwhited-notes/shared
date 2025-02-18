using System.Text;

namespace BehaviorBlackboard;

public static class DictionaryExtensions
{
    public static string WriteOut<K, V>(this IReadOnlyDictionary<K, V> dict) =>
        dict.Aggregate(
            new StringBuilder(),
            (sb, item) => sb.Append($"\t{item.Key}= {item.Value}").AppendLine(),
            sb => sb.ToString());
}
