#!/bin/bash
# Setup script for automated deployment checks
# Run once after cloning the repository

set -e

echo "🔧 Setting up automated deployment checks..."
echo ""

# Make sure we're in the repo root
cd "$(git rev-parse --show-toplevel)"

# Make hooks executable
echo "📝 Installing Git hooks..."
chmod +x .git/hooks/pre-commit
chmod +x .git/hooks/pre-push
echo "   ✓ Pre-commit hook installed"
echo "   ✓ Pre-push hook installed"
echo ""

# Make compatibility checkers executable
echo "🔍 Setting up compatibility checkers..."
chmod +x check_compatibility.sh
chmod +x check_compatibility.py
echo "   ✓ check_compatibility.sh"
echo "   ✓ check_compatibility.py"
echo ""

# Check if virtual environment exists
if [ ! -d "venv" ]; then
    echo "📦 Creating virtual environment..."
    python3 -m venv venv
    echo "   ✓ Virtual environment created"
fi

# Activate virtual environment
echo "🐍 Activating virtual environment..."
source venv/bin/activate
echo "   ✓ Virtual environment activated"
echo ""

# Install dependencies
echo "📥 Installing dependencies..."
pip install --upgrade pip > /dev/null 2>&1
pip install -r requirements.txt
echo "   ✓ Dependencies installed"
echo ""

# Run compatibility check to verify setup
echo "🧪 Running compatibility check..."
python check_compatibility.py

echo ""
echo "✅ Setup complete!"
echo ""
echo "Automated checks are now enabled:"
echo "  • Pre-commit hook: Runs before every commit"
echo "  • Pre-push hook: Runs before every push"
echo "  • GitHub Actions: Runs on every push to main/develop"
echo ""
echo "To manually run checks:"
echo "  ./check_compatibility.sh    (quick bash check)"
echo "  python check_compatibility.py    (detailed Python check)"
echo ""
echo "To bypass hooks (not recommended):"
echo "  git commit --no-verify"
echo "  git push --no-verify"
echo ""
