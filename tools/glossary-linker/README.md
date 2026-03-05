# Glossary Linker

**Status**: Planned — Phase 1 scope  
**Phase 0 state**: Directory placeholder only.

This tool will automatically link occurrences of glossary terms in project
documents to their definitions in `content/glossary.md`.

## Planned Features

- Scan all `.md` files in `principles/`, `governance/`, `content/`
- Identify unlinked uses of terms defined in `content/glossary.md`
- Output a report of suggested link insertions (non-destructive)
- Optional: apply links automatically with `--apply` flag

## Implementation Target

Phase 1 — once the glossary grows to 20+ terms and consistent link
coverage becomes meaningful.

## Contributing

If you want to help build this tool, open an issue labelled `tooling`
or post in the Technology working group discussions.
