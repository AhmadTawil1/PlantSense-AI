# 🌿 Smart Plant Monitor (PlantSense AI)
> **AI-powered system for plant health monitoring, image diagnosis, and personalized care guidance.**

## 📖 Overview
**Smart Plant Monitor** is an intelligent plant-care assistant that combines IoT sensors, computer vision, RAG search, and gamification to help users care for plants easily. Built as a modular Python application for Google Colab, it bridges the gap between home gardening and professional agricultural growing.

## ✨ Key Features
* **📊 Real-time Sensor Dashboard:** Monitors Moisture, Temperature, Light, and Water Pressure via MQTT/HTTPS.
* **🍂 AI-Based Diagnosis:** Uses Vision Transformers (HuggingFace) to extract features and diagnose plant health.
* **🤖 RAG Assistant:** An AI chatbot powered by Vector Stores (Chroma/FAISS) to answer questions from a verified knowledge base.
* **🔔 Smart Alerts:** A dedicated Microservice Notification Engine for real-time alerts.
* **🏆 Gamification:** A feedback loop engine that tracks User Actions to award Points, Daily Missions, and Achievements.
* **🌱 Multi-Plant Support:** Scalable architecture backed by Firebase Firestore.

## 🏗️ System Architecture
The system follows a **Microservices-based architecture**, separating the UI, AI logic, and Data handling into distinct layers.

![System Architecture](docs/mermaid-diagram-2025-11-17-213524.jpg)

### 1. 🖥️ User Interface Layer
* **Component:** `UI / Colab Widgets / Web Dashboard`
* **Function:** Serves as the central hub for User Input and Data Visualization.
* **Flow:** Sends user actions to the Gamification Engine and queries to the RAG Engine.

### 2. 📡 IoT Sensor Layer
* **Sensors:** Soil Moisture, Temperature, Light, Water Pressure.
* **Function:** Collects physical environmental data.
* **Protocol:** Transmits data via **MQTT/HTTPS** directly to the Cloud Backend.

### 3. ☁️ Cloud Backend Layer
* **Database:** **Firebase Realtime DB / Firestore** stores user data, sensor logs, and plant profiles.
* **Storage:** **Firebase Storage** handles high-resolution plant image uploads.
* **Notification Engine:** A dedicated microservice that monitors data streams and triggers alerts (e.g., "Water Now").

### 4. 🧠 AI & Intelligence Layer
* **Vision Engine:**
    * Uses **Vision Transformers / HuggingFace Models** for Feature Extraction.
    * The **Plant Health Analyzer** microservice processes these features to generate a Health Score.
* **RAG Engine (Chat):**
    * Converts user questions using an **Embedding Model**.
    * Retrieves context from a **Vector Store (Chroma/FAISS)**.
    * Generates accurate answers via an **LLM Answer Generator**.

### 5. 🎮 Gamification Engine
* **Function:** Tracks "Daily Usage" and "User Actions" (like watering or scanning).
* **Output:** Updates the dashboard with Points, Levels, and Achievements to motivate the user.

## 📂 Project Structure
This project follows a **Vertical Slice Architecture** (MVC), where each feature is a self-contained module.

```text
PlantSense-AI/
│
├── main.py                 # Entry point: Handles navigation & main layout
│
├── utils/
│   ├── __init__.py
│   └── styles.py           # Central Design System (CSS, Colors, Shared Widgets)
│
├── components/
│   ├── __init__.py
│   └── header.py           # Shared Navigation Header
│
├── pages/                  # Feature Modules (Microservice Logic)
│   ├── home/               # Main Dashboard & Plant Profile
│   ├── sensors/            # IoT Graphs & Firebase Connection
│   ├── analysis/           # Vision Transformer Integration
│   ├── chat/               # RAG Pipeline (Chroma/FAISS)
│   ├── rewards/            # Gamification Engine Logic
│   ├── alerts/             # Notification Engine Logic
│   └── auth/               # User Authentication
│
├── docs/                   # Documentation & Diagrams
└── README.md
