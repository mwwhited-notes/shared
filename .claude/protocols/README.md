# Documentation Protocols Index

This directory contains protocols for documenting equipment, projects, and inventory in this repository.

## Available Protocols

### Projects & Documentation

| Protocol | Purpose | Key Sections |
|----------|---------|--------------|
| [PROJECTS_PROTOCOL.md](PROJECTS_PROTOCOL.md) | Document active projects in projects/ directory | README format, build logs, parts lists, status tracking |
| [PROJECT_REVIEW_PROTOCOL.md](PROJECT_REVIEW_PROTOCOL.md) | Periodic inventory review and maintenance | Full review workflow, quick sync, cross-reference checks |

### Maintenance & Performance

| Protocol | Purpose | Key Sections |
|----------|---------|--------------|
| [BOOKS_PROTOCOL.md](BOOKS_PROTOCOL.md) | Maintain books.md inventory | Technical books, software/hardware references |
| [CHANGELOG_PROTOCOL.md](CHANGELOG_PROTOCOL.md) | Document repository changes in changes/ directory | Session/topic-based changelogs, file organization, change tracking |
| [CLAUDE_MD_MAINTENANCE_PROTOCOL.md](CLAUDE_MD_MAINTENANCE_PROTOCOL.md) | Keep CLAUDE.md concise for performance | Content structure, refactoring process, length guidelines |
| [INDEX_PROTOCOL.md](INDEX_PROTOCOL.md) | Creating and maintaining directory indexes | Index structure, quick-reference tables, organization |
| [TECHNICAL-RESEARCH-PROTOCOL.md](TECHNICAL-RESEARCH-PROTOCOL.md) | Document comprehensive research projects | Standards, RFCs, bibliography, implementation guides |
| [TODO_MD_ARCHIVAL_PROTOCOL.md](TODO_MD_ARCHIVAL_PROTOCOL.md) | Archive completed tasks to changes/ directory | Archival triggers, file naming, archive format, cleanup process |

## Quick Reference

### When Working on Projects

**Are you...**
- Starting a new build project? → [PROJECTS_PROTOCOL.md](PROJECTS_PROTOCOL.md)
- Doing quarterly inventory review? → [PROJECT_REVIEW_PROTOCOL.md](PROJECT_REVIEW_PROTOCOL.md)
- Creating comprehensive research/standards documentation? → [TECHNICAL-RESEARCH-PROTOCOL.md](TECHNICAL-RESEARCH-PROTOCOL.md)

### When Managing Documentation

**Are you...**
- CLAUDE.md getting too long (>600 lines)? → [CLAUDE_MD_MAINTENANCE_PROTOCOL.md](CLAUDE_MD_MAINTENANCE_PROTOCOL.md)
- TODO.md has >10 completed tasks? → [TODO_MD_ARCHIVAL_PROTOCOL.md](TODO_MD_ARCHIVAL_PROTOCOL.md)
- Major topic/milestone completed? → [TODO_MD_ARCHIVAL_PROTOCOL.md](TODO_MD_ARCHIVAL_PROTOCOL.md)
- User requests "create a changelog"? → [CHANGELOG_PROTOCOL.md](CHANGELOG_PROTOCOL.md)
- Performance issues from large context? → Check both maintenance protocols

## Protocol Maintenance

### Version History

All protocols should include:
```markdown
---

*Protocol Version: X.Y*
*Last Updated: Month YYYY*
```

### When to Update Protocols

Update protocols when:
- Adding new inventory categories
- Changing documentation standards
- Improving templates or workflows
- Clarifying ambiguous sections
- Adding new cross-reference patterns

### Protocol Consistency

All protocols follow these common patterns:
1. **Overview** - What the protocol covers
2. **When to Use** - Specific triggers for using the protocol
3. **Directory Structure** - File organization
4. **Templates** - README/documentation formats
5. **Cross-References** - Links to related inventories
6. **Common Mistakes** - What to avoid
7. **Examples** - Real-world usage

## Cross-Protocol Dependencies

### Project Relationships

```
projects/project-ideas.md (backlog)
    ↓
projects/ (active implementation)
    ↓
workshop-capabilities.md (completed capabilities)
```

Root repository projects are self-contained with their own documentation, build logs, and status tracking.

Equipment inventories and tools/components are now maintained in Personal repository. See PERSONAL-PROTOCOL.md for requesting this data.

## Common Cross-References (Root Repository)

### From Projects to Projects
```markdown
## Related Projects

- [Project Name](../../projects/project-name/) - Brief description
```

### From Research to Projects
```markdown
## Related Projects Using This Research

- [Project Name](../../projects/project-name/) - How this research applies
```

**Note:** Equipment cross-references are now maintained in Personal repository. Use personal-request-*.md files to request equipment inventory when needed in root documentation.

## Finding the Right Protocol

### Decision Tree

```
What are you doing?
│
├─ Starting a new build project?
│  └─ YES → PROJECTS_PROTOCOL.md
│
├─ Doing quarterly inventory review?
│  └─ YES → PROJECT_REVIEW_PROTOCOL.md
│
├─ Creating comprehensive research/standards documentation?
│  └─ YES → TECHNICAL-RESEARCH-PROTOCOL.md
│
├─ Creating/updating directory indexes?
│  └─ YES → INDEX_PROTOCOL.md
│
├─ Is CLAUDE.md getting too long (>600 lines)?
│  └─ YES → CLAUDE_MD_MAINTENANCE_PROTOCOL.md
│
├─ Do you have >10 completed tasks in TODO.md?
│  └─ YES → TODO_MD_ARCHIVAL_PROTOCOL.md
│
├─ Need to document a completed milestone/session?
│  └─ YES → CHANGELOG_PROTOCOL.md
│
└─ Maintaining technical book inventory (books.md)?
   └─ YES → BOOKS_PROTOCOL.md
```

**Note:** Equipment collection protocols (cameras, devices, tools, test equipment, etc.) are now maintained in the Personal repository. See PERSONAL-PROTOCOL.md in root for requesting data from Personal collections.

## Getting Started

1. **Identify what you're documenting** - Use decision tree above
2. **Read the relevant protocol** - Follow the templates and guidelines
3. **Check existing examples** - Look at similar items already documented
4. **Cross-reference appropriately** - Link related equipment/projects
5. **Update last-modified dates** - Keep timestamps current

## Questions or Improvements

If you encounter:
- **Unclear guidance** → Update protocol with clarification
- **Missing category** → Add to protocol or create new protocol
- **Conflicting protocols** → Resolve and document the decision
- **New use case** → Add example to protocol

## Protocol Index Maintenance

This README serves as the master index for all 9 documentation protocols in root (10 additional collection protocols are maintained in Personal repository). It is updated whenever:
- A new protocol is created
- An existing protocol version changes
- Protocol purposes are clarified or reorganized

### Version Tracking

| Protocol | Purpose | Current Version | Last Updated |
|----------|---------|-----------------|--------------|
| BOOKS_PROTOCOL.md | Technical books | 1.0 | Jan 2026 |
| CHANGELOG_PROTOCOL.md | Change tracking | 1.0 | Jan 2026 |
| CLAUDE_MD_MAINTENANCE_PROTOCOL.md | CLAUDE.md upkeep | 1.0 | Jan 2026 |
| INDEX_PROTOCOL.md | Creating indexes | 1.2 | Jan 2026 |
| PROJECTS_PROTOCOL.md | Active projects | 1.2 | Jan 2026 |
| PROJECT_REVIEW_PROTOCOL.md | Quarterly reviews | 1.1 | Jan 2026 |
| TECHNICAL-RESEARCH-PROTOCOL.md | Research projects | 1.3 | Jan 2026 |
| TODO_MD_ARCHIVAL_PROTOCOL.md | Task archival | 1.0 | Jan 2026 |
| README.md | This index | 1.6 | Jan 2026 |

---

*Protocol Index Version: 1.6*
*Last Updated: 2026-01-17*

### Changelog

**v1.6 (2026-01-17) - Repository Reorganization**
- Removed 10 collection protocols (moved to Personal repository):
  - CAMERA_COLLECTION_PROTOCOL.md
  - DEVICE_LAB_PROTOCOL.md
  - EQUIPMENT_DOCUMENTATION_PROTOCOL.md
  - EXPANSION_BOARDS_DOCUMENTATION_PROTOCOL.md
  - HOBBY_COLLECTION_PROTOCOL.md
  - ONLINE_SHOPPING_PROTOCOL.md
  - PROGRAMMABLE_DEVICES_DOCUMENTATION_PROTOCOL.md
  - SPORTS_COLLECTION_PROTOCOL.md
  - TOOLS_AND_COMPONENTS_PROTOCOL.md
  - VINTAGE_COMPUTERS_DOCUMENTATION_PROTOCOL.md
- Reduced index to 9 root protocols
- Updated decision tree to reflect available protocols only
- Added note about Personal repository protocols
- Root repository now focuses on projects, research, and maintenance
- Version tracking table updated to show remaining protocols

**v1.5 (2026-01-17) - New Collection Protocols**
- Added HOBBY_COLLECTION_PROTOCOL.md (v1.0) for leathercraft, sewing, jewelry making
- Added SPORTS_COLLECTION_PROTOCOL.md (v1.0) for water sports, biking, camping, fitness
- Updated TOOLS_AND_COMPONENTS_PROTOCOL.md to v1.1 for component kit organization
- Updated EQUIPMENT_DOCUMENTATION_PROTOCOL.md to v1.1 for power backup and cooling systems
- Updated ONLINE_SHOPPING_PROTOCOL.md to v1.1 for AliExpress archive standards
- Added new decision tree branches for hobby and sports collections

**v1.4 (2026-01-16) - Protocol Updates**
- Added version tracking table for all 17 protocols
- Added INDEX_PROTOCOL.md (v1.1) to maintain all directory indexes
- Updated PROJECTS_PROTOCOL.md to v1.2 with TODO.md integration
- Updated INDEX_PROTOCOL.md to v1.1 with TODO.md integration
- Clarified protocol maintenance procedures
- Made TODO.md tracking a standard practice for all work discovery

**v1.3 (2026-01-07)**
- Added cross-protocol dependencies section
- Expanded decision tree examples
- Added protocol consistency standards
- Clarified cross-reference patterns
