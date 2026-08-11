
# ============================================================
# PROJECT CONTACT
# AI FIRST CONTACT SIMULATOR
# Futuristic Streamlit Frontend
# ============================================================

# pyrefly: ignore [missing-import]
import streamlit as st
import pandas as pd
# pyrefly: ignore [missing-import]
import plotly.graph_objects as go
# pyrefly: ignore [missing-import]
import plotly.express as px

# pyrefly: ignore [missing-import]
from model import (
    generate_alien_civilization,
    generate_alien_signal,
    analyze_signal,
    analyze_intent,
    calculate_trust,
    assess_threat,
    generate_alien_response,
    human_response_advisor,
    simulate_scenario,
    generate_mission_report,
    generate_timestamp
)


# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="PROJECT CONTACT",
    page_icon="👽",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ============================================================
# CSS
# ============================================================

st.markdown(
    """
<style>

@import url(
'https://fonts.googleapis.com/css2?family=Orbitron:wght@400;500;600;700;800&family=Inter:wght@400;500;600;700&display=swap'
);

html, body, [class*="css"] {
    font-family: Inter, sans-serif;
}

.stApp {

    background:
        radial-gradient(
            circle at 15% 15%,
            rgba(34, 211, 238, 0.13),
            transparent 25%
        ),
        radial-gradient(
            circle at 85% 20%,
            rgba(124, 58, 237, 0.18),
            transparent 28%
        ),
        radial-gradient(
            circle at 50% 90%,
            rgba(16, 185, 129, 0.08),
            transparent 25%
        ),
        #020617;

    color: #e2e8f0;
}

h1, h2, h3 {
    font-family: Orbitron, sans-serif;
}

.main-title {

    font-family: Orbitron, sans-serif;

    text-align: center;

    font-size: 48px;

    font-weight: 800;

    letter-spacing: 5px;

    background:
        linear-gradient(
            90deg,
            #22d3ee,
            #8b5cf6,
            #34d399,
            #22d3ee
        );

    -webkit-background-clip: text;

    -webkit-text-fill-color: transparent;

    margin-top: 10px;

}

.subtitle {

    text-align: center;

    color: #94a3b8;

    letter-spacing: 2px;

    margin-bottom: 30px;

}

.command-card {

    background:
        linear-gradient(
            145deg,
            rgba(15,23,42,.88),
            rgba(30,41,59,.55)
        );

    border:

        1px solid
        rgba(34,211,238,.18);

    border-radius: 20px;

    padding: 22px;

    box-shadow:
        0 15px 50px rgba(0,0,0,.35);

    margin-bottom: 20px;

}

.signal-card {

    background:
        rgba(8,47,73,.45);

    border:
        1px solid
        rgba(34,211,238,.22);

    border-radius: 18px;

    padding: 20px;

}

.alien-card {

    background:
        linear-gradient(
            145deg,
            rgba(76,29,149,.28),
            rgba(15,23,42,.75)
        );

    border:
        1px solid
        rgba(167,139,250,.25);

    border-radius: 20px;

    padding: 22px;

}

.metric-box {

    background:
        rgba(15,23,42,.72);

    border:
        1px solid
        rgba(148,163,184,.12);

    border-radius: 16px;

    padding: 18px;

    text-align: center;

}

.metric-number {

    font-family: Orbitron;

    font-size: 30px;

    color: #67e8f9;

}

.metric-label {

    color: #94a3b8;

    font-size: 12px;

    letter-spacing: 1px;

}

.chat-human {

    background:
        rgba(37,99,235,.20);

    border-left:
        4px solid #3b82f6;

    border-radius: 12px;

    padding: 14px;

    margin: 10px 0;

}

.chat-alien {

    background:
        rgba(124,58,237,.20);

    border-left:
        4px solid #a78bfa;

    border-radius: 12px;

    padding: 14px;

    margin: 10px 0;

}

.status-online {

    color: #34d399;

    font-weight: 700;

}

.stButton > button {

    width: 100%;

    border-radius: 12px;

    min-height: 44px;

    background:
        linear-gradient(
            135deg,
            rgba(8,145,178,.75),
            rgba(109,40,217,.75)
        );

    border:
        1px solid
        rgba(103,232,249,.25);

    color: white;

    font-weight: 700;

}

.stButton > button:hover {

    border-color: #67e8f9;

    box-shadow:
        0 0 20px rgba(34,211,238,.15);

}

.sidebar-title {

    font-family: Orbitron;

    color: #67e8f9;

    font-size: 18px;

}

.small {

    color: #64748b;

    font-size: 12px;

}

</style>
""",
    unsafe_allow_html=True
)


# ============================================================
# SESSION STATE
# ============================================================

defaults = {

    "alien": None,

    "signal": None,

    "signal_analysis": None,

    "intent": None,

    "trust": 50.0,

    "threat": None,

    "history": [],

    "mission_started": False,

    "scenario_result": None

}

for key, value in defaults.items():

    if key not in st.session_state:

        st.session_state[key] = value


# ============================================================
# HEADER
# ============================================================

st.markdown(
    '<div class="main-title">👽 PROJECT CONTACT</div>',
    unsafe_allow_html=True
)

st.markdown(
    """
<div class="subtitle">
AI FIRST CONTACT • EXTRATERRESTRIAL COMMUNICATION •
MULTI-AGENT SIMULATION
</div>
""",
    unsafe_allow_html=True
)


# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:

    st.markdown(
        '<div class="sidebar-title">🛰️ MISSION CONTROL</div>',
        unsafe_allow_html=True
    )

    st.write("")

    difficulty = st.selectbox(
        "🎮 Mission Difficulty",
        [
            "Diplomatic",
            "Standard",
            "Uncertain",
            "Hostile"
        ]
    )

    communication_mode = st.selectbox(
        "📡 Communication Mode",
        [
            "Human ↔ Alien",
            "Signal Analysis",
            "AI Diplomatic Advisor"
        ]
    )

    st.divider()

    start_button = st.button(
        "🚀 INITIATE FIRST CONTACT"
    )

    reset_button = st.button(
        "🔄 RESET MISSION"
    )

    if reset_button:

        for key, value in defaults.items():

            st.session_state[key] = value

        st.rerun()

    st.divider()

    st.markdown(
        """
### 🧠 SYSTEM MODULES

🟢 Signal Analyzer  
🟢 Intent Engine  
🟢 Translation AI  
🟢 Trust Engine  
🟢 Threat Analyzer  
🟢 Alien AI Agent  
🟢 Human AI Advisor  
🟢 Scenario Simulator  
🟢 Diplomacy Dashboard  
🟢 Mission Reports
"""
    )

    st.divider()

    st.markdown(
        """
**SYSTEM STATUS**

🛰️ Communication Array: ONLINE  
🧠 AI Core: ONLINE  
📡 Signal Decoder: ONLINE  
🤖 Alien Agent: STANDBY  
🔐 Mission Security: ACTIVE
"""
    )


# ============================================================
# START MISSION
# ============================================================

if start_button:

    st.session_state.alien = (
        generate_alien_civilization()
    )

    st.session_state.signal = (
        generate_alien_signal()
    )

    st.session_state.signal_analysis = (
        analyze_signal(
            st.session_state.signal
        )
    )

    st.session_state.trust = 50.0

    st.session_state.intent = (
        analyze_intent(
            st.session_state.alien,
            st.session_state.signal,
            0
        )
    )

    st.session_state.threat = (
        assess_threat(
            st.session_state.alien,
            st.session_state.trust,
            st.session_state.intent
        )
    )

    st.session_state.history = []

    st.session_state.mission_started = True

    st.session_state.scenario_result = None

    st.rerun()


# ============================================================
# WELCOME SCREEN
# ============================================================

if not st.session_state.mission_started:

    st.markdown(
        """
<div class="command-card">

<h1>🌌 FIRST CONTACT PROTOCOL</h1>

<p style="font-size:18px;color:#cbd5e1;">

An unknown intelligent signal has been detected
from deep space.

Your mission is to analyze the signal, determine
the civilization's intentions, establish communication,
manage diplomatic trust and decide how humanity should
respond.

</p>

<br>

<h3>MISSION OBJECTIVE</h3>

<p>
Analyze → Interpret → Communicate → Negotiate → Survive
</p>

</div>
""",
        unsafe_allow_html=True
    )

    a, b, c = st.columns(3)

    with a:

        st.markdown(
            """
<div class="metric-box">

<div class="metric-number">
15+
</div>

<div class="metric-label">
AI SIMULATION FEATURES
</div>

</div>
""",
            unsafe_allow_html=True
        )

    with b:

        st.markdown(
            """
<div class="metric-box">

<div class="metric-number">
AI
</div>

<div class="metric-label">
ALIEN INTELLIGENCE
</div>

</div>
""",
            unsafe_allow_html=True
        )

    with c:

        st.markdown(
            """
<div class="metric-box">

<div class="metric-number">
∞
</div>

<div class="metric-label">
POSSIBLE SCENARIOS
</div>

</div>
""",
            unsafe_allow_html=True
        )

    st.info(
        "👈 Click INITIATE FIRST CONTACT in Mission Control "
        "to begin the simulation."
    )

    st.stop()


# ============================================================
# DATA
# ============================================================

alien = st.session_state.alien
signal = st.session_state.signal
signal_analysis = st.session_state.signal_analysis
intent = st.session_state.intent
trust = st.session_state.trust
threat = st.session_state.threat
history = st.session_state.history


# ============================================================
# STATUS HEADER
# ============================================================

st.markdown(
    f"""
<div class="command-card">

<div style="display:flex;justify-content:space-between;">

<div>

<h2>👽 CONTACT ESTABLISHED</h2>

<span class="status-online">
● COMMUNICATION CHANNEL ACTIVE
</span>

</div>

<div style="text-align:right;color:#64748b;">

MISSION TIME<br>

<b style="color:#cbd5e1;">
{generate_timestamp()}
</b>

</div>

</div>

</div>
""",
    unsafe_allow_html=True
)


# ============================================================
# TOP METRICS
# ============================================================

m1, m2, m3, m4, m5 = st.columns(5)

with m1:

    st.metric(
        "🤝 TRUST",
        f"{trust:.0f}%"
    )

with m2:

    st.metric(
        "⚠️ THREAT",
        f"{threat['score']:.0f}%"
    )

with m3:

    st.metric(
        "🧠 INTELLIGENCE",
        f"{signal_analysis['intelligence_probability']:.0f}%"
    )

with m4:

    st.metric(
        "🔬 TECHNOLOGY",
        f"{alien['technology_index']}"
    )

with m5:

    st.metric(
        "📡 MESSAGES",
        len(history)
    )


# ============================================================
# MAIN TABS
# ============================================================

tabs = st.tabs(
    [
        "📡 Signal",
        "👽 Civilization",
        "🧠 Intent",
        "🤝 Diplomacy",
        "⚠️ Threat",
        "🗣️ Communication",
        "🔮 Scenarios",
        "🧠 AI Advisor",
        "📊 Dashboard",
        "📑 Mission Report"
    ]
)


# ============================================================
# SIGNAL TAB
# ============================================================

with tabs[0]:

    st.markdown(
        "## 📡 Extraterrestrial Signal Analysis"
    )

    c1, c2 = st.columns(2)

    with c1:

        st.markdown(
            """
<div class="signal-card">

<h3>RAW TRANSMISSION</h3>

<p style="
font-family:monospace;
font-size:16px;
color:#67e8f9;
word-break:break-all;
">

"""
            +
            signal["binary"]
            +
            """
</p>

</div>
""",
            unsafe_allow_html=True
        )

    with c2:

        st.markdown(
            """
<div class="signal-card">

<h3>SIGNAL CLASSIFICATION</h3>

"""
            +
            f"""
<p>
<b>Type:</b> {signal['signal_type']}
</p>

<p>
<b>Complexity:</b> {signal['complexity']}%
</p>

<p>
<b>Artificial Probability:</b>
{signal['artificial_probability']}%
</p>

<p>
<b>Origin Confidence:</b>
{signal['origin_confidence']}%
</p>

</div>
""",
            unsafe_allow_html=True
        )

    st.write("")

    signal_data = pd.DataFrame(
        {
            "Metric": [
                "Intelligence Probability",
                "Mathematical Structure",
                "Repetition Score",
                "Artificial Probability"
            ],

            "Value": [
                signal_analysis[
                    "intelligence_probability"
                ],

                signal_analysis[
                    "mathematical_structure"
                ],

                signal_analysis[
                    "repetition_score"
                ],

                signal[
                    "artificial_probability"
                ]
            ]
        }
    )

    fig = px.bar(
        signal_data,
        x="Metric",
        y="Value",
        range_y=[0, 100],
        template="plotly_dark",
        title="Signal Intelligence Metrics"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    st.success(
        f"🔎 Analysis: "
        f"{signal_analysis['pattern_classification']}"
    )


# ============================================================
# CIVILIZATION TAB
# ============================================================

with tabs[1]:

    st.markdown(
        "## 👽 Alien Civilization Profile"
    )

    st.markdown(
        f"""
<div class="alien-card">

<h2>
{alien['name']}
</h2>

<p>
<b>Species:</b> {alien['species']}
</p>

<p>
<b>Homeworld:</b> {alien['homeworld']}
</p>

<p>
<b>Civilization:</b> {alien['civilization_level']}
</p>

<p>
<b>Biology:</b> {alien['biological_type']}
</p>

<p>
<b>Communication:</b> {alien['communication_method']}
</p>

<p>
<b>Primary Value:</b> {alien['primary_value']}
</p>

<p>
<b>Energy:</b> {alien['energy_source']}
</p>

</div>
""",
        unsafe_allow_html=True
    )

    civilization_data = pd.DataFrame(
        {
            "Metric": [
                "Technology",
                "Aggression",
                "Curiosity",
                "Diplomacy"
            ],

            "Value": [
                alien["technology_index"],
                alien["aggression"],
                alien["curiosity"],
                alien["diplomacy"]
            ]
        }
    )

    fig = px.bar(
        civilization_data,
        x="Metric",
        y="Value",
        range_y=[0, 100],
        template="plotly_dark",
        title="Civilization Characteristics"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )


# ============================================================
# INTENT TAB
# ============================================================

with tabs[2]:

    st.markdown(
        "## 🧠 Alien Intent Analysis"
    )

    st.success(
        f"Detected Intent: {intent['intent']}"
    )

    a, b, c = st.columns(3)

    a.metric(
        "Peace Probability",
        f"{intent['peace_probability']}%"
    )

    b.metric(
        "Hostility Probability",
        f"{intent['hostility_probability']}%"
    )

    c.metric(
        "Confidence",
        f"{intent['confidence']}%"
    )

    st.write(
        "### Possible Objectives"
    )

    for goal in intent["possible_goals"]:

        st.write(
            f"🔹 {goal}"
        )

    chart = pd.DataFrame(
        {
            "Intent": [
                "Peace",
                "Hostility"
            ],

            "Probability": [
                intent["peace_probability"],
                intent["hostility_probability"]
            ]
        }
    )

    fig = px.pie(
        chart,
        names="Intent",
        values="Probability",
        hole=0.5,
        template="plotly_dark",
        title="Intent Probability"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )


# ============================================================
# DIPLOMACY TAB
# ============================================================

with tabs[3]:

    st.markdown(
        "## 🤝 Diplomatic Relationship"

    )

    st.progress(
        int(trust)
    )

    if trust >= 80:

        status = "🟢 Strong Alliance Potential"

    elif trust >= 60:

        status = "🟢 Positive Relations"

    elif trust >= 40:

        status = "🟡 Neutral Relations"

    elif trust >= 20:

        status = "🟠 Diplomatic Tension"

    else:

        status = "🔴 Critical Distrust"

    st.subheader(
        status
    )

    st.write(
        f"Current diplomatic trust: **{trust:.1f}%**"
    )

    if history:

        trust_history = []

        running = 50

        for item in history:

            running = item.get(
                "trust_after",
                running
            )

            trust_history.append(
                running
            )

        if trust_history:

            chart = pd.DataFrame(
                {
                    "Round": range(
                        1,
                        len(trust_history) + 1
                    ),

                    "Trust": trust_history
                }
            )

            fig = px.line(
                chart,
                x="Round",
                y="Trust",
                markers=True,
                range_y=[0, 100],
                template="plotly_dark",
                title="Diplomatic Trust Timeline"
            )

            st.plotly_chart(
                fig,
                use_container_width=True
            )


# ============================================================
# THREAT TAB
# ============================================================

with tabs[4]:

    st.markdown(
        "## ⚠️ Threat Assessment System"
    )

    score = threat["score"]

    if score < 20:
        st.success(
            f"THREAT LEVEL: {threat['level']}"
        )

    elif score < 60:
        st.warning(
            f"THREAT LEVEL: {threat['level']}"
        )

    else:
        st.error(
            f"THREAT LEVEL: {threat['level']}"
        )

    fig = go.Figure(
        go.Indicator(
            mode="gauge+number",
            value=score,
            title={
                "text": "Threat Score"
            },
            gauge={
                "axis": {
                    "range": [0, 100]
                }
            }
        )
    )

    fig.update_layout(
        template="plotly_dark",
        height=350
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    st.subheader(
        "Recommended Actions"
    )

    for recommendation in threat[
        "recommendations"
    ]:

        st.write(
            f"🛡️ {recommendation}"
        )


# ============================================================
# COMMUNICATION TAB
# ============================================================

with tabs[5]:

    st.markdown(
        "## 🗣️ First Contact Communication"
    )

    st.info(
        "You are the human diplomatic representative. "
        "Every message can influence trust and threat levels."
    )

    for item in history:

        if item["speaker"] == "Human":

            st.markdown(
                f"""
<div class="chat-human">

<b>👨‍🚀 HUMAN</b>

<br><br>

{item['message']}

</div>
""",
                unsafe_allow_html=True
            )

        else:

            st.markdown(
                f"""
<div class="chat-alien">

<b>👽 {alien['species'].upper()}</b>

<br><br>

{item['message']}

</div>
""",
                unsafe_allow_html=True
            )

    user_message = st.chat_input(
        "Send a message to the alien civilization..."
    )

    if user_message:

        previous_trust = st.session_state.trust

        trust_result = calculate_trust(
            previous_trust,
            user_message,
            alien
        )

        st.session_state.trust = (
            trust_result["trust"]
        )

        st.session_state.intent = (
            analyze_intent(
                alien,
                signal,
                len(history)
            )
        )

        st.session_state.threat = (
            assess_threat(
                alien,
                st.session_state.trust,
                st.session_state.intent
            )
        )

        alien_message = generate_alien_response(
            user_message,
            alien,
            st.session_state.trust,
            st.session_state.threat,
            history
        )

        st.session_state.history.append(
            {
                "speaker": "Human",
                "message": user_message,
                "time": generate_timestamp(),
                "trust_after": st.session_state.trust
            }
        )

        st.session_state.history.append(
            {
                "speaker": "Alien",
                "message": alien_message,
                "time": generate_timestamp(),
                "trust_after": st.session_state.trust
            }
        )

        st.rerun()


# ============================================================
# SCENARIO TAB
# ============================================================

with tabs[6]:

    st.markdown(
        "## 🔮 First Contact Scenario Simulator"
    )

    scenario = st.selectbox(
        "Choose a scenario",
        [
            "Peaceful Contact",
            "Scientific Exchange",
            "Military Escalation",
            "Cultural Exchange",
            "Resource Negotiation"
        ]
    )

    if st.button(
        "🔮 RUN SCENARIO"
    ):

        st.session_state.scenario_result = (
            simulate_scenario(
                alien,
                trust,
                threat["score"],
                scenario
            )
        )

    if st.session_state.scenario_result:

        result = (
            st.session_state.scenario_result
        )

        st.success(
            result["outcome"]
        )

        a, b, c = st.columns(3)

        a.metric(
            "Trust After",
            f"{result['trust_after']}%"
        )

        b.metric(
            "Threat After",
            f"{result['threat_after']}%"
        )

        c.metric(
            "Success Probability",
            f"{result['success_probability']}%"
        )


# ============================================================
# AI ADVISOR TAB
# ============================================================

with tabs[7]:

    st.markdown(
        "## 🧠 AI Diplomatic Decision Assistant"
    )

    situation = st.text_area(
        "Describe your current diplomatic situation",
        placeholder=(
            "Example: The alien civilization asks "
            "whether humanity possesses advanced weapons."
        )
    )

    if st.button(
        "🧠 GENERATE DIPLOMATIC ADVICE"
    ):

        if not situation:

            st.warning(
                "Describe the situation first."
            )

        else:

            advice = human_response_advisor(
                situation,
                alien,
                trust,
                threat["score"]
            )

            st.success(
                advice["recommendation"]
            )

            st.markdown(
                "### 💬 Suggested Response"
            )

            st.info(
                advice["suggested_message"]
            )

            st.metric(
                "AI Confidence",
                f"{advice['confidence']}%"
            )


# ============================================================
# DASHBOARD TAB
# ============================================================

with tabs[8]:

    st.markdown(
        "## 📊 Mission Intelligence Dashboard"
    )

    dashboard = pd.DataFrame(
        {
            "Metric": [
                "Trust",
                "Threat",
                "Technology",
                "Curiosity",
                "Diplomacy",
                "Aggression"
            ],

            "Value": [
                trust,
                threat["score"],
                alien["technology_index"],
                alien["curiosity"],
                alien["diplomacy"],
                alien["aggression"]
            ]
        }
    )

    fig = px.bar(
        dashboard,
        x="Metric",
        y="Value",
        range_y=[0, 100],
        template="plotly_dark",
        title="First Contact Intelligence Matrix"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    left, right = st.columns(2)

    with left:

        st.markdown(
            """
<div class="command-card">

<h3>🛰️ SYSTEM STATUS</h3>

<p>Signal Decoder ........ 🟢 ONLINE</p>
<p>Alien AI .............. 🟢 ACTIVE</p>
<p>Threat Engine ......... 🟢 ACTIVE</p>
<p>Trust Engine .......... 🟢 ACTIVE</p>
<p>Communication ......... 🟢 ACTIVE</p>

</div>
""",
            unsafe_allow_html=True
        )

    with right:

        st.markdown(
            """
<div class="command-card">

<h3>🎯 MISSION OBJECTIVE</h3>

<p>
Establish communication without escalating
the relationship into conflict.
</p>

<p>
Analyze unknown intelligence while maintaining
diplomatic awareness.
</p>

</div>
""",
            unsafe_allow_html=True
        )


# ============================================================
# MISSION REPORT TAB
# ============================================================

with tabs[9]:

    st.markdown(
        "## 📑 First Contact Mission Report"
    )

    report = generate_mission_report(
        alien,
        signal,
        signal_analysis,
        intent,
        trust,
        threat,
        history
    )

    st.text_area(
        "Mission Report",
        report,
        height=650
    )

    st.download_button(
        "📥 DOWNLOAD MISSION REPORT",
        data=report,
        file_name="PROJECT_CONTACT_MISSION_REPORT.txt",
        mime="text/plain",
        use_container_width=True
    )


# ============================================================
# FOOTER
# ============================================================

st.divider()

st.markdown(
    """
<div style="
text-align:center;
padding:25px;
color:#64748b;
">

<b style="color:#67e8f9;">
PROJECT CONTACT
</b>

<br>

AI First Contact & Extraterrestrial Communication Simulator

<br><br>

<small>
Fictional educational simulation.
No real extraterrestrial communication is performed.
</small>

</div>
""",
    unsafe_allow_html=True
)

