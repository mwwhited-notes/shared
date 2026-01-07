
## Summary

There should be a common query definition for search, filter, sort and page.

## Definitions

- Search: global query parameter that will be used to filter across all/selected properties
  - properties may be excluded or explicitly included
- Filter: predicated rules may be provided per property
  - example operators may include: equal to, not equal, greater than, less than, greater than or equal, less than or equal, not null, is null, in set, not in set
- Order: per field and direction
- Paging: row count return is optional, page index is 1 based, page length included for offset

## Open Questions

- How should weighted parameters be handled.  (ie: vectors/embeddings, re-ranking)
- How to handle predicate collections like AND/OR chains or group predicates
- Should json property names be abbreviated

## Example Messages

### Request

```json
{
    "search" : "[search term]",
    "filter": [
        { "field": "[fieldName]", "operator": "[operator]", "value":"[value]" },
        { "field": "[fieldName]", "operator": "[operator]", "value":"[value]" },
        { "field": "[fieldName]", "operator": "[operator]", "value":"[value]" }
    ],
    "orderBy": [
        {"field": "[fieldName]", "direction": "[asc|desc]"}
    ],
    "page": {
        "excludeCount": "[true|false]",
        "page": "[int]",
        "length": "[int]"
    }
}
```

### Response

```json
{
    "rows": [{...}],
    "page": {
        "page": "[int]",
        "length": "[int]",
        "count": "[int]"
    }
    "messages" :[
        { "level": "[info|warn|error]", "message": "[string]"},
    ]
}
```
