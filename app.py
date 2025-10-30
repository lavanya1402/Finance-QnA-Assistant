# app.py
# Finance Q&A Assistant (Education Only) — 2025
# Single-model build: Groq 'gemma2-9b-it'
# Made with ❤️ by Lavanya Srivastava

import os
from dotenv import load_dotenv
import streamlit as st
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage

load_dotenv()  # expects GROQ_API_KEY in .env

# ---- LLM: Groq (LangChain) ----
try:
    from langchain_groq import ChatGroq  # pip install -U langchain-groq
except Exception:
    st.error("Missing dependency: langchain-groq. Install with: pip install -U langchain-groq")
    st.stop()

# =========================
# APP CONFIG
# =========================
st.set_page_config(page_title="Finance Q&A Assistant (Education Only)", page_icon="💹")
st.title("💹 Finance Q&A Assistant — Education, not Advice (2025)")
st.caption(
    "For learning purposes only — not financial, investment, legal, tax, or accounting advice. "
    "Always do your own research and consult a licensed professional."
)

# ----------------- Single Model -----------------
MODEL_NAME = "llama-3.3-70b-versatile"   # ✅ stable Groq chat model
TEMPERATURE_DEFAULT = 0.2

with st.sidebar:
    st.header("Settings")
    temperature = st.slider("Creativity (temperature)", 0.0, 1.0, TEMPERATURE_DEFAULT, 0.1)
    st.info("Using Groq model: gemma2-9b-it (stable as of 2025).", icon="💬")

    mode = st.radio(
        "Assistant Mode",
        [
            "Markets & Macro (Education)",
            "Investing 101 (Asset Classes & Diversification)",
            "Risk & Portfolio Concepts",
            "Personal Finance (Budget, Debt, Goals)",
            "Fraud & Scam Watch (2025)",
            "Crypto Basics (Education)",
        ],
        index=0,
    )

    st.write("---")
    st.subheader("📓 Market Notes (optional, private)")
    st.caption("Paste weekly macro notes (CPI, rate decisions, earnings, etc.) or upload .txt/.md")

    if "market_notes" not in st.session_state:
        st.session_state.market_notes = ""

    uploaded = st.file_uploader("Upload notes (.txt/.md)", type=["txt", "md"])
    if uploaded:
        st.session_state.market_notes = uploaded.read().decode("utf-8")

    notes_text = st.text_area(
        "Paste / edit notes here",
        value=st.session_state.market_notes,
        height=180,
        placeholder="- CPI Thu (consensus 3.2% YoY)\n- Fed Chair Fri 10:00\n- BigTech earnings Wed\n- 2s10s curve, IG spreads, VIX ~14",
    )
    st.session_state.market_notes = notes_text

    col_a, col_b = st.columns(2)
    with col_a:
        use_notes = st.checkbox("Use notes in answers", value=True)
    with col_b:
        if st.button("Clear notes"):
            st.session_state.market_notes = ""
            st.rerun()

    st.write("---")
    st.subheader("Disclaimer")
    st.write(
        "This assistant provides **general educational information** only. "
        "It cannot make recommendations or predictions. Seek a qualified advisor."
    )

# ----------------- Prompt Helpers -----------------
def _truncate(text: str, limit: int = 2000) -> str:
    if not text:
        return ""
    return text if len(text) <= limit else text[:limit] + "\n...[truncated]"

def build_system_prompt(selected_mode: str, notes: str, include_notes: bool) -> str:
    base = """You are a careful, neutral Finance Q&A assistant for the public (2025).
- You do NOT provide investment, legal, tax, or accounting advice.
- You do NOT recommend specific securities, allocations, or trades.
- Explain concepts with short paragraphs and bullet points.
- Avoid guarantees or predictions.
- If asked for personalized advice, decline and suggest consulting a licensed professional.
- When relevant, add a 'What to double-check' checklist (fees, risks, horizon, taxes, liquidity).
- Define jargon simply (beta, drawdown, Sharpe, duration, yield curve)."""

    mode_details = {
        "Markets & Macro (Education)": "Explain macro indicators (inflation, rates, growth, jobs), yield curves, and high-level effects on asset classes.",
        "Investing 101 (Asset Classes & Diversification)": "Explain stocks, bonds, ETFs, diversification, compounding, rebalancing, and fee awareness.",
        "Risk & Portfolio Concepts": "Explain risk tolerance vs. capacity, volatility, drawdowns, correlation, and dollar-cost averaging.",
        "Personal Finance (Budget, Debt, Goals)": "Discuss budgeting, emergency funds, debt payoff, goal setting, and insurance basics (non-jurisdictional).",
        "Fraud & Scam Watch (2025)": "Explain 2025 scams: deepfakes, fake 'guaranteed returns', pump groups, phishing, fake AI trading bots. Include safety tips.",
        "Crypto Basics (Education)": "Explain blockchains, wallets, private keys, stablecoins, custody, and volatility. No token picks or price calls.",
    }

    notes_block = (
        "\n\nUser's Market Notes (unverified, for context only):\n" + _truncate(notes)
        if include_notes and notes.strip()
        else ""
    )
    return base + "\n\nMode:\n" + mode_details[selected_mode] + notes_block

# ----------------- LLM Init -----------------
if not os.getenv("GROQ_API_KEY"):
    st.warning("⚠️ Please set your GROQ_API_KEY in a .env file.")
chat = ChatGroq(model=MODEL_NAME, temperature=temperature)

# ----------------- Session State -----------------
if "messages" not in st.session_state:
    st.session_state.messages = [
        SystemMessage(
            content=build_system_prompt("Markets & Macro (Education)", st.session_state.market_notes, True)
        )
    ]
if "active_mode" not in st.session_state:
    st.session_state.active_mode = "Markets & Macro (Education)"

current_system = build_system_prompt(mode, st.session_state.market_notes, use_notes)
if (
    mode != st.session_state.active_mode
    or not isinstance(st.session_state.messages[-1], SystemMessage)
    or st.session_state.messages[-1].content != current_system
):
    st.session_state.active_mode = mode
    st.session_state.messages.append(SystemMessage(content=current_system))

# ----------------- Sample Prompts -----------------
st.write("#### Try a sample prompt")
c1, c2, c3 = st.columns(3)
with c1:
    if st.button("📊 How do rates affect bonds?"):
        st.session_state.prefill = "Explain how interest rate changes typically affect bond prices and duration risk (education only)."
with c2:
    if st.button("🧺 What is diversification?"):
        st.session_state.prefill = "What does diversification mean in investing, and why might investors consider it over concentrating in one stock?"
with c3:
    if st.button("🛡️ Spotting 2025 scams"):
        st.session_state.prefill = "List common 2025 finance scams and a checklist to avoid them (no links)."

# ----------------- History -----------------
for m in st.session_state.messages:
    if isinstance(m, HumanMessage):
        with st.chat_message("user"):
            st.write(m.content)
    elif isinstance(m, AIMessage):
        with st.chat_message("assistant"):
            st.write(m.content)

user_input = st.chat_input("Ask a finance question (education only, no recommendations).", key="chat_input")
if "prefill" in st.session_state and st.session_state.prefill:
    user_input = st.session_state.prefill
    st.session_state.prefill = ""

# ----------------- Safety Banner -----------------
RISK_FLAGS = [
    "guaranteed returns", "insider tip", "all-in", "margin call",
    "loan at high interest", "get rich quick", "secret strategy",
    "send crypto now", "seed phrase", "private key", "double your money",
]
def maybe_show_risk_banner(text: str):
    if not text:
        return
    if any(flag in text.lower() for flag in RISK_FLAGS):
        st.warning("⚠️ Message includes terms seen in scams. Verify sources, never share private keys, and consult professionals.")

# ----------------- Handle Chat Turn -----------------
if user_input:
    maybe_show_risk_banner(user_input)
    st.session_state.messages.append(HumanMessage(content=user_input))
    st.session_state.messages.append(SystemMessage(content=current_system))

    with st.chat_message("assistant"):
        answer = chat.invoke(st.session_state.messages)  # LangChain ≥0.3 style
        st.write(answer.content)

    st.session_state.messages.append(AIMessage(content=answer.content))

# ----------------- Footer -----------------
st.write("---")
st.caption(
    "Educational demo (2025). No portfolio data collected. "
    "For deployment, add compliance, region-specific disclosures, and proper logging."
)
st.markdown(
    "<p style='text-align:center; color:gray; font-size:0.9em;'>"
    "💡 Made with ❤️ by <b>Lavanya Srivastava</b> — Powered by Groq + Streamlit (2025)"
    "</p>",
    unsafe_allow_html=True,
)
