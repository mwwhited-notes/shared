namespace BehaviorSpecification.Engine;

public class NotSpecification<T>(ISpecification<T> other) : CompositeSpecification<T>
{
    private readonly ISpecification<T> _other = other;

    public override bool IsSatisfiedBy(T candidate) => !_other.IsSatisfiedBy(candidate);
}