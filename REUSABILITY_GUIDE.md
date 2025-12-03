# 🔄 Reusability Guide: Using Automation in Other Projects

## 🎯 Quick Answer

**YES!** These automation scripts work for:

- ✅ **Any Python project** - Works immediately
- ✅ **Node.js/JavaScript** - Modify commands
- ✅ **Java/Maven/Gradle** - Modify commands
- ✅ **Go** - Modify commands
- ✅ **Ruby** - Modify commands
- ✅ **Rust** - Modify commands
- ✅ **Any language** - Use universal template

**The concepts are universal. Only the commands change.**

---

## 🚀 Method 1: Copy to Another Python Project

### Step-by-Step:

```bash
# 1. Navigate to your new project
cd /path/to/my-new-python-project

# 2. Copy automation files
cp ~/Documents/genai-security-maturity-explorer/check_compatibility.py .
cp ~/Documents/genai-security-maturity-explorer/check_compatibility.sh .
cp ~/Documents/genai-security-maturity-explorer/setup_checks.sh .
cp -r ~/Documents/genai-security-maturity-explorer/.github .

# 3. Customize for your project
vim check_compatibility.py  # Update line 115: critical_imports
vim .github/workflows/compatibility-check.yml  # Update line 48: main file name

# 4. Run setup
./setup_checks.sh

# 5. Done!
git add .
git commit -m "Add automated checks"
```

### What to Customize:

**File: `check_compatibility.py`** (Line ~115)

```python
# Change this list to your project's critical imports
critical_imports = [
    "flask",           # ← Your imports
    "sqlalchemy",      # ←
    "redis",           # ←
    "celery"           # ←
]
```

**File: `.github/workflows/compatibility-check.yml`** (Line ~48)

```yaml
- name: ✅ Verify app syntax
  run: |
    python -m py_compile main.py  # ← Your main file
```

**File: `check_compatibility.py`** (Line ~135)

```python
required_files = {
    "main.py": "Main application file",        # ← Your files
    "requirements.txt": "Python dependencies",
    "Dockerfile": "Container configuration",   # ← Your files
}
```

---

## 🌐 Method 2: Adapt for Node.js/JavaScript

### Quick Start:

```bash
# 1. Copy universal template
cp examples/universal-pre-commit-template.sh .git/hooks/pre-commit
chmod +x .git/hooks/pre-commit

# 2. Edit for Node.js
vim .git/hooks/pre-commit
```

### Customization Example:

```bash
#!/bin/bash
# Pre-commit hook for Node.js

set -e

echo "🔍 Running pre-commit checks for Node.js..."
echo ""

# 1. Check Node.js version
echo "1️⃣  Checking Node.js version..."
node --version
echo ""

# 2. Check dependencies
echo "2️⃣  Checking dependencies..."
if [ ! -d "node_modules" ]; then
    echo "   ❌ Run: npm install"
    exit 1
fi
echo "   ✅ node_modules found"
echo ""

# 3. Run ESLint
echo "3️⃣  Running ESLint..."
npm run lint
echo ""

# 4. Run tests
echo "4️⃣  Running tests..."
npm test
echo ""

# 5. Build check
echo "5️⃣  Checking build..."
npm run build --dry-run
echo ""

# 6. Security audit
echo "6️⃣  Security audit..."
npm audit --audit-level=moderate
echo ""

echo "✅ All checks passed!"
exit 0
```

### GitHub Actions for Node.js:

```yaml
name: Node.js CI

on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest
    strategy:
      matrix:
        node-version: [18.x, 20.x]

    steps:
      - uses: actions/checkout@v4
      - name: Setup Node.js
        uses: actions/setup-node@v4
        with:
          node-version: ${{ matrix.node-version }}

      - run: npm ci
      - run: npm run lint
      - run: npm test
      - run: npm run build
      - run: npm audit
```

---

## ☕ Method 3: Adapt for Java/Maven

### Pre-Commit Hook:

```bash
#!/bin/bash
# Pre-commit hook for Java/Maven

set -e

echo "🔍 Running pre-commit checks for Java..."
echo ""

# 1. Check Java version
echo "1️⃣  Checking Java..."
java -version
echo ""

# 2. Compile
echo "2️⃣  Compiling..."
mvn compile -q
echo "   ✅ Compilation successful"
echo ""

# 3. Run tests
echo "3️⃣  Running tests..."
mvn test -q
echo "   ✅ Tests passed"
echo ""

# 4. Check style
echo "4️⃣  Checking code style..."
mvn checkstyle:check -q
echo ""

# 5. Security scan
echo "5️⃣  Dependency check..."
mvn dependency-check:check -q
echo ""

echo "✅ All checks passed!"
exit 0
```

### GitHub Actions for Java:

```yaml
name: Java CI

on: [push, pull_request]

jobs:
  build:
    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v4
      - name: Set up JDK 11
        uses: actions/setup-java@v4
        with:
          java-version: "11"
          distribution: "temurin"

      - name: Build with Maven
        run: mvn clean install

      - name: Run tests
        run: mvn test

      - name: Check style
        run: mvn checkstyle:check
```

---

## 🗂️ Method 4: Universal Template (Any Language)

### Use the Template:

```bash
# 1. Copy universal template
cp examples/universal-pre-commit-template.sh .git/hooks/pre-commit

# 2. Make executable
chmod +x .git/hooks/pre-commit

# 3. Customize sections 1-6 for your language
vim .git/hooks/pre-commit
```

### Customization Matrix:

| Language    | Version Check      | Dependencies                    | Linter              | Tests         | Compile/Check  |
| ----------- | ------------------ | ------------------------------- | ------------------- | ------------- | -------------- |
| **Python**  | `python --version` | `venv/`, `requirements.txt`     | `flake8`, `black`   | `pytest`      | `py_compile`   |
| **Node.js** | `node --version`   | `node_modules/`, `package.json` | `eslint`            | `npm test`    | `tsc --noEmit` |
| **Java**    | `java -version`    | `pom.xml`, `build.gradle`       | `checkstyle`        | `mvn test`    | `mvn compile`  |
| **Go**      | `go version`       | `go.mod`                        | `gofmt`, `golint`   | `go test`     | `go build`     |
| **Ruby**    | `ruby --version`   | `Gemfile`                       | `rubocop`           | `rake test`   | `ruby -c`      |
| **Rust**    | `rustc --version`  | `Cargo.toml`                    | `rustfmt`, `clippy` | `cargo test`  | `cargo check`  |
| **PHP**     | `php --version`    | `composer.json`                 | `phpcs`             | `phpunit`     | `php -l`       |
| **C#**      | `dotnet --version` | `*.csproj`                      | `dotnet format`     | `dotnet test` | `dotnet build` |

---

## 📦 Creating a Reusable Package

### Make it a Git Submodule:

```bash
# In your automation repo
cd ~/Documents/automation-toolkit
git init
cp check_compatibility.py .
cp check_compatibility.sh .
cp -r .github .
git add .
git commit -m "Initial automation toolkit"
git remote add origin https://github.com/YourUsername/automation-toolkit.git
git push -u origin main

# In any new project
cd /path/to/new-project
git submodule add https://github.com/YourUsername/automation-toolkit.git automation
./automation/setup_checks.sh
```

### Or Create an NPM Package:

```bash
# For Node.js projects
npm install --save-dev @yourname/automation-hooks

# In package.json:
{
  "scripts": {
    "prepare": "automation-hooks install"
  }
}
```

### Or Create a PyPI Package:

```bash
# For Python projects
pip install automation-hooks

# In your project:
automation-hooks install
```

---

## 🎨 Customization Checklist

When adapting to a new project, update:

- [ ] **Language version** - Check command (e.g., `node --version`)
- [ ] **Package manager** - Check command (e.g., `npm install`)
- [ ] **Critical imports** - List of must-have packages
- [ ] **Main file** - Entry point (e.g., `main.py`, `index.js`)
- [ ] **Linter command** - Code style tool (e.g., `eslint`)
- [ ] **Test command** - How to run tests (e.g., `pytest`)
- [ ] **Build command** - Compilation step (if applicable)
- [ ] **Config files** - Required files (e.g., `package.json`)
- [ ] **GitHub Actions** - Update workflow file
- [ ] **Branch names** - Update in workflow file

---

## 💡 Best Practices

### 1. **Keep It Simple**

Don't add every possible check. Focus on what matters:

- Version compatibility
- Syntax/compilation
- Tests (if you have them)
- Critical imports

### 2. **Make It Fast**

Pre-commit hooks should be < 30 seconds:

- ✅ Quick: Syntax check, linting
- ⚠️ Slow: Full test suite (use pre-push instead)
- ❌ Very slow: Security scans (use GitHub Actions)

### 3. **Provide Escape Hatch**

Always allow bypassing in emergencies:

```bash
git commit --no-verify -m "Emergency fix"
```

### 4. **Document It**

Add to your project's README:

````markdown
## Development Setup

Run once:

```bash
./setup_checks.sh
```
````

This installs Git hooks that run automated checks.

````

### 5. **Test Locally First**
Before committing hook changes:
```bash
# Test the pre-commit hook
.git/hooks/pre-commit

# If it passes, commit it
git commit -m "Update hooks"
````

---

## 🧪 Testing Your Automation

### Test Pre-Commit Hook:

```bash
# Should pass
.git/hooks/pre-commit

# Should fail (break something intentionally)
echo "syntax error" >> app.py
.git/hooks/pre-commit
git checkout app.py  # Undo
```

### Test GitHub Actions:

```bash
# Push to a test branch
git checkout -b test-automation
git push origin test-automation

# Check: https://github.com/YourUser/YourRepo/actions
```

---

## 📚 Examples Provided

Check the `examples/` directory:

- `nodejs-pre-commit` - Complete Node.js example
- `nodejs-github-actions.yml` - Node.js CI/CD
- `java-pre-commit` - Complete Java/Maven example
- `universal-pre-commit-template.sh` - Language-agnostic template

---

## 🤝 Contributing Your Adaptations

Found a good setup for another language? Share it!

```bash
# Add your example
cp .git/hooks/pre-commit examples/golang-pre-commit

# Submit PR
git add examples/
git commit -m "Add Go pre-commit example"
git push
```

---

## ❓ FAQ

**Q: Do I need all three layers (pre-commit, pre-push, GitHub Actions)?**  
A: No. Start with one:

- Minimum: GitHub Actions only
- Better: Pre-commit + GitHub Actions
- Best: All three layers

**Q: Can I use this in a monorepo?**  
A: Yes! Place hooks at the repo root and check which directory changed:

```bash
CHANGED_FILES=$(git diff --cached --name-only)
if echo "$CHANGED_FILES" | grep -q "^frontend/"; then
    # Run frontend checks
fi
```

**Q: What if my team doesn't have the same tools installed?**  
A: Use Docker:

```bash
# Instead of: python check_compatibility.py
# Use: docker run python:3.11 python check_compatibility.py
```

**Q: Can I run checks in parallel?**  
A: Yes!

```bash
# Run linter and tests simultaneously
(npm run lint) & (npm test) & wait
```

---

## 🎉 Summary

| Project Type           | Setup Time | What to Copy       | What to Customize |
| ---------------------- | ---------- | ------------------ | ----------------- |
| **Python (similar)**   | 2 min      | Everything         | Import list only  |
| **Python (different)** | 5 min      | Everything         | Imports + files   |
| **Node.js**            | 10 min     | Templates          | All commands      |
| **Java**               | 10 min     | Templates          | All commands      |
| **Other**              | 15 min     | Universal template | Everything        |

**Bottom line:** Spend 10 minutes now, save hours later! 🚀

---

## 📖 Additional Resources

- **Git Hooks**: https://git-scm.com/book/en/v2/Customizing-Git-Git-Hooks
- **GitHub Actions**: https://docs.github.com/en/actions
- **Pre-commit Framework**: https://pre-commit.com/ (alternative tool)
- **Husky** (Node.js): https://typicode.github.io/husky/ (alternative)

---

**Need help?** Open an issue or PR at:  
https://github.com/RubyJane88/genai-security-maturity-explorer/issues
