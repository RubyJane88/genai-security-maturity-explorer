#!/bin/bash
# Pre-deployment compatibility checker for GenAI Security Maturity Explorer
# Run this script before pushing to catch compatibility issues early

set -e  # Exit on any error

echo "🔍 Python Compatibility Checker"
echo "================================"
echo ""

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# 1. Check Python version
echo "1️⃣  Checking Python version..."
PYTHON_VERSION=$(python --version 2>&1 | awk '{print $2}')
echo "   Current: Python $PYTHON_VERSION"

MAJOR=$(echo $PYTHON_VERSION | cut -d. -f1)
MINOR=$(echo $PYTHON_VERSION | cut -d. -f2)

if [ "$MAJOR" -eq 3 ] && [ "$MINOR" -eq 11 ]; then
    echo -e "   ${GREEN}✅ Python 3.11 detected (recommended)${NC}"
elif [ "$MAJOR" -eq 3 ] && [ "$MINOR" -ge 9 ] && [ "$MINOR" -le 12 ]; then
    echo -e "   ${YELLOW}⚠️  Python 3.$MINOR works, but 3.11 recommended for deployment${NC}"
else
    echo -e "   ${RED}❌ Python $PYTHON_VERSION may have compatibility issues${NC}"
    echo "   Recommendation: Use Python 3.11"
fi
echo ""

# 2. Check if virtual environment is activated
echo "2️⃣  Checking virtual environment..."
if [ -n "$VIRTUAL_ENV" ]; then
    echo -e "   ${GREEN}✅ Virtual environment active: $VIRTUAL_ENV${NC}"
else
    echo -e "   ${RED}❌ No virtual environment detected${NC}"
    echo "   Run: source venv/bin/activate"
    exit 1
fi
echo ""

# 3. Check for requirements.txt
echo "3️⃣  Checking requirements.txt..."
if [ -f "requirements.txt" ]; then
    echo -e "   ${GREEN}✅ requirements.txt found${NC}"
    echo "   Packages:"
    while IFS= read -r line; do
        if [[ ! "$line" =~ ^# ]] && [ ! -z "$line" ]; then
            echo "      - $line"
        fi
    done < requirements.txt
else
    echo -e "   ${RED}❌ requirements.txt not found${NC}"
    exit 1
fi
echo ""

# 4. Test install in dry-run mode
echo "4️⃣  Simulating package installation (dry-run)..."
pip install --dry-run -r requirements.txt > /dev/null 2>&1
if [ $? -eq 0 ]; then
    echo -e "   ${GREEN}✅ All packages resolve successfully${NC}"
else
    echo -e "   ${RED}❌ Package resolution failed${NC}"
    echo "   Run: pip install -r requirements.txt (to see details)"
    exit 1
fi
echo ""

# 5. Check for conflicting dependencies
echo "5️⃣  Checking for dependency conflicts..."
pip check > /dev/null 2>&1
if [ $? -eq 0 ]; then
    echo -e "   ${GREEN}✅ No dependency conflicts detected${NC}"
else
    echo -e "   ${YELLOW}⚠️  Dependency conflicts found:${NC}"
    pip check
fi
echo ""

# 6. Verify key imports work
echo "6️⃣  Testing critical imports..."
python -c "import dash; import plotly; import pandas; import numpy; print('   ✅ All critical packages import successfully')" 2>&1
if [ $? -ne 0 ]; then
    echo -e "   ${RED}❌ Import test failed${NC}"
    exit 1
fi
echo ""

# 7. Check if app.py has syntax errors
echo "7️⃣  Checking app.py syntax..."
python -m py_compile app.py 2>&1
if [ $? -eq 0 ]; then
    echo -e "   ${GREEN}✅ app.py has no syntax errors${NC}"
else
    echo -e "   ${RED}❌ Syntax errors found in app.py${NC}"
    exit 1
fi
echo ""

# 8. Generate dependency tree
echo "8️⃣  Analyzing dependency tree..."
if command -v pipdeptree &> /dev/null; then
    echo "   Dependency tree (showing potential conflicts):"
    pipdeptree --warn fail > /tmp/deptree.txt 2>&1
    if [ $? -eq 0 ]; then
        echo -e "   ${GREEN}✅ No circular dependencies or conflicts${NC}"
    else
        echo -e "   ${YELLOW}⚠️  Potential issues detected:${NC}"
        cat /tmp/deptree.txt | grep -i "warning\|conflict" || echo "   (See full output with: pipdeptree)"
    fi
else
    echo -e "   ${YELLOW}⚠️  pipdeptree not installed (optional check skipped)${NC}"
    echo "   Install with: pip install pipdeptree"
fi
echo ""

# 9. Security vulnerability check
echo "9️⃣  Checking for security vulnerabilities..."
if command -v safety &> /dev/null; then
    safety check --json > /tmp/safety.json 2>&1
    VULNS=$(cat /tmp/safety.json | grep -o '"vulnerabilities_found": [0-9]*' | grep -o '[0-9]*')
    if [ "$VULNS" = "0" ]; then
        echo -e "   ${GREEN}✅ No known security vulnerabilities${NC}"
    else
        echo -e "   ${YELLOW}⚠️  $VULNS security vulnerabilities found${NC}"
        echo "   Run: safety check --full-report"
    fi
else
    echo -e "   ${YELLOW}⚠️  safety not installed (optional check skipped)${NC}"
    echo "   Install with: pip install safety"
fi
echo ""

# 10. Compare with production environment
echo "🔟 Deployment environment check..."
echo "   Target: Render.com (Python 3.11, Linux x86_64)"
if [ -f ".python-version" ]; then
    DEPLOY_VERSION=$(cat .python-version)
    echo "   Specified deployment Python: $DEPLOY_VERSION"
    if [ "$DEPLOY_VERSION" = "3.11.0" ] || [ "$DEPLOY_VERSION" = "3.11" ]; then
        echo -e "   ${GREEN}✅ Deployment Python version is stable${NC}"
    else
        echo -e "   ${YELLOW}⚠️  Consider using Python 3.11 for deployment${NC}"
    fi
else
    echo -e "   ${YELLOW}⚠️  .python-version file not found${NC}"
fi
echo ""

# Summary
echo "================================"
echo "📊 Compatibility Check Summary"
echo "================================"
echo ""
echo "All critical checks passed! Safe to deploy. 🚀"
echo ""
echo "💡 Tips:"
echo "   • Always test locally before pushing"
echo "   • Monitor Render.com build logs"
echo "   • Keep dependencies updated regularly"
echo ""
