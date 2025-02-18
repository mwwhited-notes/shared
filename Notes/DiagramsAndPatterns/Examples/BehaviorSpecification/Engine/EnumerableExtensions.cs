using System.Linq.Expressions;

namespace BehaviorSpecification.Engine;

public static class For<T>
{
    public static ISpecification<T> Rule(Expression<Func<T, bool>> expression) =>
        new LinqSpecification<T>(expression);
}

public static class EnumerableExtensions
{
    public static ISpecification<T> Has<T>(this IEnumerable<T> items) =>
         new InSetSpecification<T>(items);
}
