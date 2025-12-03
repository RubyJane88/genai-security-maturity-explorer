# 🔄 Universal Automation Template

This is a **language-agnostic template** for pre-commit/pre-push hooks.  
Customize the commands for your specific language and tools.

## 📋 Template Structure

```bash
#!/bin/bash
# Universal pre-commit hook template
# Customize sections 1-6 for your project

set -e  # Exit on any error

echo "🔍 Running pre-commit checks..."
echo ""

# ============================================
# 1. CHECK LANGUAGE VERSION
# ============================================
echo "1️⃣  Checking language version..."

# CUSTOMIZE THIS:
# Python:   python --version
# Node.js:  node --version
# Java:     java -version
# Go:       go version
# Ruby:     ruby --version
# Rust:     rustc --version

LANGUAGE_VERSION=$(python --version 2>&1)  # ← CHANGE ME
echo "   Current: $LANGUAGE_VERSION"

# Add version validation logic here
echo "   ✅ Version check passed"
echo ""

# ============================================
# 2. CHECK DEPENDENCIES INSTALLED
# ============================================
echo "2️⃣  Checking dependencies..."

# CUSTOMIZE THIS:
# Python:   check for venv/requirements.txt
# Node.js:  check for node_modules/package.json
# Java:     check for pom.xml/build.gradle
# Go:       check for go.mod
# Ruby:     check for Gemfile
# Rust:     check for Cargo.toml

if [ -f "requirements.txt" ]; then  # ← CHANGE ME
    echo "   ✅ Dependencies configuration found"
else
    echo "   ❌ Dependencies configuration not found"
    exit 1
fi
echo ""

# ============================================
# 3. RUN LINTER/CODE STYLE CHECK
# ============================================
echo "3️⃣  Running code style checks..."

# CUSTOMIZE THIS:
# Python:   flake8, black, pylint
# Node.js:  eslint, prettier
# Java:     checkstyle, spotless
# Go:       gofmt, golint
# Ruby:     rubocop
# Rust:     rustfmt, clippy

# Example for Python:
# python -m flake8 .

echo "   ⚠️  Linter not configured (skipped)"
echo ""

# ============================================
# 4. RUN TESTS
# ============================================
echo "4️⃣  Running tests..."

# CUSTOMIZE THIS:
# Python:   pytest, unittest
# Node.js:  npm test, jest
# Java:     mvn test, gradle test
# Go:       go test ./...
# Ruby:     rake test, rspec
# Rust:     cargo test

# Example for Python:
# pytest tests/

echo "   ⚠️  Tests not configured (skipped)"
echo ""

# ============================================
# 5. CHECK SYNTAX/COMPILATION
# ============================================
echo "5️⃣  Checking syntax..."

# CUSTOMIZE THIS:
# Python:   python -m py_compile *.py
# Node.js:  tsc --noEmit (TypeScript)
# Java:     mvn compile
# Go:       go build
# Ruby:     ruby -c *.rb
# Rust:     cargo check

python -m py_compile app.py  # ← CHANGE ME
if [ $? -eq 0 ]; then
    echo "   ✅ No syntax errors"
else
    echo "   ❌ Syntax errors found"
    exit 1
fi
echo ""

# ============================================
# 6. SECURITY/VULNERABILITY CHECK
# ============================================
echo "6️⃣  Checking for vulnerabilities..."

# CUSTOMIZE THIS:
# Python:   safety check, bandit
# Node.js:  npm audit
# Java:     mvn dependency-check
# Go:       go list -json -m all | nancy
# Ruby:     bundle audit
# Rust:     cargo audit

echo "   ⚠️  Security scan not configured (skipped)"
echo ""

# ============================================
# SUMMARY
# ============================================
echo "✅ All pre-commit checks passed!"
echo ""

exit 0
