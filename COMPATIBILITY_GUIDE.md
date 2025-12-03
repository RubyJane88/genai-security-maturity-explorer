# 🔍 Dependency Compatibility Guide

## Why Compatibility Issues Happen

### 1. **Python's Dynamic Nature**

Unlike compiled languages (Java, C++), Python doesn't check compatibility until runtime:

```python
# This looks fine...
import pandas as pd

# ...but crashes here if pandas wasn't compiled for your Python version
df = pd.DataFrame(data)  # ❌ ImportError at runtime!
```

### 2. **The Dependency Chain**

```
Your app (Python 3.13)
  └─ pandas 2.1.4
      └─ numpy 1.26.2
          └─ C extensions compiled for Python 3.9-3.12 ❌
              └─ Python 3.13 API changed → BUILD FAILS
```

### 3. **Platform Differences**

| Factor           | Your Mac      | Render.com | Impact                      |
| ---------------- | ------------- | ---------- | --------------------------- |
| **OS**           | macOS         | Linux      | Different system libraries  |
| **Architecture** | ARM64 (M1/M2) | x86_64     | Different compiled binaries |
| **Python**       | 3.12.9        | 3.11.0     | Different ABIs              |
| **Compiler**     | clang         | gcc        | Different C compilation     |

---

## 🛡️ How to Prevent Issues

### Strategy 1: Version Pinning

**Always pin exact versions in `requirements.txt`:**

```txt
✅ GOOD - Exact versions
dash==2.14.2
pandas==2.1.4
numpy==1.26.2

❌ BAD - Unpinned versions
dash
pandas>=2.0
numpy~=1.26
```

**Why?** Prevents surprise updates that break compatibility.

### Strategy 2: Use `.python-version`

```bash
# Tell all tools exactly which Python to use
echo "3.11.0" > .python-version
```

**Respected by:**

- Render.com
- pyenv
- asdf
- VS Code Python extension

### Strategy 3: Test Before Deploying

#### Option A: Quick Shell Script

```bash
./check_compatibility.sh
```

Checks:

- Python version
- Virtual environment
- Package resolution
- Import tests
- Syntax errors

#### Option B: Detailed Python Script

```bash
python check_compatibility.py
```

Checks:

- Python version matching
- Requirements validation
- Package compatibility
- Import tests
- Deployment files
- Dependency conflicts

### Strategy 4: Use Docker for Exact Matching

```dockerfile
# Dockerfile
FROM python:3.11-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .
CMD ["gunicorn", "app:server", "--bind", "0.0.0.0:8050"]
```

**Test locally:**

```bash
docker build -t genai-maturity .
docker run -p 8050:8050 genai-maturity
```

Now your local environment **exactly matches** production!

---

## 📋 Pre-Deployment Checklist

### Before Every Git Push:

```bash
# 1. Activate virtual environment
source venv/bin/activate

# 2. Run compatibility check
python check_compatibility.py

# 3. Test the app locally
python app.py
# Visit http://localhost:8050 and test features

# 4. Check for uncommitted files
git status

# 5. Push if all green
git add .
git commit -m "your message"
git push origin main
```

---

## 🔧 Troubleshooting Common Issues

### Issue 1: "Package X requires Python <3.13"

**Solution:**

```bash
# Update .python-version
echo "3.11.0" > .python-version

# Update render.yaml
envVars:
  - key: PYTHON_VERSION
    value: "3.11"
```

### Issue 2: "Compilation failed"

**Cause:** Binary package (pandas, numpy) not available for your Python/OS combo.

**Solution:**

```bash
# Option 1: Use compatible Python version
pyenv install 3.11.0
pyenv local 3.11.0

# Option 2: Update package to newer version
# Check: https://pypi.org/project/pandas/#files
pip install pandas==2.2.0  # May support newer Python
```

### Issue 3: "Works locally, fails on Render"

**Cause:** Mac ARM64 vs Linux x86_64 differences.

**Solution:**

```bash
# Test with Docker (matches Linux environment)
docker run -it --rm -v $(pwd):/app python:3.11 bash
cd /app
pip install -r requirements.txt
python app.py
```

### Issue 4: "Dependency conflict detected"

**Example:**

```
dash 2.14.2 requires werkzeug<3.1
flask 3.0 requires werkzeug>=3.0
```

**Solution:**

```bash
# Check conflicts
pip check

# View dependency tree
pip install pipdeptree
pipdeptree --warn fail

# Fix by updating or pinning
pip install "flask<3.0"
pip freeze > requirements.txt
```

---

## 🎯 Best Practices

### 1. **Regular Dependency Audits**

```bash
# Every month, check for updates and security issues
pip list --outdated
pip install safety
safety check
```

### 2. **Use Virtual Environments Always**

```bash
# Never install globally
python -m venv venv
source venv/bin/activate
```

### 3. **Document Your Python Version**

In multiple places for redundancy:

- `runtime.txt` → `python-3.11.0`
- `.python-version` → `3.11.0`
- `render.yaml` → `PYTHON_VERSION: "3.11"`
- `README.md` → "Python 3.11+ required"

### 4. **Test on Target Platform**

```bash
# Option 1: Docker
docker run -it python:3.11-slim bash

# Option 2: CI/CD (GitHub Actions)
# .github/workflows/test.yml
jobs:
  test:
    runs-on: ubuntu-latest
    strategy:
      matrix:
        python-version: [3.11]
```

### 5. **Pin Transitive Dependencies**

```bash
# Generate complete locked versions
pip freeze > requirements-lock.txt

# Use in production
pip install -r requirements-lock.txt
```

---

## 📚 Useful Commands

```bash
# Check Python version
python --version

# Check pip version
pip --version

# List installed packages
pip list

# Check for conflicts
pip check

# Show package dependencies
pip show pandas

# Install specific Python version (using pyenv)
pyenv install 3.11.0
pyenv local 3.11.0

# Create requirements from installed packages
pip freeze > requirements.txt

# Test if requirements install cleanly
pip install --dry-run -r requirements.txt

# Verify imports work
python -c "import dash, pandas, numpy; print('OK')"

# Check for security vulnerabilities
pip install safety
safety check
```

---

## 🚀 Quick Reference

| Problem                       | Solution                                     |
| ----------------------------- | -------------------------------------------- |
| Build fails on Render         | Match Python versions with `.python-version` |
| Works locally, fails deployed | Test with Docker using same Python version   |
| Import errors                 | Run `python check_compatibility.py`          |
| Dependency conflicts          | Run `pip check` and resolve                  |
| Outdated packages             | Run `pip list --outdated`                    |
| Security issues               | Run `safety check`                           |

---

## 📖 Additional Resources

- [Python Packaging Guide](https://packaging.python.org/)
- [Render Python Docs](https://render.com/docs/python-version)
- [Compatibility Charts](https://pypi.org/) - Check "Download files" for each package
- [Common Issues](https://render.com/docs/troubleshooting-deploys)

---

**Remember:** 5 minutes of checking prevents 5 hours of debugging! 🎯
