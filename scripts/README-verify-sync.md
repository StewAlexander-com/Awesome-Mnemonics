# Repository Sync Verification

The `verify-sync.py` script ensures that README.md, release documents, and version numbers are all in sync between local and remote repositories.

## Features

- **Version Consistency**: Verifies version numbers match across:
  - Build script (`scripts/build-releases.py`)
  - README.md release section
  - Generated release markdown files

- **Download Links**: Checks that all download links in README.md point to existing files

- **File Freshness**: Ensures release files are up-to-date relative to README.md

- **Content Consistency**: Validates that release file content matches README structure

- **Git Status**: Checks for uncommitted changes and remote sync status

## Usage

### Manual Verification

```bash
# Basic verification
python3 scripts/verify-sync.py

# Quiet mode (only show errors/warnings)
python3 scripts/verify-sync.py --quiet

# Check remote repository sync
python3 scripts/verify-sync.py --check-remote

# Auto-fix issues (runs build script automatically)
python3 scripts/verify-sync.py --auto-fix
```

### Automatic Verification (Git Hooks)

The verification script is automatically run via git hooks:

- **post-commit**: Runs after each commit to verify sync
- **post-merge**: Runs after pulling changes to verify sync
- **pre-push**: Runs before pushing (can block push if issues found)

Hooks are located in `.git/hooks/` and are automatically installed.

### After Commit and Push

The hooks will automatically run verification. You can also manually run:

```bash
# After committing
python3 scripts/verify-sync.py

# After pushing
python3 scripts/verify-sync.py --check-remote
```

## Output

The script provides color-coded output:

- ✓ **Green**: Passed checks
- ℹ **Blue**: Informational messages
- ⚠ **Yellow**: Warnings (non-critical issues)
- ✗ **Red**: Errors (critical issues)

## Handling Discrepancies

When issues are found, the script will prompt you to:

1. **Continue anyway** - Ignore the issues
2. **Run build script** - Automatically regenerate release files
3. **Exit and fix manually** - Stop and fix issues yourself

In non-interactive mode (e.g., git hooks), the script will exit with an error code if issues are found.

## Common Issues

### Version Mismatch
- **Cause**: Version number updated in one place but not others
- **Fix**: Update `VERSION` in `scripts/build-releases.py` and run build script

### Missing Download Files
- **Cause**: README references files that don't exist
- **Fix**: Run `python3 scripts/build-releases.py` to generate missing files

### Stale Release Files
- **Cause**: Release files older than README.md
- **Fix**: Run build script to regenerate: `python3 scripts/build-releases.py`

### Uncommitted Changes
- **Cause**: Modified files not committed
- **Fix**: Commit or stash changes: `git add . && git commit` or `git stash`

## Integration with CI/CD

The script can be integrated into CI/CD pipelines:

```yaml
# Example GitHub Actions step
- name: Verify Repository Sync
  run: python3 scripts/verify-sync.py --quiet --check-remote
```

Exit code 0 = all checks passed, 1 = issues found.
