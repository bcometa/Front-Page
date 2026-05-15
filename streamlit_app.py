"""
$300 Data Recovery — Internal Tools Hub

Single landing page that links to all internal Streamlit tools and the
Tailscale-only PC-3000 manual Q&A server.
"""

import streamlit as st

st.set_page_config(
    page_title="$300 Data Recovery — Tools",
    page_icon="🛠️",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ---------------------------------------------------------------------------
# Custom CSS — 300DDR brand red on dark background
# ---------------------------------------------------------------------------
st.markdown(
    """
    <style>
        /* Hide default Streamlit chrome */
        #MainMenu { visibility: hidden; }
        footer { visibility: hidden; }
        header { visibility: hidden; }

        .stApp {
            background: #0d0d0d;
            color: #f5f5f5;
        }

        .block-container {
            padding-top: 2rem;
            padding-bottom: 4rem;
            max-width: 1180px;
        }

        /* Hero ---------------------------------------------------------- */
        .hero {
            text-align: center;
            padding: 2rem 1rem 2.25rem 1rem;
            margin-bottom: 2.5rem;
            border-bottom: 2px solid #EE2400;
        }
        .hero-title {
            font-size: 3rem;
            font-weight: 800;
            letter-spacing: -1px;
            margin: 0;
            line-height: 1.1;
        }
        .hero-title .accent {
            background: linear-gradient(135deg, #EE2400 0%, #B81A00 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
        }
        .hero-sub {
            color: #9a9a9a;
            font-size: 1.05rem;
            margin-top: 0.6rem;
            text-transform: uppercase;
            letter-spacing: 3px;
        }

        /* Cards --------------------------------------------------------- */
        .tool-card {
            position: relative;
            background: #161616;
            border: 1px solid #262626;
            border-radius: 14px;
            padding: 1.75rem;
            min-height: 260px;
            display: flex;
            flex-direction: column;
            transition: border-color 0.2s ease, transform 0.2s ease, box-shadow 0.2s ease;
            margin-bottom: 1.25rem;
        }
        .tool-card:hover {
            border-color: #EE2400;
            transform: translateY(-2px);
            box-shadow: 0 10px 28px rgba(238, 36, 0, 0.18);
        }
        .tool-icon {
            font-size: 2.3rem;
            margin-bottom: 0.6rem;
            line-height: 1;
        }
        .tool-title {
            color: #ffffff;
            font-size: 1.35rem;
            font-weight: 700;
            margin: 0 0 0.4rem 0;
        }
        .tool-desc {
            color: #b3b3b3;
            font-size: 0.95rem;
            line-height: 1.55;
            flex-grow: 1;
            margin-bottom: 1.2rem;
        }
        .tool-badge {
            position: absolute;
            top: 1rem;
            right: 1rem;
            background: rgba(238, 36, 0, 0.14);
            color: #ff7a6a;
            border: 1px solid rgba(238, 36, 0, 0.35);
            padding: 0.22rem 0.55rem;
            border-radius: 999px;
            font-size: 0.7rem;
            font-weight: 700;
            letter-spacing: 0.6px;
            text-transform: uppercase;
        }
        .tool-btn {
            display: inline-block;
            background: linear-gradient(135deg, #EE2400 0%, #B81A00 100%);
            color: #ffffff !important;
            padding: 0.65rem 1.3rem;
            border-radius: 8px;
            text-decoration: none !important;
            font-weight: 600;
            font-size: 0.95rem;
            text-align: center;
            border: none;
            align-self: flex-start;
            transition: filter 0.15s ease;
        }
        .tool-btn:hover {
            filter: brightness(1.1);
        }

        /* Section headers ---------------------------------------------- */
        .section-header {
            display: flex;
            align-items: center;
            gap: 0.75rem;
            font-size: 0.95rem;
            font-weight: 700;
            color: #f5f5f5;
            text-transform: uppercase;
            letter-spacing: 2.5px;
            margin: 2.25rem 0 1.1rem 0;
            padding-bottom: 0.55rem;
            border-bottom: 1px solid #262626;
        }
        .section-header:first-of-type {
            margin-top: 0.5rem;
        }
        .section-header .section-accent {
            display: inline-block;
            width: 4px;
            height: 18px;
            background: linear-gradient(135deg, #EE2400 0%, #B81A00 100%);
            border-radius: 2px;
        }
        .section-header .section-count {
            margin-left: auto;
            font-size: 0.75rem;
            color: #888;
            letter-spacing: 1.5px;
        }

        /* Responsive card grid ----------------------------------------- */
        .tool-grid {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
            gap: 1.25rem;
        }

        /* Footer -------------------------------------------------------- */
        .footer-note {
            text-align: center;
            color: #707070;
            font-size: 0.85rem;
            margin-top: 3rem;
            padding-top: 1.5rem;
            border-top: 1px solid #232323;
        }
        .footer-note a {
            color: #b3b3b3;
            text-decoration: none;
        }
        .footer-note a:hover {
            color: #EE2400;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# ---------------------------------------------------------------------------
# Hero
# ---------------------------------------------------------------------------
st.markdown(
    """
    <div class="hero">
        <h1 class="hero-title"><span class="accent">$300</span> Data Recovery</h1>
        <div class="hero-sub">Internal Tools</div>
    </div>
    """,
    unsafe_allow_html=True,
)

# ---------------------------------------------------------------------------
# Tool definitions — grouped by manufacturer
# ---------------------------------------------------------------------------
SECTIONS = [
    {
        "name": "General",
        "tools": [
            {
                "icon": "🔀",
                "title": "Module Repair Tool",
                "desc": (
                    "Compares two binary dumps, merges non-DEAD sectors, and "
                    "zero-fills double-DEAD sectors (512-byte). DEAD = a full "
                    "sector of DE AD DE AD ..."
                ),
                "url": "https://module-merger-rhwf7v6c4rvpyck25ftgyh.streamlit.app/",
                "badge": None,
            },
            {
                "icon": "📋",
                "title": "ACE Report Converter",
                "desc": (
                    "Converts ACE Lab reports into clean, customer-ready "
                    "formatting with Slack upload built in."
                ),
                "url": "https://300ddr-acerep-proceappr-seqw4mzydzw7vh2uwnyt4t.streamlit.app/",
                "badge": None,
            },
            {
                "icon": "📖",
                "title": "PC-3000 Manual Q&A",
                "desc": (
                    "Ask questions about the PC-3000 manuals directly. Runs "
                    "locally on the shop network — requires Tailscale to access."
                ),
                "url": "http://plex:8400/",
                "badge": "Tailscale required",
            },
        ],
    },
    {
        "name": "Seagate",
        "tools": [
            {
                "icon": "🧬",
                "title": "Translator Repair",
                "desc": (
                    "Repairs corrupt translator and NRGL modules on Seagate F3 "
                    "drives — 4 documented repair modes plus checksum recompute."
                ),
                "url": "https://repair-seagate-translator-b8w4vxafqgkofkvzat8ps6.streamlit.app/",
                "badge": None,
            },
            {
                "icon": "🧠",
                "title": "ROM Repair Tool",
                "desc": "Repairs and validates corrupt Seagate ROM dumps.",
                "url": "https://seagate-rom-repair-tool-qqrqzebbm9qivsbjzrwttp.streamlit.app/",
                "badge": None,
            },
            {
                "icon": "🧩",
                "title": "1D1 / 1D2 Module Repair",
                "desc": "Repairs corrupt 1D1 and 1D2 firmware modules on Seagate drives.",
                "url": "https://seagate-1d1-1d2-module-repair-jrseycqyzx2hfborcvdgyl.streamlit.app/",
                "badge": None,
            },
        ],
    },
    {
        "name": "Western Digital",
        "tools": [
            {
                "icon": "🗺️",
                "title": "Head Map Editor",
                "desc": (
                    "View and edit head maps for Western Digital drives — "
                    "slider, custom offset, hex viewer."
                ),
                "url": "https://wd-head-map-editor-fo3bdxohj8kya9merknaq7.streamlit.app/",
                "badge": None,
            },
        ],
    },
]

# ---------------------------------------------------------------------------
# Render — manufacturer sections + responsive card grid
# ---------------------------------------------------------------------------
def render_card(tool: dict) -> str:
    """Build a tool card as a single flat HTML string (no leading whitespace).

    Streamlit's markdown parser bails out of HTML-block mode on any
    whitespace-only line, so the entire card must be emitted without
    indentation or blank gaps.
    """
    badge = (
        f'<div class="tool-badge">{tool["badge"]}</div>' if tool["badge"] else ""
    )
    return (
        '<div class="tool-card">'
        f'{badge}'
        f'<div class="tool-icon">{tool["icon"]}</div>'
        f'<div class="tool-title">{tool["title"]}</div>'
        f'<div class="tool-desc">{tool["desc"]}</div>'
        f'<a class="tool-btn" href="{tool["url"]}" target="_blank" rel="noopener">Open Tool →</a>'
        '</div>'
    )


def render_section(section: dict) -> str:
    count = len(section["tools"])
    label = "tool" if count == 1 else "tools"
    cards = "".join(render_card(t) for t in section["tools"])
    return (
        '<div class="section-header">'
        '<span class="section-accent"></span>'
        f'<span>{section["name"]}</span>'
        f'<span class="section-count">{count} {label}</span>'
        '</div>'
        f'<div class="tool-grid">{cards}</div>'
    )


for section in SECTIONS:
    st.markdown(render_section(section), unsafe_allow_html=True)

# ---------------------------------------------------------------------------
# Footer
# ---------------------------------------------------------------------------
st.markdown(
    """
    <div class="footer-note">
        <a href="https://www.300dollardatarecovery.com" target="_blank" rel="noopener">
            300dollardatarecovery.com
        </a>
    </div>
    """,
    unsafe_allow_html=True,
)
