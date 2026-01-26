# Repository Sync Verification - Quick Reference

## What It Does

Automatically verifies that:
- ✅ Version numbers match across all files (build script, README, release docs)
- ✅ All download links in README point to existing files
- ✅ Release files are up-to-date (not older than README)
- ✅ Content is consistent between README and release files
- ✅ Git status is clean and in sync with remote

## Quick Commands

```bash
# Run verification manually
python3 scripts/verify-sync.py

# Quiet mode (CI/CD friendly)
python3 scripts/verify-sync.py --quiet

# Check remote sync status
python3 scripts/verify-sync.py --check-remote

# Auto-fix issues
python3 scripts/verify-sync.py --auto-fix
```

## Automatic Hooks

The verification runs automatically:
- **After commit** (post-commit hook)
- **After pull** (post-merge hook)  
- **Before push** (pre-push hook - can block push)

## After Commit and Push

The hooks will automatically verify sync. If issues are found:
1. Fix the issues manually, OR
2. Run `python3 scripts/build-releases.py` to regenerate files, OR
3. Use `--auto-fix` flag to auto-regenerate

## Common Fixes

| Issue | Fix |
|-------|-----|
| Version mismatch | Update `VERSION` in `scripts/build-releases.py` |
| Missing files | Run `python3 scripts/build-releases.py` |
| Stale files | Run `python3 scripts/build-releases.py` |
| Uncommitted changes | `git add . && git commit` |

## Exit Codes

- `0` = All checks passed ✅
- `1` = Issues found ⚠️

Perfect for CI/CD integration!
