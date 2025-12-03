# 📋 Post-Deployment Checklist

Complete these steps after your Render.com deployment is live!

## ✅ Step 1: Get Your Live URL

After Render.com finishes deploying, you'll see a URL like:
```
https://genai-security-maturity-explorer.onrender.com
```

**Copy this URL** - you'll need it for the next steps.

## ✅ Step 2: Take a Dashboard Screenshot

### Option A: From Local (Recommended)
1. Make sure your local app is running: `python app.py`
2. Open http://localhost:8050 in your browser
3. **Set it up nicely**:
   - Make sure the heatmap is visible
   - Year selector showing 2025
   - Maybe have one modal open or hover showing
   - Use dark mode (looks more professional!)
4. Take screenshot:
   - **macOS**: Press `Cmd + Shift + 4`, then `Space`, click window
   - **Windows**: Press `Windows + Shift + S`
   - **Full page**: Use browser extension like "Awesome Screenshot"

### Option B: From Live Site
1. Visit your Render URL (wait 30s if it's sleeping)
2. Follow same setup steps as Option A
3. Take screenshot

### Save the Screenshot
```bash
# Save your screenshot as preview.png in the assets folder
# Then run:
cd /Users/rubyjanecabagnot/Documents/genai-security-maturity-explorer
git add assets/preview.png
git commit -m "docs: Add dashboard preview screenshot"
git push origin main
```

## ✅ Step 3: Update README with Actual URL (if needed)

If your Render URL is different from the default, update these locations in README.md:

1. **Line 7** - Live Demo badge
2. **Line 11** - Direct URL link

The URLs are already set to the expected default. If Render gives you a different URL, just update these.

## ✅ Step 4: Test Everything

Visit your live dashboard and verify:
- [ ] Heatmap loads correctly
- [ ] Hover tooltips show detailed evidence
- [ ] Click on threat categories opens modal
- [ ] Year selector changes data (2025, 2026, 2027)
- [ ] Dark/Light mode toggle works
- [ ] Protection Gap chart displays
- [ ] Radar charts render properly
- [ ] Mobile responsive (check on phone)

## 🎉 Done!

Once completed:
1. Your dashboard is live and accessible worldwide
2. README shows a beautiful preview image
3. Anyone can click the Live Demo badge to try it

## 📝 Optional Enhancements

- [ ] Add custom domain (Render.com settings)
- [ ] Enable monitoring/analytics
- [ ] Share on LinkedIn/Twitter with screenshot
- [ ] Add to your portfolio website
- [ ] Submit to relevant AI/security communities

---

**Current Status**: Waiting for Render.com deployment to complete!

Once deployed, come back to this checklist and complete the steps. 🚀
