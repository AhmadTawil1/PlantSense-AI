
CHAT_HISTORY = [
    {"role": "ai", "content": "Hello! I'm your AI plant assistant. I can help you with plant care advice, diagnose issues, and answer questions about your Monstera. How can I help you today?"},
    {"role": "user", "content": "Why are some of my leaves turning yellow?"},
    {"role": "ai", "content": """Based on your current sensor readings (moisture at 65%), yellowing leaves could indicate:
    <ul style='margin: 5px 0 5px 20px;'>
        <li>Overwatering - though your levels look okay</li>
        <li>Natural aging of lower leaves (normal)</li>
        <li>Nitrogen deficiency - consider fertilizing</li>
    </ul>
    I'd recommend checking if it's only the older, lower leaves. If so, this is natural!"""}
]

CONTEXT_DATA = {
    "moisture": "65%",
    "temperature": "22°C",
    "plant_type": "Monstera"
}

SUGGESTED_QUESTIONS = [
    "How often should I water?",
    "Best fertilizer schedule?",
    "Optimal light conditions?",
    "Common pest problems?"
]
