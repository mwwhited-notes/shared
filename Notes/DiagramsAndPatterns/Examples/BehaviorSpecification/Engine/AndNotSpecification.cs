namespace BehaviorSpecification.Engine;

public class AndNotSpecification<T>(ISpecification<T> left, ISpecification<T> right) : CompositeSpecification<T>
{
    private readonly ISpecification<T> _left = left;
    private readonly ISpecification<T> _right = right;

    public override bool IsSatisfiedBy(T candidate) =>
        _left.IsSatisfiedBy(candidate) && !_right.IsSatisfiedBy(candidate);
}
