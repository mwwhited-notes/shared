namespace BehaviorSpecification;

public record InvoiceModel
{
    public required DateTimeOffset DueDate { get; init; }
    public required bool Sent { get; init; }
    public required string AccountReference { get; init; }
}
