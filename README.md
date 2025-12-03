# GenAI Security Maturity Explorer 🛡️

[![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)](https://www.python.org/)
[![Dash](https://img.shields.io/badge/Dash-2.14-green.svg)](https://dash.plotly.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Live Demo](https://img.shields.io/badge/Live-Demo-brightgreen.svg)](https://genai-security-maturity-explorer.onrender.com)
[![Compatibility Checks](https://github.com/RubyJane88/genai-security-maturity-explorer/actions/workflows/compatibility-check.yml/badge.svg)](https://github.com/RubyJane88/genai-security-maturity-explorer/actions/workflows/compatibility-check.yml)

An interactive dashboard for visualizing the **Three-Dimensional Maturity Assessment** of Generative AI security risks, based on the master's research paper _"Security Risks in Generative AI"_ by Ruby Jane Cabagnot (2025).

**🌐 Live Demo**: [https://genai-security-maturity-explorer.onrender.com](https://genai-security-maturity-explorer.onrender.com)

> ⚠️ **Note**: Free tier apps sleep after 15 minutes of inactivity. First load may take 30-60 seconds to wake up.

![Dashboard Preview](assets/preview.png)

## 🎯 Overview

This dashboard presents a sociotechnical maturity assessment framework that evaluates GenAI threats across four dimensions:

| Dimension                   | Description                                           |
| --------------------------- | ----------------------------------------------------- |
| **Threat Maturity**         | How sophisticated and prevalent the threat has become |
| **Technical Controls**      | Effectiveness of technical defenses and mitigations   |
| **Governance Enforcement**  | Regulatory frameworks and policy implementation       |
| **Stakeholder Protections** | Legal remedies and protections for affected parties   |

### Key Finding

> _"Threats consistently reach Level 4 (mature) while protections lag at Levels 0-2, with stakeholder protection representing the most severe deficit."_

## 📌 Executive Summary: Why This Matters

Generative AI systems are being rapidly deployed across critical sectors—from healthcare to finance, education to public services—yet **security protections are dangerously lagging behind emerging threats**. This dashboard reveals a stark reality:

### The Crisis

- **Threat Sophistication**: Attacks like prompt injection and privacy breaches have reached industrial maturity (Level 4)
- **Protection Gap**: Average 3.5-point gap between threat capabilities and defensive measures
- **Stakeholder Vulnerability**: End users have virtually no legal protections (averaging Level 0.5)
- **Governance Void**: Regulatory frameworks remain undefined or unenforced (Levels 0-1)

### The Impact

Without coordinated action, we face:

- **Mass Privacy Violations**: Training data extraction exposing sensitive personal information
- **Automated Manipulation**: Scaled disinformation campaigns undermining democratic processes
- **Liability Black Holes**: No clear accountability when AI systems cause harm
- **Trust Erosion**: Public confidence in AI systems collapsing due to repeated security failures

### The Solution

This tool enables **evidence-based decision-making** by:

1. **Quantifying the gap** between threats and protections with academic rigor
2. **Modeling future scenarios** to prioritize investments and policy interventions
3. **Tracking progress** as technical, regulatory, and legal frameworks evolve
4. **Facilitating dialogue** between technologists, policymakers, and civil society

## 👥 Who Should Use This Tool

### 🏢 **Policymakers & Regulators**

- **Use Case**: Prioritize which AI security domains need urgent regulatory attention
- **Benefit**: Understand where enforcement gaps create the most risk to citizens
- **Example**: EU AI Act implementation teams assessing compliance readiness

### 🔒 **Security Teams & Risk Managers**

- **Use Case**: Conduct AI risk assessments and justify security budget allocations
- **Benefit**: Compare your organization's defenses against industry maturity benchmarks
- **Example**: CISOs presenting board-level risk reports on GenAI deployments

### 🎓 **Researchers & Academics**

- **Use Case**: Identify research gaps and emerging threat vectors
- **Benefit**: Access synthesized data from 46+ authoritative sources in one dashboard
- **Example**: PhD students studying AI governance or doctoral committees reviewing thesis work

### 💼 **Technology Leaders & Product Managers**

- **Use Case**: Make informed decisions about AI system design and deployment
- **Benefit**: Understand full lifecycle security requirements beyond technical controls
- **Example**: AI startup founders designing responsible AI architectures

### 🏛️ **Civil Society & Advocacy Groups**

- **Use Case**: Hold organizations accountable for AI safety claims
- **Benefit**: Access evidence-based data to support policy advocacy efforts
- **Example**: Digital rights organizations campaigning for stronger AI protections

### 📰 **Journalists & Public Educators**

- **Use Case**: Explain complex AI security issues to general audiences
- **Benefit**: Visual storytelling tool with credible academic foundations
- **Example**: Tech journalists covering AI safety and regulation stories

## 🚀 Quick Start

### Prerequisites

- Python 3.9 or higher
- pip package manager

### Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/RubyJane88/genai-security-maturity-explorer.git
   cd genai-security-maturity-explorer
   ```

2. **Create and activate virtual environment**

   ```bash
   # Create virtual environment
   python3 -m venv venv

   # Activate (macOS/Linux)
   source venv/bin/activate

   # Activate (Windows)
   venv\Scripts\activate
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**

   ```bash
   python app.py
   ```

5. **Open your browser**
   Navigate to `http://localhost:8050`

## 📊 Features

### Interactive Heatmap

- **Hover** over cells to see detailed evidence and references
- **Click** on threat categories for comprehensive analysis
- Color-coded maturity levels (0-4 scale)

### Controls

- 📅 **Year Selector**: Compare 2025 baseline with 2026-2027 projections
- 🔬 **What-If Simulation**: Model the impact of improved governance
- 🌓 **Dark/Light Mode**: Toggle display theme
- 📥 **Export**: Download visualizations as PNG

### Analysis Views

- **Protection Gap Chart**: Visualize the disparity between threats and defenses
- **Radar Charts**: Detailed threat profiles by category
- **Quick Statistics**: Summary metrics at a glance

## 🗂️ Project Structure

```
genai-security-maturity-explorer/
├── app.py                 # Main Dash application
├── requirements.txt       # Python dependencies
├── README.md             # This file
├── LICENSE               # MIT License
├── Procfile              # For Heroku/Render deployment
├── render.yaml           # Render.com configuration
├── runtime.txt           # Python version specification
├── assets/
│   └── custom.css        # Custom styling
└── data/
    └── maturity_data.json # Maturity assessment data
```

## 🌐 Deployment

### Render.com (Recommended - Free Tier)

1. Fork this repository
2. Create account at [render.com](https://render.com)
3. Click **New → Web Service**
4. Connect your GitHub repository
5. Render will auto-detect settings from `render.yaml`
6. Click **Create Web Service**

### Netlify (Alternative - Free Tier)

**Note**: Netlify is designed for static sites, but can host Python apps using serverless functions. For Dash apps, Render or Heroku are better suited, but here's how to deploy on Netlify:

**Option 1: Using Netlify Functions (Requires Refactoring)**

1. Refactor Dash app to use serverless functions
2. Create `netlify.toml`:

   ```toml
   [build]
     command = "pip install -r requirements.txt"
     publish = "public"

   [[redirects]]
     from = "/*"
     to = "/.netlify/functions/app/:splat"
     status = 200
   ```

**Option 2: Use Render Instead** ⭐ **Recommended**

- Netlify doesn't natively support long-running Python web servers
- Render.com offers better support for Dash/Flask applications
- Both have free tiers with similar features

### Heroku

```bash
heroku create genai-maturity-explorer
git push heroku main
heroku open
```

### Docker

```bash
docker build -t genai-maturity .
docker run -p 8050:8050 genai-maturity
```

### Deployment Comparison

| Platform       | Free Tier    | Best For          | Python/Dash Support       |
| -------------- | ------------ | ----------------- | ------------------------- |
| **Render.com** | ✅ 750hrs/mo | Web apps & APIs   | ⭐⭐⭐⭐⭐ Native         |
| **Heroku**     | ⚠️ Limited   | Rapid prototyping | ⭐⭐⭐⭐ Native           |
| **Netlify**    | ✅ Unlimited | Static sites      | ⭐⭐ Requires workarounds |
| **Docker**     | N/A          | Self-hosting      | ⭐⭐⭐⭐⭐ Full control   |

### 📸 Post-Deployment Steps

After your app is live on Render.com:

1. **Update the Live URL** (if different from default):
   - Copy your actual Render URL
   - Update the URL in the badges and "Live Demo" section at the top of this README
2. **Add Dashboard Screenshot**:

   - Visit your live dashboard
   - Take a screenshot showing the heatmap and controls
   - Save as `assets/preview.png`
   - Commit and push:
     ```bash
     git add assets/preview.png
     git commit -m "docs: Add dashboard preview screenshot"
     git push origin main
     ```

3. **Test the deployment**:
   - Verify all interactive features work
   - Check hover tooltips and click modals
   - Test year selector and dark mode toggle

## 📚 Data Sources

The maturity assessment synthesizes 46 academic and regulatory sources, including:

- **Academic Literature**: ACM Computing Surveys, IEEE S&P, NeurIPS, FAccT
- **Regulatory Documents**: EU AI Act, NIST AI RMF, EDPB Guidelines
- **Incident Databases**: AI Incident Database, CVE records
- **Industry Reports**: OWASP Top 10 for LLMs, vendor security advisories

### Key References

| Category         | Representative Sources                        |
| ---------------- | --------------------------------------------- |
| Prompt Injection | Greshake et al. (2023), Reddy & Gujral (2025) |
| Privacy          | Carlini et al. (2024), Liu et al. (2024)      |
| Governance       | European Commission (2024), NIST (2024)       |
| Harms Taxonomy   | Weidinger et al. (2022), Shelby et al. (2023) |

## 🔬 Methodology

The Three-Dimensional Maturity Assessment uses a 0-4 scale:

| Level | Name           | Description                                      |
| ----- | -------------- | ------------------------------------------------ |
| 0     | Non-existent   | No capability or protection present              |
| 1     | Initial        | Ad-hoc, reactive responses only                  |
| 2     | Developing     | Some processes defined, inconsistent application |
| 3     | Defined        | Standardized processes, proactive measures       |
| 4     | Managed/Mature | Optimized, measurable, continuously improved     |

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

### Future Updates

- [ ] Add 2026 empirical data when available
- [ ] Include additional threat categories
- [ ] API endpoint for programmatic access
- [ ] Integration with AI Incident Database

## 📖 Citation

If you use this dashboard or the underlying research, please cite:

```bibtex
@mastersthesis{cabagnot2025security,
  author  = {Cabagnot, Ruby Jane},
  title   = {Security Risks in Generative AI: A Sociotechnical Maturity Assessment},
  school  = {[OsloMet University, Oslo, Norway]]},
  year    = {2025},
  type    = {Master's Research Paper on Cybersecurity & Privacy}
}
```

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👤 Author

**Ruby Jane Cabagnot**

- GitHub: [@RubyJane88](https://github.com/RubyJane88)

---

<p align="center">
  <em>Built with ❤️ using Plotly Dash</em>
</p>
