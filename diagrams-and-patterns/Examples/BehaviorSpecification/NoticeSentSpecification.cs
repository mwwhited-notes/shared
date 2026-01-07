using BehaviorSpecification.Engine;
using System.Linq.Expressions;

namespace BehaviorSpecification;

public class NoticeSentSpecification : LinqSpecification<InvoiceModel>
{
    public NoticeSentSpecification() : base(model => model.Sent)
    {
    }
}
