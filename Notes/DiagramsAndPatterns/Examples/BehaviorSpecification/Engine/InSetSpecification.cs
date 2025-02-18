namespace BehaviorSpecification.Engine;

public class InSetSpecification<T>(IEnumerable<T> set) :
    LinqSpecification<T>(model => set.Any(i => i != null && i.Equals(model)))
{
}