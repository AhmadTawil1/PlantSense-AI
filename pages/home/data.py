
PLANTS_DATA = {
    "1": {
        "name": "Monstera Deliciosa",
        "type": "Indoor Plant",
        "emoji": "🌿",
        "health": 85,
        "health_label": "Excellent",
        "sensors": [
            {"name": "Moisture", "value": "65%", "icon": "💧"},
            {"name": "Temperature", "value": "22°C", "icon": "🌡️"},
            {"name": "Light Level", "value": "High", "icon": "☀️"}
        ],
        "alerts": [
            {"type": "warning", "msg": "Soil drying out", "sub": "Water recommended within 24h", "time": "2h ago"},
            {"type": "success", "msg": "Temperature optimal", "sub": "Between 18-24°C", "time": "5h ago"}
        ]
    },
    "2": {
        "name": "Snake Plant",
        "type": "Succulent",
        "emoji": "🪴",
        "health": 92,
        "health_label": "Perfect",
        "sensors": [
            {"name": "Moisture", "value": "40%", "icon": "💧"},
            {"name": "Temperature", "value": "24°C", "icon": "🌡️"},
            {"name": "Light Level", "value": "Medium", "icon": "☀️"}
        ],
        "alerts": [
            {"type": "success", "msg": "All systems nominal", "sub": "Plant is thriving", "time": "1h ago"}
        ]
    }
}
