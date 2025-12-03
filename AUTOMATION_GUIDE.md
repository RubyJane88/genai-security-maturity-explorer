# 🤖 Automated Deployment Checks

## Overview

This project includes **three layers of automated checks** to prevent deployment issues:

1. **Local Git Hooks** - Run before commits and pushes
2. **GitHub Actions** - Run on every push to GitHub
3. **Manual Tools** - Run anytime you want

---

## 🚀 Quick Setup

```bash
# One-time setup (installs all automation)
./setup_checks.sh
```

That's it! All automated checks are now enabled.

---

## 📋 What Gets Checked Automatically

### ✅ Pre-Commit Hook (Strict)

**Runs:** Before every `git commit`

**Checks:**

- ✓ Virtual environment activated
- ✓ Python version compatibility
- ✓ Package compatibility
- ✓ Critical imports work
- ✓ Deployment files present
- ✓ No dependency conflicts

**Result:** Blocks commit if any check fails

### ✅ Pre-Push Hook (Safety Net)

**Runs:** Before every `git push`

**Checks:**

- ✓ app.py has no syntax errors
- ✓ Critical packages import successfully
- ✓ No dependency conflicts
- ✓ All deployment files present

**Result:** Blocks push if critical checks fail

### ✅ GitHub Actions (CI/CD)

**Runs:** After every push to GitHub

**Three parallel jobs:**

1. **Compatibility Check**

   - Installs on Python 3.11 (deployment target)
   - Tests all imports
   - Runs full compatibility check
   - Verifies app.py syntax

2. **Security Scan**

   - Checks for known vulnerabilities
   - Uses `safety` package
   - Non-blocking (warns only)

3. **Code Quality**
   - Checks code formatting (black)
   - Runs linter (flake8)
   - Non-blocking (warns only)

---

## 🎯 Usage Examples

### Scenario 1: Normal Workflow (Fully Automated)

```bash
# 1. Make changes to code
vim app.py

# 2. Try to commit
git add app.py
git commit -m "Add feature"
# ✅ Pre-commit hook runs automatically

# 3. Try to push
git push origin main
# ✅ Pre-push hook runs automatically
# ✅ GitHub Actions runs after push
```

### Scenario 2: Quick Manual Check

```bash
# Before making changes, verify everything works
python check_compatibility.py
```

### Scenario 3: Bypass Hooks (Emergency Only)

```bash
# Skip pre-commit (not recommended)
git commit --no-verify -m "Emergency fix"

# Skip pre-push (really not recommended)
git push --no-verify origin main
```

### Scenario 4: Fresh Clone Setup

```bash
# Someone else clones your repo
git clone https://github.com/RubyJane88/genai-security-maturity-explorer.git
cd genai-security-maturity-explorer

# One command to set everything up
./setup_checks.sh
```

---

## 📊 What You See

### ✅ Successful Commit

```bash
$ git commit -m "Update feature"
🔍 Running pre-commit compatibility checks...

Running compatibility checks...
==================================================
🔍 PRE-DEPLOYMENT COMPATIBILITY CHECK
==================================================
...
Score: 6/6 checks passed

🎉 All checks passed! Safe to deploy.

✅ All pre-commit checks passed! Proceeding with commit...

[main abc1234] Update feature
 1 file changed, 10 insertions(+)
```

### ❌ Failed Commit

```bash
$ git commit -m "Broken feature"
🔍 Running pre-commit compatibility checks...

❌ Import test failed: ModuleNotFoundError: No module named 'pandas'

❌ Pre-commit checks failed!
   Fix the issues above before committing.

   To bypass (not recommended): git commit --no-verify
```

### 📱 GitHub Actions Status

After pushing, check: `https://github.com/RubyJane88/genai-security-maturity-explorer/actions`

You'll see:

- ✅ Compatibility Check (passed)
- ✅ Security Scan (passed)
- ✅ Code Quality (passed)

Or click on failed checks to see details.

---

## 🔧 Configuration

### Customize Pre-Commit Hook

Edit: `.git/hooks/pre-commit`

```bash
# Example: Skip checks for certain files
if [[ "$file" == *.md ]]; then
    skip
fi
```

### Customize GitHub Actions

Edit: `.github/workflows/compatibility-check.yml`

```yaml
# Example: Add Python 3.12 testing
strategy:
  matrix:
    python-version: ["3.11", "3.12"]
```

### Disable Hooks Temporarily

```bash
# Disable for one command
git commit --no-verify

# Disable all hooks
mv .git/hooks/pre-commit .git/hooks/pre-commit.disabled

# Re-enable
mv .git/hooks/pre-commit.disabled .git/hooks/pre-commit
```

---

## 🎨 GitHub Actions Badge

Add to your README.md:

```markdown
[![Compatibility Checks](https://github.com/RubyJane88/genai-security-maturity-explorer/actions/workflows/compatibility-check.yml/badge.svg)](https://github.com/RubyJane88/genai-security-maturity-explorer/actions/workflows/compatibility-check.yml)
```

Shows build status to visitors!

---

## 🐛 Troubleshooting

### Issue: "Virtual environment not activated"

```bash
# Solution: Activate before committing
source venv/bin/activate
git commit -m "message"
```

### Issue: Hooks not running

```bash
# Check if hooks are executable
ls -la .git/hooks/pre-commit
ls -la .git/hooks/pre-push

# Make executable
chmod +x .git/hooks/pre-commit
chmod +x .git/hooks/pre-push
```

### Issue: GitHub Actions failing

```bash
# Check workflow file syntax
cat .github/workflows/compatibility-check.yml

# View logs on GitHub
# Go to: Actions tab → Click failed workflow → View logs
```

### Issue: False positives

```bash
# Test locally first
python check_compatibility.py

# If passes locally but fails in CI, check Python version
# GitHub Actions uses Python 3.11
```

---

## 📦 What Gets Installed

### Git Hooks (Local Only)

- `.git/hooks/pre-commit` - Runs before commits
- `.git/hooks/pre-push` - Runs before pushes

**Note:** Git hooks are **not** pushed to GitHub (they're in `.git/` which is ignored). Team members need to run `./setup_checks.sh` after cloning.

### GitHub Actions (Cloud)

- `.github/workflows/compatibility-check.yml` - CI/CD pipeline

**Note:** This **is** pushed to GitHub and runs automatically for everyone.

---

## 🔄 Maintenance

### Update Dependencies

```bash
# Update requirements
pip install --upgrade dash plotly pandas numpy

# Regenerate requirements.txt
pip freeze > requirements.txt

# Test compatibility
python check_compatibility.py

# Commit if all green
git commit -m "chore: Update dependencies"
```

### Monthly Security Check

```bash
# Install safety
pip install safety

# Check for vulnerabilities
safety check

# Update if needed
pip install --upgrade package-name
```

---

## 📈 Benefits

### Before Automation

❌ Push → Build fails → Debug → Fix → Push again  
⏱️ Time wasted: 10-20 minutes per failure

### After Automation

✅ Commit blocked → Fix immediately → Commit succeeds → Deploy works  
⏱️ Time saved: 10-20 minutes per deployment

### Additional Benefits

- 🛡️ Prevents bad code from reaching production
- 📊 Consistent code quality across team
- 🔒 Early security vulnerability detection
- 📚 Self-documenting deployment requirements
- ✅ Confidence in every deployment

---

## 🎓 Learning Resources

- [Git Hooks Documentation](https://git-scm.com/book/en/v2/Customizing-Git-Git-Hooks)
- [GitHub Actions Documentation](https://docs.github.com/en/actions)
- [Python Packaging Best Practices](https://packaging.python.org/)

---

## 💡 Pro Tips

1. **Run checks before starting work**

   ```bash
   python check_compatibility.py
   ```

2. **Keep virtual environment activated**

   ```bash
   # Add to ~/.zshrc or ~/.bashrc
   cd() { builtin cd "$@" && [ -f venv/bin/activate ] && source venv/bin/activate; }
   ```

3. **Watch GitHub Actions in real-time**

   - Push code → Go to Actions tab → Watch build live

4. **Use pre-commit for faster feedback**

   - Catches issues before push
   - Saves CI/CD minutes

5. **Review failed checks carefully**
   - They exist to save you time
   - Fix root cause, don't bypass

---

**Remember:** Automation is your friend! These checks take seconds but save hours. 🚀
