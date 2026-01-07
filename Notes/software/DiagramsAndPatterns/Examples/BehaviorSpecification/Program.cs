using BehaviorSpecification.Engine;
using System.Dynamic;

namespace BehaviorSpecification;

internal class Program
{
    static void Main(string[] args)
    {
        var invoices = new List<InvoiceModel>()
        {
            new (){ DueDate = DateTime.Now.AddDays(1), Sent = false, AccountReference="a"},
            new (){ DueDate = DateTime.Now.AddDays(-1), Sent = false, AccountReference="b"},
            new (){ DueDate = DateTime.Now.AddDays(1), Sent = true, AccountReference="c"},
            new (){ DueDate = DateTime.Now.AddDays(-1), Sent = true, AccountReference="d"},
        };
        var collections = new List<InvoiceModel>();

        //define rules

        var overDue = new OverDueSpecification(DateTimeOffset.Now);
        var noticeSent = new NoticeSentSpecification();

        var sendToCollectionsRule = overDue.And(noticeSent).And(collections.Has().Not());
        var sendNotificationRule = overDue.And(noticeSent.Not()).And(collections.Has().Not());

        //use rules

        var sentToCollections = invoices.Where(sendToCollectionsRule.IsSatisfiedBy).ToList();
        foreach (var invoice in sentToCollections)
        {
            collections.Add(invoice);
            Console.WriteLine($"Send to collections: {invoice}");
        }

        var sendNotification = invoices.Where(sendNotificationRule.IsSatisfiedBy).ToList();
        foreach (var invoice in sendNotification)
        {
            Console.WriteLine($"Send Notification: {invoice}");
        }

        //check

        foreach (var invoice in collections)
        {
            Console.WriteLine($"In Collections: {invoice}");
        }
    }
}
