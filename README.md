# GenAI Security Maturity Explorer 🛡️

[![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)](https://www.python.org/)
[![Dash](https://img.shields.io/badge/Dash-2.14-green.svg)](https://dash.plotly.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

An interactive dashboard for visualizing the **Three-Dimensional Maturity Assessment** of Generative AI security risks, based on the master's thesis _"Security Risks in Generative AI"_ by Ruby Jane Cabagnot (2025).

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
  school  = {[University Name]},
  year    = {2025},
  type    = {Master's Thesis}
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
