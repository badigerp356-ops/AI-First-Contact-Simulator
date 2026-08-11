
# ============================================================
# PROJECT CONTACT
# AI FIRST CONTACT SIMULATOR
# Backend / Intelligence Engine
# Python 3.12 compatible
# ============================================================

import os
import json
import random
import re
from datetime import datetime

# pyrefly: ignore [missing-import]
from dotenv import load_dotenv

# ------------------------------------------------------------
# OPTIONAL GEMINI SDK
# ------------------------------------------------------------

try:
    # pyrefly: ignore [missing-import]
    from google import genai
    GEMINI_AVAILABLE = True
except ImportError:
    GEMINI_AVAILABLE = False


load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

client = None

if GEMINI_AVAILABLE and GOOGLE_API_KEY:
    try:
        client = genai.Client(
            api_key=GOOGLE_API_KEY
        )
    except Exception:
        client = None


# ============================================================
# ALIEN DATA
# ============================================================

ALIEN_NAMES = [
    "Zyra",
    "Velkor",
    "Aethon",
    "Nexari",
    "Orvax",
    "Kryon",
    "Xelith",
    "Vael",
    "Tharion",
    "Elyra"
]

ALIEN_SPECIES = [
    "Aetherian",
    "Xenori",
    "Veylian",
    "Krythian",
    "Nexorian",
    "Orvani",
    "Zyphorian"
]

ALIEN_VALUES = [
    "knowledge",
    "survival",
    "exploration",
    "harmony",
    "technological advancement",
    "resource preservation",
    "scientific discovery"
]

ALIEN_GREETINGS = [
    "We observe your signal.",
    "Your transmission has reached our system.",
    "We recognize structured intelligence within your signal.",
    "Your species has crossed the communication threshold.",
    "We acknowledge your presence."
]

ALIEN_RESPONSES = [
    "We seek to understand your intentions.",
    "Your question requires further observation.",
    "We do not yet classify your civilization as hostile.",
    "Your technology is primitive by our measurements, but interesting.",
    "Communication between our civilizations may be possible.",
    "We are analyzing the meaning behind your transmission."
]


# ============================================================
# UTILITY
# ============================================================

def clamp(value, low=0, high=100):
    return max(low, min(high, value))


def random_name():
    return random.choice(ALIEN_NAMES)


def generate_timestamp():
    return datetime.now().strftime("%H:%M:%S")


# ============================================================
# ALIEN CIVILIZATION GENERATOR
# ============================================================

def generate_alien_civilization():

    technology = random.randint(45, 98)
    aggression = random.randint(5, 75)
    curiosity = random.randint(50, 99)
    diplomacy = random.randint(35, 95)

    if technology < 55:
        civilization_level = "Early Interstellar"

    elif technology < 70:
        civilization_level = "Interstellar"

    elif technology < 85:
        civilization_level = "Advanced Interstellar"

    else:
        civilization_level = "Post-Interstellar"

    population = random.randint(
        1,
        900
    )

    return {
        "name": random_name(),
        "species": random.choice(ALIEN_SPECIES),
        "homeworld": random.choice([
            "Kepler-442b",
            "Tau Ceti IV",
            "Proxima-7",
            "Epsilon Prime",
            "TRAPPIST-9",
            "Unknown Sector"
        ]),
        "civilization_level": civilization_level,
        "technology_index": technology,
        "aggression": aggression,
        "curiosity": curiosity,
        "diplomacy": diplomacy,
        "population_billions": population,
        "primary_value": random.choice(ALIEN_VALUES),
        "communication_method": random.choice([
            "Electromagnetic pulses",
            "Quantum modulation",
            "Encoded mathematics",
            "Neural resonance",
            "Multispectral signals"
        ]),
        "energy_source": random.choice([
            "Stellar harvesting",
            "Fusion",
            "Antimatter",
            "Quantum energy",
            "Artificial singularity"
        ]),
        "biological_type": random.choice([
            "Carbon-based",
            "Silicon-carbon hybrid",
            "Silicon-based",
            "Unknown biochemical structure",
            "Non-standard biological system"
        ])
    }


# ============================================================
# SIGNAL GENERATOR
# ============================================================

def generate_alien_signal():

    signal_types = [
        "Mathematical sequence",
        "Pulsed electromagnetic signal",
        "Prime-number sequence",
        "Binary transmission",
        "Repeating harmonic pattern",
        "Encoded geometric pattern"
    ]

    signal_type = random.choice(signal_types)

    binary = "".join(
        random.choice("01")
        for _ in range(48)
    )

    numbers = [
        random.choice([
            2, 3, 5, 7, 11, 13, 17, 19,
            23, 29, 31, 37, 41, 43
        ])
        for _ in range(8)
    ]

    complexity = random.randint(20, 95)

    return {
        "signal_type": signal_type,
        "binary": binary,
        "mathematical_sequence": numbers,
        "complexity": complexity,
        "origin_confidence": random.randint(70, 99),
        "artificial_probability": random.randint(75, 99),
        "repeating_pattern": random.choice([
            True,
            False
        ])
    }


# ============================================================
# SIGNAL ANALYZER
# ============================================================

def analyze_signal(signal):

    complexity = signal["complexity"]

    if complexity < 35:
        pattern = "Low-complexity pattern"

    elif complexity < 65:
        pattern = "Structured communication"

    elif complexity < 85:
        pattern = "Highly structured intelligence"

    else:
        pattern = "Extremely sophisticated encoding"

    if signal["artificial_probability"] > 85:
        origin = "Likely artificial"

    else:
        origin = "Origin uncertain"

    return {
        "pattern_classification": pattern,
        "origin_assessment": origin,
        "intelligence_probability": round(
            clamp(
                signal["artificial_probability"] +
                random.randint(-8, 8)
            ),
            1
        ),
        "complexity_score": complexity,
        "mathematical_structure": random.randint(
            60,
            99
        ),
        "repetition_score": random.randint(
            40,
            95
        ),
        "decoded_symbols": random.randint(
            3,
            24
        )
    }


# ============================================================
# INTENT ANALYZER
# ============================================================

def analyze_intent(
    alien,
    signal,
    conversation_count=0
):

    curiosity = alien["curiosity"]
    aggression = alien["aggression"]
    diplomacy = alien["diplomacy"]

    peaceful = (
        diplomacy * 0.45 +
        curiosity * 0.35 -
        aggression * 0.20
    )

    peaceful = clamp(peaceful)

    if peaceful >= 75:
        intent = "Highly Diplomatic"

    elif peaceful >= 55:
        intent = "Cautiously Peaceful"

    elif peaceful >= 40:
        intent = "Uncertain"

    elif peaceful >= 25:
        intent = "Potentially Hostile"

    else:
        intent = "Hostile"

    possible_goals = []

    if curiosity > 70:
        possible_goals.append(
            "Scientific information exchange"
        )

    if diplomacy > 65:
        possible_goals.append(
            "Diplomatic communication"
        )

    if aggression > 60:
        possible_goals.append(
            "Strategic assessment"
        )

    if not possible_goals:
        possible_goals.append(
            "Observation"
        )

    return {
        "intent": intent,
        "peace_probability": round(
            peaceful,
            1
        ),
        "hostility_probability": round(
            100 - peaceful,
            1
        ),
        "possible_goals": possible_goals,
        "confidence": random.randint(
            55,
            94
        )
    }


# ============================================================
# TRUST ENGINE
# ============================================================

def calculate_trust(
    current_trust,
    user_message,
    alien
):

    message = user_message.lower()

    positive_words = [
        "peace",
        "hello",
        "friend",
        "cooperation",
        "help",
        "understand",
        "learn",
        "together",
        "welcome"
    ]

    negative_words = [
        "attack",
        "weapon",
        "destroy",
        "threat",
        "invade",
        "enemy",
        "control"
    ]

    positive_score = sum(
        word in message
        for word in positive_words
    )

    negative_score = sum(
        word in message
        for word in negative_words
    )

    change = (
        positive_score * random.uniform(1.5, 4.0)
        -
        negative_score * random.uniform(2.0, 5.0)
    )

    change += random.uniform(
        -2,
        3
    )

    new_trust = clamp(
        current_trust + change
    )

    if new_trust >= 80:
        status = "Strong Alliance Potential"

    elif new_trust >= 60:
        status = "Positive Relations"

    elif new_trust >= 40:
        status = "Neutral Relations"

    elif new_trust >= 20:
        status = "Diplomatic Tension"

    else:
        status = "Critical Distrust"

    return {
        "trust": round(new_trust, 1),
        "change": round(
            new_trust - current_trust,
            1
        ),
        "status": status
    }


# ============================================================
# THREAT ASSESSMENT
# ============================================================

def assess_threat(
    alien,
    trust,
    intent
):

    aggression = alien["aggression"]

    base_threat = (
        aggression * 0.5 +
        (100 - trust) * 0.35 +
        intent["hostility_probability"] * 0.15
    )

    base_threat = clamp(
        base_threat
    )

    if base_threat < 20:
        level = "MINIMAL"

    elif base_threat < 40:
        level = "LOW"

    elif base_threat < 60:
        level = "MODERATE"

    elif base_threat < 80:
        level = "HIGH"

    else:
        level = "CRITICAL"

    recommendations = []

    if base_threat > 65:
        recommendations.append(
            "Maintain defensive readiness"
        )
        recommendations.append(
            "Avoid sharing sensitive information"
        )
        recommendations.append(
            "Use diplomatic communication"
        )

    elif base_threat > 40:
        recommendations.append(
            "Continue observation"
        )
        recommendations.append(
            "Increase signal analysis"
        )
        recommendations.append(
            "Avoid aggressive language"
        )

    else:
        recommendations.append(
            "Continue peaceful communication"
        )
        recommendations.append(
            "Explore scientific exchange"
        )

    return {
        "score": round(base_threat, 1),
        "level": level,
        "recommendations": recommendations
    }


# ============================================================
# LOCAL ALIEN RESPONSE
# ============================================================

def local_alien_response(
    message,
    alien,
    trust,
    threat
):

    lower = message.lower()

    if any(
        word in lower
        for word in [
            "hello",
            "hi",
            "greetings"
        ]
    ):
        return random.choice(
            ALIEN_GREETINGS
        )

    if "who are you" in lower:
        return (
            f"We are the {alien['species']} of "
            f"{alien['homeworld']}. Our civilization "
            f"classifies itself as "
            f"{alien['civilization_level']}."
        )

    if "peace" in lower:
        return (
            "Your reference to peace has increased "
            "our confidence in continued communication. "
            "We are willing to exchange knowledge."
        )

    if "technology" in lower:
        return (
            f"Our technological index is approximately "
            f"{alien['technology_index']} on your "
            f"normalized scale. We prioritize "
            f"{alien['primary_value']}."
        )

    if "home" in lower or "planet" in lower:
        return (
            f"Our civilization originates from "
            f"{alien['homeworld']}. Our biological "
            f"structure is classified as "
            f"{alien['biological_type']}."
        )

    if "attack" in lower or "weapon" in lower:
        return (
            "Your use of aggressive terminology has "
            "increased our defensive assessment. "
            "We recommend clarification."
        )

    return random.choice(
        ALIEN_RESPONSES
    )


# ============================================================
# GEMINI RESPONSE
# ============================================================

def gemini_response(
    user_message,
    alien,
    trust,
    threat,
    history
):

    if client is None:
        return None

    history_text = "\n".join(
        [
            f"{item['speaker']}: {item['message']}"
            for item in history[-8:]
        ]
    )

    prompt = f"""
You are the alien intelligence inside an educational
AI First Contact Simulation called PROJECT CONTACT.

This is a fictional simulation.

ALIEN CIVILIZATION:
{json.dumps(alien, indent=2)}

CURRENT TRUST:
{trust}

CURRENT THREAT:
{threat}

RECENT COMMUNICATION:
{history_text}

USER MESSAGE:
{user_message}

Respond as the extraterrestrial civilization.

Rules:
1. Stay in character.
2. Be intelligent and mysterious.
3. Do not claim the simulation is real.
4. Do not provide real-world dangerous instructions.
5. Keep the response between 2 and 6 paragraphs.
6. The alien should have a consistent personality.
7. The response can reveal fictional scientific/cultural information.
8. React to the user's diplomatic tone.
"""

    try:

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        return response.text

    except Exception:
        return None


# ============================================================
# MAIN CHAT ENGINE
# ============================================================

def generate_alien_response(
    user_message,
    alien,
    trust,
    threat,
    history
):

    response = gemini_response(
        user_message,
        alien,
        trust,
        threat,
        history
    )

    if response:
        return response

    return local_alien_response(
        user_message,
        alien,
        trust,
        threat
    )


# ============================================================
# HUMAN AI COMMUNICATION ASSISTANT
# ============================================================

def human_response_advisor(
    situation,
    alien,
    trust,
    threat
):

    if trust > 70 and threat < 35:

        recommendation = (
            "Use a cooperative diplomatic response. "
            "Focus on scientific exchange and mutual understanding."
        )

    elif threat > 65:

        recommendation = (
            "Use cautious diplomatic language. "
            "Avoid revealing sensitive information and "
            "request clarification of intentions."
        )

    else:

        recommendation = (
            "Maintain neutral communication and ask "
            "questions that reveal the civilization's intentions."
        )

    return {
        "recommendation": recommendation,
        "suggested_message": (
            "We acknowledge your communication and seek "
            "peaceful understanding. We propose an exchange "
            "of scientific knowledge while respecting the "
            "boundaries of both civilizations."
        ),
        "confidence": random.randint(
            70,
            96
        )
    }


# ============================================================
# SCENARIO SIMULATOR
# ============================================================

def simulate_scenario(
    alien,
    trust,
    threat,
    scenario
):

    scenarios = {

        "Peaceful Contact": {
            "trust_change": random.uniform(8, 20),
            "threat_change": random.uniform(-10, -2),
            "outcome": "Diplomatic relationship established"
        },

        "Scientific Exchange": {
            "trust_change": random.uniform(5, 16),
            "threat_change": random.uniform(-8, 2),
            "outcome": "Scientific knowledge exchange begins"
        },

        "Military Escalation": {
            "trust_change": random.uniform(-30, -10),
            "threat_change": random.uniform(15, 35),
            "outcome": "Communication enters a dangerous phase"
        },

        "Cultural Exchange": {
            "trust_change": random.uniform(10, 22),
            "threat_change": random.uniform(-12, -3),
            "outcome": "Cross-civilizational cultural exchange"
        },

        "Resource Negotiation": {
            "trust_change": random.uniform(-5, 12),
            "threat_change": random.uniform(-5, 15),
            "outcome": "Long-term resource negotiations begin"
        }
    }

    result = scenarios.get(
        scenario,
        scenarios["Peaceful Contact"]
    )

    new_trust = clamp(
        trust + result["trust_change"]
    )

    new_threat = clamp(
        threat + result["threat_change"]
    )

    return {
        "scenario": scenario,
        "trust_before": round(trust, 1),
        "trust_after": round(new_trust, 1),
        "threat_before": round(threat, 1),
        "threat_after": round(new_threat, 1),
        "outcome": result["outcome"],
        "success_probability": round(
            clamp(
                50 +
                (new_trust - new_threat) * 0.5
            ),
            1
        )
    }


# ============================================================
# MISSION REPORT
# ============================================================

def generate_mission_report(
    alien,
    signal,
    signal_analysis,
    intent,
    trust,
    threat,
    history
):

    communication_count = len(history)

    report = f"""
============================================================
              PROJECT CONTACT
        AI FIRST CONTACT MISSION REPORT
============================================================

MISSION TIMESTAMP
------------------------------------------------------------
{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}

ALIEN CIVILIZATION
------------------------------------------------------------
Species              : {alien['species']}
Civilization Name    : {alien['name']}
Homeworld            : {alien['homeworld']}
Civilization Level   : {alien['civilization_level']}
Technology Index     : {alien['technology_index']}
Population           : {alien['population_billions']} Billion
Primary Value        : {alien['primary_value']}
Communication        : {alien['communication_method']}
Energy Source        : {alien['energy_source']}
Biological Type      : {alien['biological_type']}

SIGNAL ANALYSIS
------------------------------------------------------------
Signal Type          : {signal['signal_type']}
Complexity           : {signal['complexity']}
Artificial Probability: {signal['artificial_probability']}%
Origin Confidence    : {signal['origin_confidence']}%

Pattern Classification:
{signal_analysis['pattern_classification']}

Origin Assessment:
{signal_analysis['origin_assessment']}

INTENT ANALYSIS
------------------------------------------------------------
Intent               : {intent['intent']}
Peace Probability    : {intent['peace_probability']}%
Hostility Probability: {intent['hostility_probability']}%
Confidence           : {intent['confidence']}%

TRUST ANALYSIS
------------------------------------------------------------
Current Trust        : {trust}%
Relationship Status   :
{calculate_trust(
    trust,
    "peace cooperation",
    alien
)['status']}

THREAT ASSESSMENT
------------------------------------------------------------
Threat Score         : {threat['score']}%
Threat Level         : {threat['level']}

RECOMMENDATIONS
------------------------------------------------------------
"""

    for recommendation in threat["recommendations"]:
        report += f"- {recommendation}\n"

    report += f"""

COMMUNICATION STATISTICS
------------------------------------------------------------
Messages Recorded    : {communication_count}

MISSION CONCLUSION
------------------------------------------------------------
The current simulation indicates that continued
communication should be evaluated using trust,
intent, threat assessment, and diplomatic behavior.

This report is generated from a fictional simulation
for educational and demonstration purposes.

============================================================
             END OF MISSION REPORT
============================================================
"""

    return report

