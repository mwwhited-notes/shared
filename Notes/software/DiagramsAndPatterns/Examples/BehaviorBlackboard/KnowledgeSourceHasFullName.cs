using BehaviorBlackboard.Engine;

namespace BehaviorBlackboard;

public class KnowledgeSourceHasFullName : IKnowledgeSource
{
    public void HandleChange(IBlackboard blackboard, IEventData data)
    {
        if (data.Key.Equals("first", StringComparison.OrdinalIgnoreCase) ||
            data.Key.Equals("last", StringComparison.OrdinalIgnoreCase))
        {
            var first = blackboard["first"] as string;
            var last = blackboard["last"] as string;

            if (!string.IsNullOrWhiteSpace(first) && !string.IsNullOrWhiteSpace(last))
            {
                blackboard.Set(this, "email", $"{first}.{last}@MyDomain.com");
            }
        }
    }
}
