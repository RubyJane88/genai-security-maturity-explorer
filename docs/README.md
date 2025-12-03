# Documentation Index

This directory contains comprehensive documentation for the GenAI Security Maturity Explorer project.

## 📚 Available Documents

### For Developers

- **[DEPLOYMENT_DEBUGGING_STORY.md](./DEPLOYMENT_DEBUGGING_STORY.md)** 🔥 **NEW!**
  - Real-world debugging experience with hidden dashboard overrides
  - Configuration precedence hierarchy across cloud platforms
  - Best practices and checklists for deployment troubleshooting
  - Perfect for blog posts or learning materials

- **[COMPATIBILITY_GUIDE.md](./COMPATIBILITY_GUIDE.md)**
  - Why Python dependency issues happen
  - Prevention strategies and troubleshooting matrix
  - Understanding the dependency chain problem

- **[DOCKER_DEPLOYMENT.md](./DOCKER_DEPLOYMENT.md)**
  - Docker-specific deployment instructions
  - Why Docker guarantees Python version consistency
  - Render.com Docker deployment guide

### For Automation

- **[AUTOMATION_GUIDE.md](./AUTOMATION_GUIDE.md)**
  - Git hooks setup (pre-commit, pre-push)
  - GitHub Actions CI/CD pipeline
  - Compatibility checking system

- **[AUTOMATION_SUMMARY.md](./AUTOMATION_SUMMARY.md)**
  - Quick reference for automation features
  - One-page overview of all checks

- **[REUSABILITY_GUIDE.md](./REUSABILITY_GUIDE.md)**
  - Using automation in other projects
  - Templates for Python, Node.js, Java, universal

### Post-Deployment

- **[POST_DEPLOYMENT.md](./POST_DEPLOYMENT.md)**
  - Checklist for after successful deployment
  - Screenshot capture, URL verification, feature testing

## 🎯 Quick Links by Use Case

### "I want to deploy this project"
1. Start with [DOCKER_DEPLOYMENT.md](./DOCKER_DEPLOYMENT.md)
2. Check [DEPLOYMENT_DEBUGGING_STORY.md](./DEPLOYMENT_DEBUGGING_STORY.md) if issues arise
3. Use [POST_DEPLOYMENT.md](./POST_DEPLOYMENT.md) after success

### "I'm having deployment issues"
1. Read [DEPLOYMENT_DEBUGGING_STORY.md](./DEPLOYMENT_DEBUGGING_STORY.md) **FIRST!**
2. Check platform dashboard settings before debugging code
3. Consult [COMPATIBILITY_GUIDE.md](./COMPATIBILITY_GUIDE.md) for dependency issues

### "I want to reuse the automation"
1. Follow [REUSABILITY_GUIDE.md](./REUSABILITY_GUIDE.md)
2. Check templates in `../examples/` directory
3. Reference [AUTOMATION_GUIDE.md](./AUTOMATION_GUIDE.md) for customization

### "I want to write a blog post"
- [DEPLOYMENT_DEBUGGING_STORY.md](./DEPLOYMENT_DEBUGGING_STORY.md) is ready to publish or adapt
- Includes title ideas, key angles, and viral elements
- All lessons learned documented with technical depth

## 💡 Highlighted Insights

### From the Debugging Story
> "The answer was in line 1 of the error, but we spent hours on line 50"

**Key Lesson:** Platform UI settings (dashboard) take precedence over config files, which override code. This is the **industry standard** across Render, Vercel, Heroku, AWS, and more.

### Configuration Precedence Hierarchy
```
1. 🔴 Dashboard/UI Settings (highest priority)
2. 🟠 Platform Config Files (render.yaml, vercel.json)
3. 🟡 Runtime Files (Dockerfile, Procfile)
4. 🟢 Application Code (lowest priority)
```

**Always check from top to bottom when debugging deployments!**

## 🤝 Contributing

If you discover additional deployment gotchas or debugging patterns, please:
1. Document them thoroughly
2. Add to this index
3. Submit a PR with your findings

## 📝 License

All documentation in this directory is part of the GenAI Security Maturity Explorer project and follows the same MIT License as the main repository.

---

**Last Updated:** December 3, 2025  
**Maintainer:** Ruby Jane Cabagnot
