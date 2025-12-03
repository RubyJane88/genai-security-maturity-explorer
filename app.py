"""
GenAI Security Maturity Explorer – Interactive Dashboard
=========================================================
Based on "Security Risks in Generative AI" by Ruby Jane Cabagnot (2025)

A sociotechnical three-dimensional maturity assessment visualization tool
that demonstrates systematic gaps between threat sophistication and
protective mechanisms across the generative AI landscape.
"""

import dash
from dash import dcc, html, Input, Output, State, callback, ctx
import dash_bootstrap_components as dbc
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import numpy as np

# ============================================================================
# DATA STRUCTURE - Based on Figure 3 from Cabagnot (2025)
# ============================================================================

# Threat categories (rows) - exact order from thesis Figure 3
THREAT_CATEGORIES = [
    "Prompt Injection",
    "Autonomy Harms",
    "Political Integrity",
    "Privacy"
]

# Dimensions (columns)
DIMENSIONS = [
    "Threat Maturity",
    "Technical Controls",
    "Governance Enforcement",
    "Stakeholder Protections"
]

# Maturity data from Figure 3 (2025 Baseline) - EXACT values from thesis
MATURITY_DATA_2025 = {
    "Prompt Injection": [4.0, 2.5, 2.0, 0.5],
    "Autonomy Harms": [4.0, 2.0, 2.0, 0.5],
    "Political Integrity": [4.0, 1.0, 0.5, 0.5],
    "Privacy": [4.0, 2.0, 2.0, 2.0],
}

# Projected improvements for future years (hypothetical)
MATURITY_DATA_2026 = {
    "Prompt Injection": [4.0, 3.0, 2.5, 1.0],
    "Autonomy Harms": [4.0, 2.5, 2.5, 1.0],
    "Political Integrity": [4.0, 2.0, 1.5, 1.0],
    "Privacy": [4.0, 2.5, 2.5, 2.5],
}

MATURITY_DATA_2027 = {
    "Prompt Injection": [4.0, 3.5, 3.0, 2.0],
    "Autonomy Harms": [4.0, 3.0, 3.0, 1.5],
    "Political Integrity": [4.0, 2.5, 2.5, 1.5],
    "Privacy": [4.0, 3.0, 3.0, 3.0],
}

# Detailed evidence and references for each cell
CELL_DETAILS = {
    "Prompt Injection": {
        "description": "Attacks that manipulate LLM behavior through crafted inputs, including direct and indirect injection techniques that can compromise system integrity and user trust.",
        "incidents": [
            "EchoLeak CVE-2025-32711: First real-world zero-click prompt injection in production LLM (Reddy & Gujral, 2025)",
            "Bing Chat Sydney persona leak via prompt injection (Edwards, 2023)",
            "Chevrolet dealership chatbot manipulation - offered $1 car deal (Knight, 2024)"
        ],
        "dimensions": {
            "Threat Maturity": {
                "level": 4.0,
                "description": "Fully mature threat with automated exploitation tools",
                "evidence": [
                    "Indirect prompt injection compromises real-world LLM applications (Greshake et al., 2023)",
                    "Zero-click exploits now targeting production systems (Reddy & Gujral, 2025)",
                    "Exploitation pathway from lab to weaponized attack took <2 years"
                ],
                "references": ["Greshake et al., 2023", "Reddy & Gujral, 2025", "Wang et al., 2025"]
            },
            "Technical Controls": {
                "level": 2.5,
                "description": "Partial defenses exist but easily bypassed",
                "evidence": [
                    "Input sanitization and output filtering implemented by major providers",
                    "Defenses routinely bypassed by novel injection techniques",
                    "No provably robust defense against adaptive adversaries"
                ],
                "references": ["Das et al., 2025", "Wang et al., 2025", "Ferrag et al., 2025"]
            },
            "Governance Enforcement": {
                "level": 2.0,
                "description": "Guidelines exist but enforcement is weak",
                "evidence": [
                    "OWASP Top 10 for LLMs addresses prompt injection (OWASP, 2025)",
                    "EU AI Act requires security measures but implementation unclear",
                    "No mandatory security testing requirements for LLM deployments"
                ],
                "references": ["OWASP Foundation, 2025", "European Commission, 2024", "NIST, 2024"]
            },
            "Stakeholder Protections": {
                "level": 0.5,
                "description": "Almost no legal standing or remedy for victims",
                "evidence": [
                    "Non-users have no recourse when affected by LLM outputs",
                    "Section 230 shields platforms from most liability in US",
                    "Burden of proof on affected individuals is prohibitive"
                ],
                "references": ["Citron & Chesney, 2025", "Li et al., 2025", "NTIA, 2024"]
            }
        },
        "thesis_quote": "The exploitation pathway from laboratory proof-of-concept to weaponized zero-click vulnerability took less than two years—far outpacing protective response capabilities."
    },
    "Autonomy Harms": {
        "description": "Threats to human agency, decision-making autonomy, and cognitive independence from AI systems, including skill atrophy, over-reliance, and manipulation.",
        "incidents": [
            "Documented skill atrophy in developers over-relying on AI coding assistants",
            "ChatGPT influence on student critical thinking and learning processes",
            "AI-generated content flooding information ecosystems affecting human judgment"
        ],
        "dimensions": {
            "Threat Maturity": {
                "level": 4.0,
                "description": "Widespread autonomy erosion across domains",
                "evidence": [
                    "Documented skill atrophy in professionals using AI assistants",
                    "Educational integrity concerns reported across institutions globally",
                    "Cognitive offloading reducing human critical thinking capacity"
                ],
                "references": ["Bernstein et al., 2025", "Shelby et al., 2023", "Weidinger et al., 2022"]
            },
            "Technical Controls": {
                "level": 2.0,
                "description": "Limited technical solutions for autonomy protection",
                "evidence": [
                    "AI detection tools have high false positive rates",
                    "No effective technical barriers to over-reliance",
                    "Friction-adding UX patterns largely unexplored"
                ],
                "references": ["Bernstein et al., 2025", "Bommasani et al., 2024"]
            },
            "Governance Enforcement": {
                "level": 2.0,
                "description": "Emerging policies but no enforcement mechanisms",
                "evidence": [
                    "Educational institutions creating AI use policies",
                    "Professional bodies issuing guidance without enforcement",
                    "No regulatory framework for cognitive autonomy protection"
                ],
                "references": ["European Commission, 2024", "NIST, 2024", "OECD, 2024"]
            },
            "Stakeholder Protections": {
                "level": 0.5,
                "description": "No recognized right to cognitive autonomy",
                "evidence": [
                    "No legal framework protecting against autonomy harms",
                    "Affected individuals may not recognize their own diminished agency",
                    "Collective harms not actionable individually"
                ],
                "references": ["Citron & Chesney, 2025", "Bommasani et al., 2024", "AWO International, 2023"]
            }
        },
        "thesis_quote": "Autonomy harms represent a uniquely insidious category where the affected individuals may not recognize their own diminished agency."
    },
    "Political Integrity": {
        "description": "Threats to democratic processes, electoral systems, and political discourse from AI-generated content including deepfakes, synthetic media, and coordinated disinformation.",
        "incidents": [
            "Biden robocall deepfake urging voters to skip NH primary (NPR, 2024)",
            "AI-generated political disinformation campaigns in multiple countries",
            "Synthetic media targeting election integrity in 2024 cycles"
        ],
        "dimensions": {
            "Threat Maturity": {
                "level": 4.0,
                "description": "Active exploitation in electoral contexts globally",
                "evidence": [
                    "Documented use in 2024 election cycles across multiple countries",
                    "AI robocalls directly targeting voter behavior and turnout",
                    "Synthetic candidates and AI-generated campaign materials deployed"
                ],
                "references": ["NPR, 2024", "Li et al., 2025", "Trend Micro, 2024"]
            },
            "Technical Controls": {
                "level": 1.0,
                "description": "Detection tools unreliable for sophisticated fakes",
                "evidence": [
                    "Deepfake detection accuracy varies widely and lags generation",
                    "Real-time verification not feasible at scale",
                    "Watermarking standards (C2PA) adoption remains minimal"
                ],
                "references": ["Ferrag et al., 2025", "Golda et al., 2024", "Radanliev et al., 2025"]
            },
            "Governance Enforcement": {
                "level": 0.5,
                "description": "Minimal regulation of AI in political contexts",
                "evidence": [
                    "Few jurisdictions require AI disclosure in political ads",
                    "First Amendment concerns limit US government action",
                    "Cross-border enforcement nearly impossible"
                ],
                "references": ["NCSL, 2025", "Citron & Chesney, 2025", "European Commission, 2024"]
            },
            "Stakeholder Protections": {
                "level": 0.5,
                "description": "Voters and candidates lack effective remedies",
                "evidence": [
                    "No rapid response mechanism for electoral deepfakes",
                    "Damage occurs before content can be debunked",
                    "No cause of action for diffuse democratic harms"
                ],
                "references": ["NPR, 2024", "Li et al., 2025", "AWO International, 2023"]
            }
        },
        "thesis_quote": "The 3.5-level gap between threat maturity and stakeholder protection in political integrity represents perhaps the most acute democratic vulnerability in the generative AI era."
    },
    "Privacy": {
        "description": "Baseline comparison category showing traditional privacy protections that pre-date generative AI, demonstrating that established legal frameworks substantially narrow protection gaps.",
        "incidents": [
            "ChatGPT data breach exposing user conversations (OpenAI, 2023)",
            "Samsung employees leaking proprietary code via ChatGPT (Milmo, 2023)",
            "Training data extraction attacks revealing personal information"
        ],
        "dimensions": {
            "Threat Maturity": {
                "level": 4.0,
                "description": "Sophisticated privacy attacks well-documented",
                "evidence": [
                    "Membership inference and model inversion attacks mature",
                    "Training data extraction demonstrated at scale (Carlini et al.)",
                    "Unintentional memorization creates persistent privacy risks"
                ],
                "references": ["Carlini et al., 2024", "Liu et al., 2024", "Das et al., 2025"]
            },
            "Technical Controls": {
                "level": 2.0,
                "description": "Differential privacy and access controls exist",
                "evidence": [
                    "Major providers implementing privacy-preserving techniques",
                    "Effectiveness varies significantly across implementations",
                    "Trade-offs between privacy and model utility persist"
                ],
                "references": ["Liu et al., 2024", "Das et al., 2025", "Golda et al., 2024"]
            },
            "Governance Enforcement": {
                "level": 2.0,
                "description": "GDPR and emerging AI regulations apply",
                "evidence": [
                    "GDPR provides baseline protections in EU",
                    "EDPB guidance specifically addresses LLM privacy risks",
                    "Enforcement actions beginning against AI companies"
                ],
                "references": ["EDPB, 2025", "European Commission, 2024", "Veale & Borgesius, 2023"]
            },
            "Stakeholder Protections": {
                "level": 2.0,
                "description": "Established privacy rights provide some recourse",
                "evidence": [
                    "Data subject rights under GDPR enforceable",
                    "Class action mechanisms available in some jurisdictions",
                    "Pre-existing legal frameworks reduce protection gap by 1.5 levels"
                ],
                "references": ["EDPB, 2025", "Veale & Borgesius, 2023", "OECD, 2024"]
            }
        },
        "thesis_quote": "Privacy serves as a crucial baseline comparator, demonstrating that when legal frameworks predate the technology, protection gaps are substantially narrower—a key finding for policy development."
    }
}

# Maturity level descriptions
MATURITY_LEVELS = {
    0: "Non-existent",
    1: "Initial/Ad-hoc",
    2: "Developing",
    3: "Defined",
    4: "Managed/Mature"
}

def get_level_description(level):
    """Get description for a maturity level."""
    if level < 0.5:
        return "Non-existent"
    elif level < 1.5:
        return "Initial/Ad-hoc"
    elif level < 2.5:
        return "Developing"
    elif level < 3.5:
        return "Defined"
    else:
        return "Managed/Mature"

# ============================================================================
# APP INITIALIZATION
# ============================================================================

app = dash.Dash(
    __name__,
    external_stylesheets=[
        dbc.themes.DARKLY,
        dbc.icons.FONT_AWESOME,
        "https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap"
    ],
    suppress_callback_exceptions=True,
    meta_tags=[
        {"name": "viewport", "content": "width=device-width, initial-scale=1"},
        {"name": "description", "content": "Interactive dashboard for GenAI security maturity assessment based on Cabagnot (2025)"},
        {"property": "og:title", "content": "GenAI Security Maturity Explorer"},
        {"property": "og:description", "content": "A sociotechnical three-dimensional maturity assessment of generative AI security risks"}
    ]
)

app.title = "GenAI Security Maturity Explorer | Cabagnot 2025"
server = app.server  # For deployment (Render, Heroku, etc.)

# ============================================================================
# HELPER FUNCTIONS
# ============================================================================

def get_maturity_data(year):
    """Get maturity data for a specific year."""
    if year == "2025":
        return MATURITY_DATA_2025
    elif year == "2026":
        return MATURITY_DATA_2026
    elif year == "2027":
        return MATURITY_DATA_2027
    return MATURITY_DATA_2025


def create_heatmap(year="2025", governance_adjustment=0, dark_mode=True):
    """Create the main heatmap figure based on Figure 3 from the thesis."""
    data = get_maturity_data(year)
    
    # Build matrix
    z_values = []
    hover_texts = []
    
    for category in THREAT_CATEGORIES:
        row_values = data[category].copy()
        
        # Apply governance adjustment (affects Governance and Stakeholder columns)
        if governance_adjustment > 0:
            # Governance column (index 2)
            row_values[2] = min(4.0, row_values[2] + governance_adjustment * 0.5)
            # Stakeholder column (index 3) - smaller effect
            row_values[3] = min(4.0, row_values[3] + governance_adjustment * 0.3)
        
        z_values.append(row_values)
        
        # Build detailed hover text for each cell
        row_hover = []
        for i, dim in enumerate(DIMENSIONS):
            level = row_values[i]
            level_desc = get_level_description(level)
            
            # Get detailed evidence if available
            if category in CELL_DETAILS and dim in CELL_DETAILS[category]["dimensions"]:
                details = CELL_DETAILS[category]["dimensions"][dim]
                evidence = details.get("evidence", [])[:2]
                refs = details.get("references", [])[:2]
                evidence_text = "<br>• ".join([""] + evidence)
                refs_text = ", ".join(refs)
                hover = (
                    f"<b>{category}</b><br>"
                    f"<b>{dim}</b><br><br>"
                    f"<b>Level {level:.1f}</b>: {level_desc}<br>"
                    f"{evidence_text}<br><br>"
                    f"<i>References: {refs_text}</i>"
                )
            else:
                hover = (
                    f"<b>{category}</b><br>"
                    f"<b>{dim}</b><br><br>"
                    f"<b>Level {level:.1f}</b>: {level_desc}"
                )
            
            row_hover.append(hover)
        hover_texts.append(row_hover)
    
    # Color scale: red (0) → orange → yellow → light green → dark green (4)
    # Matching the thesis Figure 3 exactly
    colorscale = [
        [0, '#d73027'],      # Red (0)
        [0.25, '#fc8d59'],   # Orange (1)
        [0.5, '#fee08b'],    # Yellow (2)
        [0.75, '#d9ef8b'],   # Light green (3)
        [1, '#1a9850']       # Dark green (4)
    ]
    
    # Create heatmap figure
    fig = go.Figure(data=go.Heatmap(
        z=z_values,
        x=DIMENSIONS,
        y=THREAT_CATEGORIES,
        colorscale=colorscale,
        zmin=0,
        zmax=4,
        text=[[f"{v:.1f}" for v in row] for row in z_values],
        texttemplate="%{text}",
        textfont={"size": 16, "color": "black", "family": "Inter, sans-serif"},
        hovertemplate="%{customdata}<extra></extra>",
        customdata=hover_texts,
        colorbar=dict(
            title=dict(
                text="Maturity<br>Level",
                font=dict(size=12)
            ),
            titleside="right",
            tickvals=[0, 1, 2, 3, 4],
            ticktext=["0 - Non-existent", "1 - Initial", "2 - Developing", "3 - Defined", "4 - Mature"],
            len=0.75,
            thickness=20,
            x=1.02
        )
    ))
    
    # Update layout
    bg_color = "#1a1a2e" if dark_mode else "#ffffff"
    text_color = "#ffffff" if dark_mode else "#000000"
    grid_color = "#444444" if dark_mode else "#cccccc"
    
    year_label = f"{year} Baseline" if year == "2025" else f"{year} Projection"
    
    fig.update_layout(
        title=dict(
            text=f"<b>Maturity Levels Across Threats and Dimensions (0-4 Scale)</b><br><sup>{year_label}</sup>",
            font=dict(size=18, color=text_color, family="Inter, sans-serif"),
            x=0.5,
            xanchor="center"
        ),
        xaxis=dict(
            title=dict(
                text="Assessment Dimension",
                font=dict(size=14, color=text_color)
            ),
            tickfont=dict(size=12, color=text_color),
            side="bottom",
            tickangle=0
        ),
        yaxis=dict(
            title=dict(
                text="Threat Category",
                font=dict(size=14, color=text_color)
            ),
            tickfont=dict(size=12, color=text_color),
            autorange="reversed"
        ),
        paper_bgcolor=bg_color,
        plot_bgcolor=bg_color,
        height=450,
        margin=dict(l=150, r=120, t=100, b=80),
        font=dict(family="Inter, sans-serif")
    )
    
    return fig


def create_gap_analysis_chart(year="2025", dark_mode=True):
    """Create a bar chart showing the gap between threat maturity and protections."""
    data = get_maturity_data(year)
    
    categories = []
    gaps = []
    threat_levels = []
    protection_levels = []
    
    for cat in THREAT_CATEGORIES:
        threat_level = data[cat][0]
        avg_protection = np.mean(data[cat][1:])
        gap = threat_level - avg_protection
        
        categories.append(cat)
        gaps.append(gap)
        threat_levels.append(threat_level)
        protection_levels.append(avg_protection)
    
    bg_color = "#1a1a2e" if dark_mode else "#ffffff"
    text_color = "#ffffff" if dark_mode else "#000000"
    
    # Color based on gap severity
    colors = ['#d73027' if g > 2.5 else '#fc8d59' if g > 2 else '#fee08b' if g > 1.5 else '#d9ef8b' for g in gaps]
    
    fig = go.Figure(data=[
        go.Bar(
            x=categories,
            y=gaps,
            marker_color=colors,
            text=[f"{g:.1f}" for g in gaps],
            textposition="outside",
            textfont=dict(color=text_color, size=14, family="Inter, sans-serif"),
            hovertemplate=(
                "<b>%{x}</b><br>"
                "Threat Level: %{customdata[0]:.1f}<br>"
                "Avg Protection: %{customdata[1]:.1f}<br>"
                "<b>Gap: %{y:.1f}</b><extra></extra>"
            ),
            customdata=list(zip(threat_levels, protection_levels))
        )
    ])
    
    fig.update_layout(
        title=dict(
            text="<b>Protection Gap Analysis</b><br><sup>Threat Maturity − Average Protection Score</sup>",
            font=dict(size=16, color=text_color, family="Inter, sans-serif"),
            x=0.5,
            xanchor="center"
        ),
        xaxis=dict(
            tickangle=0,
            tickfont=dict(size=11, color=text_color),
            title=""
        ),
        yaxis=dict(
            title=dict(
                text="Gap Size (Levels)",
                font=dict(size=12, color=text_color)
            ),
            tickfont=dict(color=text_color),
            range=[0, 4],
            gridcolor=text_color if not dark_mode else "#333333",
            gridwidth=0.5
        ),
        paper_bgcolor=bg_color,
        plot_bgcolor=bg_color,
        height=320,
        margin=dict(l=60, r=20, t=80, b=60),
        font=dict(family="Inter, sans-serif"),
        bargap=0.3
    )
    
    return fig


def create_radar_chart(category, year="2025", dark_mode=True):
    """Create a radar chart for a specific threat category."""
    data = get_maturity_data(year)
    
    if category not in data:
        return go.Figure()
    
    values = data[category]
    
    bg_color = "#1a1a2e" if dark_mode else "#ffffff"
    text_color = "#ffffff" if dark_mode else "#000000"
    
    # Close the polygon by repeating the first value
    values_closed = values + [values[0]]
    dimensions_closed = DIMENSIONS + [DIMENSIONS[0]]
    
    fig = go.Figure()
    
    # Add filled area
    fig.add_trace(go.Scatterpolar(
        r=values_closed,
        theta=dimensions_closed,
        fill='toself',
        fillcolor='rgba(26, 152, 80, 0.25)',
        line=dict(color='#1a9850', width=2),
        marker=dict(size=8, color='#1a9850'),
        name=category,
        hovertemplate="<b>%{theta}</b><br>Level: %{r:.1f}<extra></extra>"
    ))
    
    # Add reference circle at level 2 (developing)
    fig.add_trace(go.Scatterpolar(
        r=[2, 2, 2, 2, 2],
        theta=dimensions_closed,
        mode='lines',
        line=dict(color='rgba(255,255,255,0.3)', dash='dot', width=1),
        showlegend=False,
        hoverinfo='skip'
    ))
    
    fig.update_layout(
        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[0, 4],
                tickvals=[0, 1, 2, 3, 4],
                ticktext=['0', '1', '2', '3', '4'],
                tickfont=dict(color=text_color, size=10),
                gridcolor='rgba(255,255,255,0.2)' if dark_mode else 'rgba(0,0,0,0.1)'
            ),
            angularaxis=dict(
                tickfont=dict(color=text_color, size=10),
                gridcolor='rgba(255,255,255,0.2)' if dark_mode else 'rgba(0,0,0,0.1)'
            ),
            bgcolor=bg_color
        ),
        paper_bgcolor=bg_color,
        title=dict(
            text=f"<b>{category}</b>",
            font=dict(color=text_color, size=14, family="Inter, sans-serif"),
            x=0.5,
            xanchor="center"
        ),
        height=280,
        margin=dict(l=60, r=60, t=60, b=40),
        font=dict(family="Inter, sans-serif"),
        showlegend=False
    )
    
    return fig


def create_dimension_card(dimension, data):
    """Create a card for a dimension in the modal."""
    if not data:
        return html.Div()
    
    level = data.get("level", 0)
    
    # Determine color based on level
    if level < 1.0:
        color = "danger"
        bg_class = "bg-danger bg-opacity-10"
    elif level < 2.0:
        color = "warning"
        bg_class = "bg-warning bg-opacity-10"
    elif level < 3.0:
        color = "info"
        bg_class = "bg-info bg-opacity-10"
    else:
        color = "success"
        bg_class = "bg-success bg-opacity-10"
    
    return dbc.Card([
        dbc.CardHeader([
            html.Strong(dimension),
            dbc.Badge(f"Level {level:.1f}", color=color, className="float-end")
        ], className="d-flex justify-content-between align-items-center"),
        dbc.CardBody([
            html.P(data.get("description", ""), className="mb-2 fw-light"),
            html.Ul([
                html.Li(e, className="small mb-1") for e in data.get("evidence", [])
            ], className="mb-2 ps-3"),
            html.Small([
                html.I(className="fas fa-book me-1"),
                ", ".join(data.get("references", []))
            ], className="text-muted")
        ])
    ], className=f"h-100 {bg_class}")


# ============================================================================
# LAYOUT COMPONENTS
# ============================================================================

def create_header():
    """Create the application header."""
    return dbc.Row([
        dbc.Col([
            html.Div([
                html.H1([
                    html.I(className="fas fa-shield-alt me-3"),
                    "Generative AI Security Maturity Explorer"
                ], className="mb-2 display-5"),
                html.H5(
                    "A Sociotechnical Three-Dimensional Maturity Assessment",
                    className="text-muted mb-1 fw-light"
                ),
                html.P([
                    "Based on ",
                    html.Em("'Security Risks in Generative AI'"),
                    " by Ruby Jane Cabagnot (2025)"
                ], className="small text-muted mb-0")
            ], className="py-4")
        ])
    ])


def create_sidebar():
    """Create the control sidebar."""
    return dbc.Card([
        dbc.CardHeader([
            html.I(className="fas fa-sliders-h me-2"),
            html.Span("Controls", className="fw-bold")
        ]),
        dbc.CardBody([
            # Year selector
            html.Label([
                html.I(className="fas fa-calendar me-2"),
                "Assessment Year"
            ], className="fw-bold mb-2"),
            dcc.Dropdown(
                id="year-selector",
                options=[
                    {"label": "📊 2025 Baseline", "value": "2025"},
                    {"label": "📈 2026 Projection", "value": "2026"},
                    {"label": "🔮 2027 Projection", "value": "2027"},
                ],
                value="2025",
                className="mb-4",
                clearable=False
            ),
            
            html.Hr(className="my-3"),
            
            # Governance simulation slider
            html.Label([
                html.I(className="fas fa-flask me-2"),
                "What-If Simulation"
            ], className="fw-bold mb-2"),
            html.P(
                "Simulate governance improvement:",
                className="small text-muted mb-2"
            ),
            dcc.Slider(
                id="governance-slider",
                min=0,
                max=4,
                step=1,
                value=0,
                marks={
                    0: {'label': '0', 'style': {'color': '#d73027'}},
                    1: {'label': '1', 'style': {'color': '#fc8d59'}},
                    2: {'label': '2', 'style': {'color': '#fee08b'}},
                    3: {'label': '3', 'style': {'color': '#d9ef8b'}},
                    4: {'label': '4', 'style': {'color': '#1a9850'}}
                },
                tooltip={"placement": "bottom", "always_visible": False}
            ),
            html.P(
                "↑ Watch protection cells turn greener as governance improves",
                className="small text-muted mt-2 mb-4 fst-italic"
            ),
            
            html.Hr(className="my-3"),
            
            # Dark mode toggle
            dbc.Switch(
                id="dark-mode-toggle",
                label="Dark Mode",
                value=True,
                className="mb-4"
            ),
            
            html.Hr(className="my-3"),
            
            # Statistics
            html.Label([
                html.I(className="fas fa-chart-pie me-2"),
                "Quick Statistics"
            ], className="fw-bold mb-3"),
            html.Div(id="quick-stats"),
            
            html.Hr(className="my-3"),
            
            # Instructions
            html.Label([
                html.I(className="fas fa-info-circle me-2"),
                "How to Use"
            ], className="fw-bold mb-2"),
            html.Ul([
                html.Li("Hover over cells for evidence", className="small"),
                html.Li("Click threats for detailed analysis", className="small"),
                html.Li("Use slider to simulate improvements", className="small"),
            ], className="small text-muted ps-3")
        ])
    ], className="h-100")


def create_detail_modal():
    """Create the modal for detailed threat information."""
    return dbc.Modal([
        dbc.ModalHeader(
            dbc.ModalTitle(id="modal-title"),
            close_button=True,
            className="border-bottom border-secondary"
        ),
        dbc.ModalBody(id="modal-body", className="p-4"),
        dbc.ModalFooter([
            html.Small(
                "Data from Cabagnot (2025) systematic literature review",
                className="text-muted me-auto"
            ),
            dbc.Button(
                "Close",
                id="close-modal",
                className="ms-auto",
                color="secondary",
                n_clicks=0
            )
        ], className="border-top border-secondary")
    ], id="detail-modal", size="xl", scrollable=True, centered=True)


def create_main_content():
    """Create the main content area."""
    return html.Div([
        # Main heatmap card
        dbc.Card([
            dbc.CardHeader([
                html.I(className="fas fa-th me-2"),
                html.Span("Maturity Assessment Heatmap", className="fw-bold"),
                html.Small(
                    " — Click on any threat category for detailed analysis",
                    className="text-muted ms-2"
                )
            ]),
            dbc.CardBody([
                dcc.Loading(
                    dcc.Graph(
                        id="main-heatmap",
                        config={
                            "displayModeBar": True,
                            "displaylogo": False,
                            "toImageButtonOptions": {
                                "format": "png",
                                "filename": "genai_security_maturity_heatmap",
                                "height": 600,
                                "width": 1000,
                                "scale": 2
                            },
                            "modeBarButtonsToRemove": ["lasso2d", "select2d"]
                        }
                    ),
                    type="default",
                    color="#1a9850"
                )
            ])
        ], className="mb-4"),
        
        # Analysis row
        dbc.Row([
            # Gap analysis chart
            dbc.Col([
                dbc.Card([
                    dbc.CardHeader([
                        html.I(className="fas fa-chart-bar me-2"),
                        html.Span("Protection Gap Analysis", className="fw-bold")
                    ]),
                    dbc.CardBody([
                        dcc.Loading(
                            dcc.Graph(
                                id="gap-chart",
                                config={"displayModeBar": False}
                            ),
                            type="default",
                            color="#1a9850"
                        )
                    ])
                ], className="h-100")
            ], lg=7, className="mb-4 mb-lg-0"),
            
            # Radar chart
            dbc.Col([
                dbc.Card([
                    dbc.CardHeader([
                        html.I(className="fas fa-radar me-2"),
                        html.Span("Threat Profile", className="fw-bold")
                    ]),
                    dbc.CardBody([
                        dcc.Dropdown(
                            id="radar-threat-selector",
                            options=[{"label": t, "value": t} for t in THREAT_CATEGORIES],
                            value="Prompt Injection",
                            className="mb-3",
                            clearable=False
                        ),
                        dcc.Loading(
                            dcc.Graph(
                                id="radar-chart",
                                config={"displayModeBar": False}
                            ),
                            type="default",
                            color="#1a9850"
                        )
                    ])
                ], className="h-100")
            ], lg=5)
        ], className="mb-4"),
        
        # Key findings
        dbc.Card([
            dbc.CardHeader([
                html.I(className="fas fa-lightbulb me-2"),
                html.Span("Key Findings from Cabagnot (2025)", className="fw-bold")
            ]),
            dbc.CardBody([
                dbc.Row([
                    dbc.Col([
                        html.Div([
                            html.H4("3.5", className="text-danger mb-1 display-6 fw-bold"),
                            html.P("Maximum Gap", className="fw-bold mb-1"),
                            html.Small(
                                "Political Integrity: threat vs. protection",
                                className="text-muted"
                            )
                        ], className="text-center p-3")
                    ], md=3, className="border-end"),
                    dbc.Col([
                        html.Div([
                            html.H4("0.5", className="text-warning mb-1 display-6 fw-bold"),
                            html.P("Avg Stakeholder Protection", className="fw-bold mb-1"),
                            html.Small(
                                "For GenAI-specific threats (excl. Privacy)",
                                className="text-muted"
                            )
                        ], className="text-center p-3")
                    ], md=3, className="border-end"),
                    dbc.Col([
                        html.Div([
                            html.H4("1.5", className="text-success mb-1 display-6 fw-bold"),
                            html.P("Privacy Advantage", className="fw-bold mb-1"),
                            html.Small(
                                "Pre-existing law narrows protection gap",
                                className="text-muted"
                            )
                        ], className="text-center p-3")
                    ], md=3, className="border-end"),
                    dbc.Col([
                        html.Div([
                            html.H4("46", className="text-info mb-1 display-6 fw-bold"),
                            html.P("Sources Reviewed", className="fw-bold mb-1"),
                            html.Small(
                                "Academic, regulatory, incident data",
                                className="text-muted"
                            )
                        ], className="text-center p-3")
                    ], md=3)
                ])
            ])
        ])
    ])


def create_footer():
    """Create the application footer."""
    return html.Footer([
        html.Hr(className="mt-4"),
        dbc.Row([
            dbc.Col([
                html.P([
                    "© 2025 Ruby Jane Cabagnot | ",
                    html.A(
                        "GitHub Repository",
                        href="https://github.com/RubyJane88/genai-security-maturity-explorer",
                        className="text-decoration-none",
                        target="_blank"
                    ),
                    " | Based on systematic review of 46 sources"
                ], className="text-center text-muted small mb-2"),
                html.P([
                    html.Strong("Maturity Scale: "),
                    "0=Non-existent, 1=Initial, 2=Developing, 3=Defined, 4=Mature"
                ], className="text-center text-muted small mb-0")
            ])
        ], className="pb-4")
    ])


# ============================================================================
# APP LAYOUT
# ============================================================================

app.layout = dbc.Container([
    # Header
    create_header(),
    
    html.Hr(className="my-0"),
    
    # Main content area
    dbc.Row([
        # Sidebar
        dbc.Col([
            create_sidebar()
        ], lg=3, md=4, className="py-4"),
        
        # Main area
        dbc.Col([
            create_main_content()
        ], lg=9, md=8, className="py-4")
    ]),
    
    # Modal for details
    create_detail_modal(),
    
    # Footer
    create_footer()
    
], fluid=True, className="px-4")


# ============================================================================
# CALLBACKS
# ============================================================================

@app.callback(
    [Output("main-heatmap", "figure"),
     Output("gap-chart", "figure"),
     Output("quick-stats", "children")],
    [Input("year-selector", "value"),
     Input("governance-slider", "value"),
     Input("dark-mode-toggle", "value")]
)
def update_charts(year, governance_adj, dark_mode):
    """Update all charts based on controls."""
    # Main heatmap
    heatmap = create_heatmap(year, governance_adj, dark_mode)
    
    # Gap chart
    gap_chart = create_gap_analysis_chart(year, dark_mode)
    
    # Calculate statistics
    data = get_maturity_data(year)
    
    avg_threat = np.mean([data[cat][0] for cat in THREAT_CATEGORIES])
    avg_tech = np.mean([data[cat][1] for cat in THREAT_CATEGORIES])
    avg_gov = np.mean([data[cat][2] for cat in THREAT_CATEGORIES])
    avg_stake = np.mean([data[cat][3] for cat in THREAT_CATEGORIES])
    overall_gap = avg_threat - avg_stake
    
    # Build stats display
    stats = html.Div([
        html.Div([
            html.Span("Threat Maturity: ", className="text-muted"),
            html.Span(f"{avg_threat:.1f}", className="fw-bold text-danger")
        ], className="mb-1"),
        html.Div([
            html.Span("Technical Controls: ", className="text-muted"),
            html.Span(f"{avg_tech:.1f}", className="fw-bold text-warning")
        ], className="mb-1"),
        html.Div([
            html.Span("Governance: ", className="text-muted"),
            html.Span(f"{avg_gov:.1f}", className="fw-bold text-info")
        ], className="mb-1"),
        html.Div([
            html.Span("Stakeholder Protection: ", className="text-muted"),
            html.Span(f"{avg_stake:.1f}", className="fw-bold text-success")
        ], className="mb-2"),
        html.Hr(className="my-2"),
        html.Div([
            html.Span("Overall Gap: ", className="text-muted"),
            html.Span(f"{overall_gap:.1f}", className="fw-bold text-danger fs-5")
        ])
    ], className="small")
    
    return heatmap, gap_chart, stats


@app.callback(
    Output("radar-chart", "figure"),
    [Input("radar-threat-selector", "value"),
     Input("year-selector", "value"),
     Input("dark-mode-toggle", "value")]
)
def update_radar(category, year, dark_mode):
    """Update radar chart for selected threat."""
    return create_radar_chart(category, year, dark_mode)


@app.callback(
    [Output("detail-modal", "is_open"),
     Output("modal-title", "children"),
     Output("modal-body", "children")],
    [Input("main-heatmap", "clickData"),
     Input("close-modal", "n_clicks")],
    [State("detail-modal", "is_open")],
    prevent_initial_call=True
)
def toggle_modal(click_data, close_clicks, is_open):
    """Handle modal opening/closing with detailed threat information."""
    triggered = ctx.triggered_id
    
    if triggered == "close-modal":
        return False, "", ""
    
    if click_data is None:
        return False, "", ""
    
    # Get clicked category
    point = click_data["points"][0]
    category = point["y"]
    
    if category not in CELL_DETAILS:
        return False, "", ""
    
    details = CELL_DETAILS[category]
    
    # Build modal title
    modal_title = html.Div([
        html.I(className="fas fa-shield-virus me-2"),
        html.Span(category)
    ])
    
    # Build modal content
    content = [
        # Description
        dbc.Alert([
            html.I(className="fas fa-info-circle me-2"),
            details["description"]
        ], color="info", className="mb-4"),
        
        # Thesis quote
        dbc.Card([
            dbc.CardBody([
                html.I(className="fas fa-quote-left me-2 text-muted fa-lg"),
                html.Em(details["thesis_quote"], className="fs-6"),
                html.Div([
                    html.Small("— Cabagnot (2025)", className="text-muted float-end mt-2")
                ])
            ])
        ], className="mb-4 border-start border-4 border-primary bg-dark"),
        
        # Dimension breakdown
        html.H5([
            html.I(className="fas fa-layer-group me-2"),
            "Dimension Analysis"
        ], className="mb-3"),
        dbc.Row([
            dbc.Col([
                create_dimension_card(dim, details["dimensions"].get(dim, {}))
            ], lg=6, className="mb-3")
            for dim in DIMENSIONS
        ]),
        
        # Real-world incidents
        html.H5([
            html.I(className="fas fa-exclamation-triangle me-2 text-warning"),
            "Real-World Incidents"
        ], className="mb-3 mt-4"),
        dbc.ListGroup([
            dbc.ListGroupItem([
                html.I(className="fas fa-bolt me-2 text-warning"),
                incident
            ], className="bg-dark border-secondary")
            for incident in details["incidents"]
        ])
    ]
    
    return True, modal_title, content


# ============================================================================
# RUN SERVER
# ============================================================================

if __name__ == "__main__":
    app.run_server(debug=True, host="0.0.0.0", port=8050)
