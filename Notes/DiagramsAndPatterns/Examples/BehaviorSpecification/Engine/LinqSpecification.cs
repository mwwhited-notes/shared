using System.Linq.Expressions;

namespace BehaviorSpecification.Engine;

public class LinqSpecification<T>(
    Expression<Func<T, bool>> Expression
    ) : CompositeSpecification<T>
{
    public override bool IsSatisfiedBy(T candidate) => Expression.Compile()(candidate);
}
