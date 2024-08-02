using BehaviorBlackboard.Engine;

namespace BehaviorBlackboard;

public class KnowledgeSourceHasEmail : IKnowledgeSource
{
    public void HandleChange(IBlackboard blackboard, IEventData data)
    {
        if (data.Key.Equals("email", StringComparison.OrdinalIgnoreCase))
        {
            blackboard.Set(this, "ready", true);
        }
    }
}
