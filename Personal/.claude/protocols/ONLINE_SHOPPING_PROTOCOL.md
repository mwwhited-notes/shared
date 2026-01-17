# Online Shopping Documentation Protocol

Standard procedure for tracking experiences with online retailers and sellers.

---

## Overview

This protocol ensures consistent documentation of online shopping experiences, particularly for electronics, test equipment, and components. The goal is to maintain a reference of reliable (and unreliable) sellers.

---

## Information to Capture

### For Each Purchase

| Field | Description |
|-------|-------------|
| Seller/Retailer | Name as shown on platform |
| Platform | eBay, Amazon, AliExpress, direct, etc. |
| Store URL | Direct link to seller's store |
| Item Purchased | What was bought |
| Date | When purchased |
| Price | Total including shipping |
| Condition Listed | How item was described (new, used, refurbished) |
| Condition Received | Actual condition on arrival |

### Seller Evaluation

| Criteria | Rating Scale |
|----------|--------------|
| Photo Accuracy | Accurate / Misleading / Deceptive |
| Item Description | Accurate / Incomplete / Misleading |
| Packaging Quality | Excellent / Good / Fair / Poor / Unacceptable |
| Shipping Speed | As expected / Delayed |
| Communication | Responsive / Slow / None needed |
| Would Buy Again | Yes / With caution / No |

### Red Flags to Document

- Deceptive photos (hiding damage, wrong angles)
- Stickers/labels added to hide defects
- Inadequate packaging materials
- Improvised shipping containers
- Item not as described
- Missing accessories
- Signs of prior repair or modification

---

## Default Assumptions

- **Would Buy Again:** Assume "Yes" unless the user explicitly states otherwise
- If seller is added to Blacklist, "Would Buy Again" is automatically "No"

---

## Conversation Triggers

When the user mentions any of the following, update `ShoppingOnline.md`:

- "I bought from..." or "I ordered from..."
- "The seller..." or "The package..."
- Feedback about shipping, packaging, or seller behavior
- Store links or seller names
- Pricing information for purchases
- Recommendations for or against sellers

---

## File Structure

### Main Documentation

**Primary file:** `ShoppingOnline.md`

```markdown
# Online Shopping - Seller Notes

## Direct Retailer Orders

### Amazon
- References to archived invoice files by year

### eBay Sellers
[Quick reference table]

## Seller Details
[Expanded entries per seller]

## Other Online Retailers
[Non-eBay/Amazon sources]

## Blacklist
[Sellers to avoid - with reasons]

## Notes
[General shopping tips]
```

### Invoice Archiving

Detailed order invoices are organized in `.invoices/` directory by retailer and year:

**Pattern:** `.invoices/{retailer}-{year}.md`

**Examples:**
- `.invoices/amazon-2019.md` - All Amazon orders from 2019
- `.invoices/amazon-2020.md` - All Amazon orders from 2020
- `.invoices/aliexpress-2022.md` - All AliExpress orders from 2022 through 2026
- `.invoices/mouser-2021.md` - All Mouser orders from 2021

**Each invoice file contains:**
- Complete order numbers and dates
- Seller/platform information
- Item descriptions with quantities
- Pricing (item price, shipping, tax, total)
- Condition (new/used/refurbished)
- Shipping method and speed
- Seller notes and feedback

**ShoppingOnline.md references** point to these archive files rather than repeating full order details, keeping the main file focused on seller evaluation and retail strategy.

---

## Adding a New Seller Entry

### Quick Table Entry

```markdown
| Seller Name | Rating | Packaging | Notes |
```

Ratings: Excellent / Good / Fair / Poor / Avoid

### Detailed Entry Template

```markdown
### [Seller Name]

- **Platform:** [eBay/Amazon/etc.]
- **Store URL:** [link]
- **Purchases:**
  - [Item] ([Date]) - $[price]
- **Photo Accuracy:** [Accurate/Misleading/Deceptive]
- **Packaging Quality:** [rating] - [details]
- **Item Accuracy:** [Accurate/Misleading] - [details]
- **Red Flags:** [list any issues]
- **Would Buy Again:** [Yes/With caution/No]
- **Notes:** [additional comments]
```

---

## Updating Existing Entries

When new information is received about a known seller:

1. Add new purchases to their purchase history
2. Update ratings if experience differs significantly
3. Add new red flags or positive notes
4. Update "Would Buy Again" recommendation if changed

---

## Invoice Organization Process

### When to Archive Orders

Create a new invoice archive file (`.invoices/{retailer}-{year}.md`) when:

1. A retailer has accumulated multiple orders (5+) from a single year
2. ShoppingOnline.md becomes difficult to navigate due to order volume
3. You want to preserve complete order details while keeping ShoppingOnline.md focused on seller evaluation

### How to Archive Orders

1. **Create new file:** `.invoices/{retailer}-{year}.md`
2. **Copy full order details** (order numbers, dates, items, pricing, notes) from ShoppingOnline.md
3. **Update ShoppingOnline.md** to replace order details with a summary table or reference links pointing to the archive file
4. **Include summary metadata** at the top of archive file:
   - Retailer name
   - Year covered
   - Number of orders
   - Total spending
   - Date range

### Archive File Template

```markdown
# [Retailer] Orders - [Year]

**Summary:**
- Period: [YYYY-MM-DD] to [YYYY-MM-DD]
- Total Orders: [#]
- Total Spent: $[amount]

---

## Order Details

### Order #[number] - [Date]
- **Items:** [description]
- **Price:** $[item] + $[shipping] shipping + $[tax] tax = **$[total]**
- **Condition:** [new/used/refurbished]
- **Shipping:** [method]
- **Notes:** [any relevant details]
```

### AliExpress Invoice Archive Format

AliExpress invoices are archived with the following specific format:

**File naming:** `.invoices/aliexpress-{YYYY}.md` (combined multi-year archives are acceptable if period is large)

**Archive structure:**
```markdown
# AliExpress Orders - [Year Range]

**Summary:**
- Orders: [#] total across years
- Date Range: YYYY-MM-DD to YYYY-MM-DD
- Total Spent: $[amount]
- Quality Alerts: [List any known issues - counterfeits, defects, etc.]

---

## Orders by Year

### [Year]

| Order ID | Date | Store | Item(s) | Qty | Price | Status | Notes |
|----------|------|-------|---------|-----|-------|--------|-------|
| [...] | YYYY-MM-DD | [Store Name] | [Description] | [#] | $[amount] | [Shipped/Delivered/Awaiting] | [Any notes] |
```

**Special handling for AliExpress:**
1. **Quality alerts** - Document suspected counterfeits or quality issues upfront
2. **Incomplete descriptions** - Note items lacking itemized details; use order IDs for reference
3. **Shipping delays** - Track expected vs. actual delivery status
4. **Store/seller tracking** - Include store names for future reference on repeat orders
5. **Duplicate orders** - Note if same item was ordered multiple times on same date
6. **Multi-package orders** - Track orders split across multiple shipments

**Example quality alert:**
```markdown
**Quality Alerts:**
- 2023-01-17 (Shop2982020 Store): AD633 chips - confirmed counterfeit (documented in ShoppingOnline.md blacklist)
- 2026-01-14: 3 HDMI KVM Extenders ordered same day - verify if intentional
```

---

## Blacklist Criteria

Move seller to Blacklist section if:

- Deceptive photos or descriptions
- Intentionally hiding damage
- Repeated poor packaging
- Failure to resolve issues
- Suspected counterfeits

---

## Version History

*Protocol Version: 1.1*
*Last Updated: 2026-01-17*

### v1.1 (2026-01-17) - AliExpress Invoice Archive Standards
- Added specific format documentation for AliExpress invoice archives
- Documented special handling for AliExpress orders (quality alerts, duplicate tracking, shipping delays)
- Added example quality alert format for counterfeited components
- Expanded invoice archiving section with AliExpress-specific considerations
- Updated examples to include AliExpress archive files

### v1.0 (2026-01-XX)
- Initial protocol documentation
- Added invoice archiving documentation with pattern `.invoices/{retailer}-{year}.md`
- Defined seller evaluation criteria and blacklist standards
