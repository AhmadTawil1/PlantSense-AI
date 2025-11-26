🌿 Smart Plant Monitor
AI-powered system for plant health monitoring, image diagnosis, and personalized care guidance.
Overview

Smart Plant Monitor is an intelligent plant-care assistant that combines IoT sensors, computer vision, RAG search, and gamification to help users care for plants easily — from home users to agricultural growers.

Features

Real-time sensor dashboard (Moisture / Temperature / Light / Water Pressure)

AI-based image diagnosis (leaf issues, diseases, dryness, pests)

RAG assistant for plant-care guidance

Alerts & notifications with predictions

Daily missions + XP + achievements

Multi-plant support

User-adaptive dashboard (simple / professional modes)



System Architecture (SOON)



Personas

Home Plant Owner + Agricultural Grower



Tech Stack (Future Use)

Python (Colab + Jupyter)

LangChain / RAG

ipywidgets interface

Firebase (Auth, Firestore, Storage)

MQTT for sensor pipeline

FastAPI (optional backend)

👥 Team
Member	Role	Tasks (for v1)
Ahmad Tawil	System Lead	Requirements, convergent thinking, success story research
Cyrine	UX Researcher	Persona interviews + insights
Aya	UX Researcher	Persona interviews + insights
Adam	UI Designer	Initial screen designs
Wail	System Modeling	Use Case Diagram



📂 Folder Structure (Expected)
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

