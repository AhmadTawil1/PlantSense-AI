# 🌿 Smart Plant Monitor
> **AI-powered system for plant health monitoring, image diagnosis, and personalized care guidance.**

## 📖 Overview
**Smart Plant Monitor** is an intelligent plant-care assistant that combines IoT sensors, computer vision, RAG search, and gamification to help users care for plants easily — bridging the gap between home gardening and agricultural growing.

## ✨ Key Features
* **📊 Real-time Sensor Dashboard:** Monitors Moisture, Temperature, Light, and Water Pressure.
* **🍂 AI-Based Diagnosis:** Computer vision analysis for leaf issues, diseases, dryness, and pests.
* **🤖 RAG Assistant:** An AI chatbot for personalized plant-care guidance.
* **🔔 Smart Alerts:** Notifications with predictive analysis.
* **🏆 Gamification:** Daily missions, XP system, and achievements.
* **🌱 Multi-Plant Support:** Manage multiple plants in one interface.
* **🎛️ Adaptive Interface:** Toggles between 'Simple' and 'Professional' modes based on user needs.

## 👥 Target Personas
1. **Home Plant Owner:** Hobbyists looking for ease of care.
2. **Agricultural Grower:** Professionals needing data and scale.

## 🛠️ Tech Stack (Future Roadmap)
* **Core:** Python (Colab + Jupyter)
* **AI & ML:** LangChain / RAG
* **Interface:** ipywidgets
* **Backend & Data:** Firebase (Auth, Firestore, Storage)
* **IoT:** MQTT for sensor pipelines
* **API:** FastAPI (Optional)

## 🏗️ System Architecture
*(Coming Soon)*

## 🤝 Team
| Member | Role | Key Tasks (v1) |
| :--- | :--- | :--- |
| **Ahmad Tawil** | System Lead | Requirements, Convergent thinking, Success stories |
| **Cyrine** | UX Researcher | Persona interviews + Insights |
| **Aya** | UX Researcher | Persona interviews + Insights |
| **Adam** | UI Designer | Initial screen designs |
| **Wail** | System Modeling | Use Case Diagram |

## 📂 Project Structure
```text
smart-plant-monitor/
│
├── docs/
│   ├── persona-interviews/
│   ├── design-thinking/
│   ├── use-case-diagrams/
│   └── architecture/
│
├── ui-design/
│   ├── home/
│   ├── sensors/
│   ├── analysis/
│   ├── ai-chat/
│   ├── rewards/
│   └── alerts/
│
├── notebooks/
│   ├── colab_widgets/
│   ├── image_analysis/
│   └── rag/
│
├── backend/
│   ├── mqtt/
│   ├── firebase/
│   └── api/
│
├── data/
│   ├── examples/
│   └── sensors-simulated/
│
└── README.md
