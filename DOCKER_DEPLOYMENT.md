# Docker Deployment Guide

If Render.com continues to use Python 3.13 despite configuration, use Docker deployment instead.

## ✅ Option 1: Render with Docker

1. **Update render.yaml** to use Docker:

```yaml
services:
  - type: web
    name: genai-security-maturity-explorer
    runtime: docker
    plan: free
    dockerfilePath: ./Dockerfile
    dockerContext: .
```

2. Commit and push:

```bash
git add Dockerfile render.yaml
git commit -m "Switch to Docker deployment"
git push origin main
```

3. Render will automatically rebuild using Docker

## ✅ Option 2: Test Docker Locally

```bash
# Build image
docker build -t genai-maturity .

# Run container
docker run -p 8050:8050 genai-maturity

# Access at http://localhost:8050
```

## ✅ Option 3: Deploy to Other Platforms

### Fly.io (Free tier available)

```bash
# Install flyctl
curl -L https://fly.io/install.sh | sh

# Launch app
fly launch

# Deploy
fly deploy
```

### Railway (Free tier)

1. Go to https://railway.app
2. Click "New Project"
3. Connect GitHub repo
4. Railway auto-detects Dockerfile
5. Deploy!

## Why Docker?

- ✅ **Complete control** over Python version
- ✅ **Same environment** locally and in production
- ✅ **No surprises** - what works locally works deployed
- ✅ **Platform independent** - works on Render, Fly.io, Railway, AWS, etc.

## Current Status

The project includes:

- `Dockerfile` - Production-ready Docker configuration
- `render.yaml` - Can be switched to Docker mode
- `.python-version` & `runtime.txt` - For native Python builds

Choose whichever deployment method works best!
