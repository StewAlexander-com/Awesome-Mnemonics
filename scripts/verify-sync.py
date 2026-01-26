#!/usr/bin/env python3
"""
Verification script to ensure README.md, release documents, and versions are in sync
between local and remote repositories.

Usage:
    python3 scripts/verify-sync.py [--auto-fix] [--check-remote]
"""
import re
import subprocess
import sys
from pathlib import Path
from typing import Dict, List, Tuple, Optional

ROOT = Path(__file__).resolve().parents[1]
README = ROOT / "README.md"
BUILD_SCRIPT = ROOT / "scripts" / "build-releases.py"
RELEASES_DIR = ROOT / "releases"
COMPLETE_GUIDE_MD = RELEASES_DIR / "Awesome-Mnemonics-Complete-Guide.md"

class Colors:
    """ANSI color codes for terminal output."""
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BLUE = '\033[94m'
    RESET = '\033[0m'
    BOLD = '\033[1m'

class VerificationResult:
    """Container for verification results."""
    def __init__(self):
        self.errors: List[str] = []
        self.warnings: List[str] = []
        self.info: List[str] = []
        self.passed: List[str] = []
    
    def add_error(self, msg: str):
        self.errors.append(msg)
    
    def add_warning(self, msg: str):
        self.warnings.append(msg)
    
    def add_info(self, msg: str):
        self.info.append(msg)
    
    def add_pass(self, msg: str):
        self.passed.append(msg)
    
    def has_issues(self) -> bool:
        return len(self.errors) > 0 or len(self.warnings) > 0

def get_version_from_build_script() -> Optional[str]:
    """Extract version from build script."""
    try:
        content = BUILD_SCRIPT.read_text(encoding="utf-8")
        match = re.search(r'VERSION\s*=\s*["\']([^"\']+)["\']', content)
        if match:
            return match.group(1)
    except Exception as e:
        return None
    return None

def get_version_from_readme() -> Optional[str]:
    """Extract version from README release section."""
    try:
        content = README.read_text(encoding="utf-8")
        # Look for "**v2.8**" pattern in Release Versions section
        match = re.search(r'\*\*v(\d+\.\d+)\*\*.*Release Versions', content, re.DOTALL)
        if match:
            return match.group(1)
        # Fallback: look for any v2.x in release section
        match = re.search(r'## 📥 Release Versions.*?\*\*v(\d+\.\d+)\*\*', content, re.DOTALL)
        if match:
            return match.group(1)
    except Exception as e:
        return None
    return None

def get_version_from_release_md() -> Optional[str]:
    """Extract version from generated release markdown."""
    if not COMPLETE_GUIDE_MD.exists():
        return None
    try:
        content = COMPLETE_GUIDE_MD.read_text(encoding="utf-8")
        match = re.search(r'Release v(\d+\.\d+)', content)
        if match:
            return match.group(1)
    except Exception as e:
        return None
    return None

def get_download_links_from_readme() -> List[str]:
    """Extract all download file links from README."""
    try:
        content = README.read_text(encoding="utf-8")
        # Find all releases/... file references (more precise pattern)
        pattern = r'\]\(releases/([^\s\)]+\.(?:pdf|docx|rtf|md|zip))\)'
        matches = re.findall(pattern, content)
        return [f"releases/{match}" for match in matches]
    except Exception as e:
        return []

def verify_version_consistency(result: VerificationResult):
    """Verify version numbers are consistent across all files."""
    print(f"{Colors.BOLD}Checking version consistency...{Colors.RESET}")
    
    build_version = get_version_from_build_script()
    readme_version = get_version_from_readme()
    release_version = get_version_from_release_md()
    
    if not build_version:
        result.add_error("Could not extract version from build script")
        return
    
    if not readme_version:
        result.add_error("Could not extract version from README.md")
        return
    
    if not release_version:
        result.add_warning("Could not extract version from release markdown (file may not exist)")
    else:
        if build_version != release_version:
            result.add_error(f"Version mismatch: build script has {build_version}, release markdown has {release_version}")
    
    if build_version != readme_version:
        result.add_error(f"Version mismatch: build script has {build_version}, README has v{readme_version}")
    else:
        result.add_pass(f"Version consistency: All files use v{build_version}")

def verify_download_links(result: VerificationResult):
    """Verify all download links in README point to existing files."""
    print(f"{Colors.BOLD}Checking download links...{Colors.RESET}")
    
    links = get_download_links_from_readme()
    if not links:
        result.add_warning("No download links found in README.md")
        return
    
    missing_files = []
    existing_files = []
    
    for link in set(links):  # Remove duplicates
        file_path = ROOT / link
        if file_path.exists():
            existing_files.append(link)
        else:
            missing_files.append(link)
    
    if missing_files:
        result.add_error(f"Missing files referenced in README: {', '.join(missing_files)}")
    else:
        result.add_pass(f"All {len(existing_files)} download links point to existing files")

def verify_file_freshness(result: VerificationResult):
    """Verify release files are newer than or equal to README."""
    print(f"{Colors.BOLD}Checking file freshness...{Colors.RESET}")
    
    if not README.exists():
        result.add_error("README.md does not exist")
        return
    
    readme_mtime = README.stat().st_mtime
    # Allow 24 hours difference for PDF (may fail to regenerate due to LaTeX issues)
    pdf_tolerance = 24 * 60 * 60  # 24 hours in seconds
    
    release_files = [
        (COMPLETE_GUIDE_MD, 0),  # No tolerance
        (RELEASES_DIR / "Awesome-Mnemonics-Complete-Guide.docx", 0),
        (RELEASES_DIR / "Awesome-Mnemonics-Complete-Guide.rtf", 0),
        (RELEASES_DIR / "Awesome-Mnemonics-Complete-Guide.pdf", pdf_tolerance),  # 24h tolerance
    ]
    
    stale_files = []
    fresh_files = []
    
    for file_path, tolerance in release_files:
        if not file_path.exists():
            continue
        
        file_mtime = file_path.stat().st_mtime
        age_diff = readme_mtime - file_mtime
        
        if age_diff > tolerance:
            stale_files.append((file_path.name, file_mtime, readme_mtime, age_diff))
        else:
            fresh_files.append(file_path.name)
    
    if stale_files:
        for name, file_time, readme_time, age_diff in stale_files:
            hours_old = age_diff / 3600
            if hours_old > 24:
                result.add_warning(f"{name} is {hours_old:.1f} hours older than README.md (may need regeneration)")
            else:
                result.add_warning(f"{name} is older than README.md (may need regeneration)")
    else:
        result.add_pass(f"All release files are up-to-date ({len(fresh_files)} files checked)")

def verify_content_consistency(result: VerificationResult):
    """Verify release markdown content matches README structure."""
    print(f"{Colors.BOLD}Checking content consistency...{Colors.RESET}")
    
    if not COMPLETE_GUIDE_MD.exists():
        result.add_warning("Release markdown does not exist (run build script first)")
        return
    
    try:
        readme_content = README.read_text(encoding="utf-8")
        release_content = COMPLETE_GUIDE_MD.read_text(encoding="utf-8")
        
        # Check that release version description matches
        readme_version_match = re.search(r'\*\*v\d+\.\d+\*\*.*?—\s*([^\[]+)\[', readme_content)
        release_version_match = re.search(r'\*\*v\d+\.\d+\*\*.*?—\s*([^\[]+)\[', release_content)
        
        if readme_version_match and release_version_match:
            readme_desc = readme_version_match.group(1).strip()
            release_desc = release_version_match.group(1).strip()
            if readme_desc != release_desc:
                result.add_warning(f"Version descriptions differ between README and release file")
            else:
                result.add_pass("Version descriptions match between README and release file")
        
        # Check that release file has the expected transformations
        if "Awesome Mnemonics - Complete Guide" not in release_content:
            result.add_warning("Release file may not have correct title transformation")
        else:
            result.add_pass("Release file has correct title")
            
    except Exception as e:
        result.add_error(f"Error checking content consistency: {e}")

def check_git_status(result: VerificationResult, check_remote: bool = False):
    """Check git status for uncommitted changes and remote sync."""
    print(f"{Colors.BOLD}Checking git status...{Colors.RESET}")
    
    try:
        # Check for uncommitted changes (only unstaged, not staged)
        status_result = subprocess.run(
            ["git", "status", "--porcelain"],
            cwd=ROOT,
            capture_output=True,
            text=True,
            check=False
        )
        
        if status_result.returncode != 0:
            result.add_warning("Could not check git status (not a git repo?)")
            return
        
        all_changes = [line for line in status_result.stdout.strip().split('\n') if line.strip()]
        
        # Separate staged (A/M/D in first column) from unstaged (A/M/D in second column)
        # Format: "XY filename" where X=staged, Y=unstaged
        unstaged_changes = []
        staged_changes = []
        
        for line in all_changes:
            if len(line) < 3:
                continue
            staged_status = line[0]
            unstaged_status = line[1]
            
            # Filter out verification script files (they're expected initially)
            filename = line[3:].strip()
            verification_files = ['scripts/verify-sync.py', 'scripts/README-verify-sync.md', 'scripts/VERIFICATION-SUMMARY.md']
            if any(vf in filename for vf in verification_files):
                continue
            
            if unstaged_status != ' ':
                unstaged_changes.append(line)
            elif staged_status != ' ':
                staged_changes.append(line)
        
        if unstaged_changes:
            result.add_warning(f"Unstaged changes detected: {len(unstaged_changes)} file(s)")
            for line in unstaged_changes[:5]:  # Show first 5
                result.add_info(f"  {line}")
            if len(unstaged_changes) > 5:
                result.add_info(f"  ... and {len(unstaged_changes) - 5} more")
        elif staged_changes:
            result.add_info(f"Staged changes ready to commit: {len(staged_changes)} file(s)")
            result.add_pass("No unstaged changes (some files are staged)")
        else:
            result.add_pass("No uncommitted changes")
        
        # Check remote sync if requested
        if check_remote:
            try:
                # Fetch latest from remote
                subprocess.run(
                    ["git", "fetch", "origin"],
                    cwd=ROOT,
                    capture_output=True,
                    check=False
                )
                
                # Check if local is ahead/behind remote
                status_result = subprocess.run(
                    ["git", "status", "-sb"],
                    cwd=ROOT,
                    capture_output=True,
                    text=True,
                    check=True
                )
                
                if "ahead" in status_result.stdout:
                    result.add_warning("Local branch is ahead of remote (unpushed commits)")
                elif "behind" in status_result.stdout:
                    result.add_warning("Local branch is behind remote (need to pull)")
                else:
                    result.add_pass("Local and remote branches are in sync")
                    
            except Exception as e:
                result.add_warning(f"Could not check remote sync: {e}")
                
    except Exception as e:
        result.add_warning(f"Error checking git status: {e}")

def print_results(result: VerificationResult):
    """Print verification results with color coding."""
    print(f"\n{Colors.BOLD}{'='*60}{Colors.RESET}")
    print(f"{Colors.BOLD}Verification Results{Colors.RESET}")
    print(f"{Colors.BOLD}{'='*60}{Colors.RESET}\n")
    
    if result.passed:
        print(f"{Colors.GREEN}✓ Passed ({len(result.passed)}):{Colors.RESET}")
        for msg in result.passed:
            print(f"  {Colors.GREEN}✓{Colors.RESET} {msg}")
        print()
    
    if result.info:
        print(f"{Colors.BLUE}ℹ Info ({len(result.info)}):{Colors.RESET}")
        for msg in result.info:
            print(f"  {Colors.BLUE}ℹ{Colors.RESET} {msg}")
        print()
    
    if result.warnings:
        print(f"{Colors.YELLOW}⚠ Warnings ({len(result.warnings)}):{Colors.RESET}")
        for msg in result.warnings:
            print(f"  {Colors.YELLOW}⚠{Colors.RESET} {msg}")
        print()
    
    if result.errors:
        print(f"{Colors.RED}✗ Errors ({len(result.errors)}):{Colors.RESET}")
        for msg in result.errors:
            print(f"  {Colors.RED}✗{Colors.RESET} {msg}")
        print()
    
    # Summary
    if not result.has_issues():
        print(f"{Colors.GREEN}{Colors.BOLD}✓ All checks passed! Everything is in sync.{Colors.RESET}\n")
        return 0
    else:
        print(f"{Colors.YELLOW}{Colors.BOLD}⚠ Issues found: {len(result.errors)} error(s), {len(result.warnings)} warning(s){Colors.RESET}\n")
        return 1

def prompt_user_action(result: VerificationResult) -> bool:
    """Prompt user for action on discrepancies."""
    if not result.has_issues():
        return True
    
    # Check if running in non-interactive mode
    if not sys.stdin.isatty():
        print(f"{Colors.YELLOW}Non-interactive mode: Issues found but cannot prompt.{Colors.RESET}")
        return False
    
    print(f"{Colors.BOLD}How would you like to proceed?{Colors.RESET}")
    print("  1. Continue anyway (ignore issues)")
    print("  2. Run build script to regenerate release files")
    print("  3. Exit and fix issues manually")
    
    while True:
        try:
            choice = input(f"\n{Colors.BOLD}Enter choice (1-3): {Colors.RESET}").strip()
            if choice == "1":
                return True
            elif choice == "2":
                print(f"\n{Colors.BLUE}Running build script...{Colors.RESET}")
                try:
                    subprocess.run(
                        ["python3", str(BUILD_SCRIPT)],
                        cwd=ROOT,
                        check=True
                    )
                    print(f"{Colors.GREEN}Build script completed. Re-run verification to check results.{Colors.RESET}\n")
                    return False  # Suggest re-running verification
                except subprocess.CalledProcessError as e:
                    print(f"{Colors.RED}Build script failed: {e}{Colors.RESET}\n")
                    return False
            elif choice == "3":
                print(f"{Colors.YELLOW}Exiting. Please fix issues manually.{Colors.RESET}\n")
                return False
            else:
                print(f"{Colors.RED}Invalid choice. Please enter 1, 2, or 3.{Colors.RESET}")
        except (KeyboardInterrupt, EOFError):
            print(f"\n{Colors.YELLOW}Interrupted by user.{Colors.RESET}\n")
            return False

def main():
    """Main verification function."""
    import argparse
    
    parser = argparse.ArgumentParser(
        description="Verify README, documents, and release versions are in sync"
    )
    parser.add_argument(
        "--check-remote",
        action="store_true",
        help="Also check remote repository sync status"
    )
    parser.add_argument(
        "--auto-fix",
        action="store_true",
        help="Automatically run build script if issues found (non-interactive)"
    )
    parser.add_argument(
        "--quiet",
        action="store_true",
        help="Only show errors and warnings"
    )
    
    args = parser.parse_args()
    
    result = VerificationResult()
    
    if not args.quiet:
        print(f"{Colors.BOLD}Verifying repository sync...{Colors.RESET}\n")
    
    # Run all verification checks
    verify_version_consistency(result)
    verify_download_links(result)
    verify_file_freshness(result)
    verify_content_consistency(result)
    check_git_status(result, check_remote=args.check_remote)
    
    # Print results
    exit_code = print_results(result)
    
    # Handle discrepancies
    if result.has_issues():
        if args.auto_fix:
            print(f"{Colors.BLUE}Auto-fix enabled: Running build script...{Colors.RESET}")
            try:
                subprocess.run(
                    ["python3", str(BUILD_SCRIPT)],
                    cwd=ROOT,
                    check=True
                )
                print(f"{Colors.GREEN}Build script completed.{Colors.RESET}\n")
                # Re-run verification
                print(f"{Colors.BLUE}Re-running verification...{Colors.RESET}\n")
                result2 = VerificationResult()
                verify_version_consistency(result2)
                verify_download_links(result2)
                verify_file_freshness(result2)
                verify_content_consistency(result2)
                exit_code = print_results(result2)
            except subprocess.CalledProcessError as e:
                print(f"{Colors.RED}Build script failed: {e}{Colors.RESET}\n")
                exit_code = 1
        else:
            if not prompt_user_action(result):
                exit_code = 1
    
    return exit_code

if __name__ == "__main__":
    sys.exit(main())
