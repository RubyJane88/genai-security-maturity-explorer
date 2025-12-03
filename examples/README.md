# 📦 Automation Examples

This directory contains **ready-to-use automation scripts** for different programming languages and frameworks.

## 📋 Available Examples

### Python

- `../check_compatibility.py` - Full Python compatibility checker (in root)
- `../check_compatibility.sh` - Bash version (in root)

### Node.js/JavaScript

- `nodejs-pre-commit` - Complete pre-commit hook for Node.js projects
- `nodejs-github-actions.yml` - GitHub Actions workflow for Node.js

### Java/Maven

- `java-pre-commit` - Complete pre-commit hook for Java/Maven projects

### Universal

- `universal-pre-commit-template.sh` - Language-agnostic template you can customize

## 🚀 How to Use

### Option 1: Copy Directly

```bash
# For Node.js project
cp examples/nodejs-pre-commit /path/to/your-project/.git/hooks/pre-commit
chmod +x /path/to/your-project/.git/hooks/pre-commit

# For Java project
cp examples/java-pre-commit /path/to/your-project/.git/hooks/pre-commit
chmod +x /path/to/your-project/.git/hooks/pre-commit
```

### Option 2: Use as Template

```bash
# Copy universal template
cp examples/universal-pre-commit-template.sh .git/hooks/pre-commit

# Edit for your language
vim .git/hooks/pre-commit

# Make executable
chmod +x .git/hooks/pre-commit
```

### Option 3: Customize Python Scripts

```bash
# Copy to your Python project
cp check_compatibility.py /path/to/your-project/
cd /path/to/your-project/

# Edit critical imports (line ~115)
vim check_compatibility.py

# Run
python check_compatibility.py
```

## 📚 Documentation

See the comprehensive guides:

- `../REUSABILITY_GUIDE.md` - How to adapt for any project
- `../AUTOMATION_GUIDE.md` - Complete automation documentation
- `../COMPATIBILITY_GUIDE.md` - Why issues happen + solutions

## 🎯 Quick Reference

| Your Project   | Use This File                      | Time to Setup |
| -------------- | ---------------------------------- | ------------- |
| Python         | `../check_compatibility.py`        | 2 minutes     |
| Node.js        | `nodejs-pre-commit`                | 5 minutes     |
| Java/Maven     | `java-pre-commit`                  | 5 minutes     |
| Other language | `universal-pre-commit-template.sh` | 10 minutes    |

## 🔧 Customization Points

When adapting to your project, update:

1. **Language version check** (Section 1)
2. **Dependencies check** (Section 2)
3. **Linter command** (Section 3)
4. **Test command** (Section 4)
5. **Build/compile command** (Section 5)
6. **Security scan** (Section 6)

## 💡 Tips

- **Test first**: Run the hook manually before committing

  ```bash
  .git/hooks/pre-commit
  ```

- **Start simple**: Don't add all checks at once. Start with:

  1. Version check
  2. Syntax check
  3. Add more as needed

- **Keep it fast**: Pre-commit should be < 30 seconds

  - Quick checks: pre-commit hook
  - Slow checks: GitHub Actions

- **Document it**: Add to your project README:

  ````markdown
  ## Development

  Automated checks are enabled. To install:

  ```bash
  ./setup_checks.sh
  ```
  ````

  ```

  ```

## 🤝 Contributing

Have a good setup for another language? Add it here!

```bash
# Add your example
cp .git/hooks/pre-commit examples/your-language-pre-commit

# Submit PR
git add examples/
git commit -m "Add [Language] pre-commit example"
```

## 🌟 Future Examples to Add

Want to contribute? These would be helpful:

- [ ] Go/Golang
- [ ] Ruby/Rails
- [ ] Rust
- [ ] PHP/Laravel
- [ ] C#/.NET
- [ ] Swift
- [ ] Kotlin
- [ ] TypeScript (separate from Node.js)

---

**Need help?** Check `../REUSABILITY_GUIDE.md` for detailed instructions!
