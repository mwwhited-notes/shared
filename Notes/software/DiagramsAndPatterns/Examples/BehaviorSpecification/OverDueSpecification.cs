using BehaviorSpecification.Engine;
using System.Linq.Expressions;

namespace BehaviorSpecification;

public class OverDueSpecification(DateTimeOffset CurrentDate) :
    LinqSpecification<InvoiceModel>(model => model.DueDate <= CurrentDate)
{
}
