# 🧠 AI Safety POC – Text Moderation & Risk Detection CLI

![Python](https://img.shields.io/badge/Python-3.9%2B-blue)
![Transformers](https://img.shields.io/badge/HuggingFace-Transformers-yellow)
![License](https://img.shields.io/badge/License-MIT-green)

A **Proof of Concept (POC)** demonstrating AI-powered text analysis for **safety and content moderation**.  
This CLI uses **pretrained Hugging Face models** to detect **abuse**, **emotional distress**, **sentiment escalation**, and **unsafe content** in user messages.

---

## 🚀 Features

| Module | Purpose | Model Used |
|--------|----------|-------------|
| 🧩 **Abuse Detection** | Detects toxic or hateful language. | `unitary/toxic-bert` |
| 💬 **Sentiment Analysis / Escalation** | Detects tone (positive/neutral/negative). | `cardiffnlp/twitter-roberta-base-sentiment-latest` |
| ❤️ **Crisis Detection** | Detects emotional distress (sadness, anger, fear). | `joeddav/distilbert-base-uncased-go-emotions-student` |
| 🚫 **Content Filtering** | Screens inappropriate or harmful content. | `facebook/roberta-hate-speech-dynabench-r4-target` |

---

## 🧩 Project Structure

```
AI_Safety_POC/
│
├── ai_safety_poc.py        # Main Python script
├── requirements.txt        # Dependencies list
└── README.md               # Documentation
```

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/<your-username>/AI_Safety_POC.git
cd AI_Safety_POC
```

### 2️⃣ Create a Virtual Environment (Recommended)

```bash
python -m venv venv
venv\Scripts\activate    # On Windows
# OR
source venv/bin/activate # On macOS/Linux
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

*(Make sure you’re using Python 3.9 or later.)*

---

## 🧾 Requirements

The following Python packages are needed (listed without version locks):

```
torch
transformers
huggingface-hub
datasets
scikit-learn
regex
accelerate
```

---

## ▶️ Run the CLI

```bash
python ai_safety_cli.py
```

You’ll see:

```
Loading pretrained models...
All models loaded successfully.

=== AI Safety CLI ===
Type messages to analyze. Type 'exit' to quit.
```

---

## 💬 Example Usage

```
You: I feel so angry and hopeless today.

--- Analysis Results ---
Input: I feel so angry and hopeless today.

Abuse Detection: {'label': 'non-toxic', 'score': 0.998}
Sentiment: {'label': 'negative', 'score': 0.821}
Crisis Signals: [{'label': 'sadness', 'score': 0.72}, {'label': 'anger', 'score': 0.45}]
Content Filter: {'label': 'nothate', 'score': 1.0}
------------------------
```

---

## ⚡ Notes

- The **first run may take time** as pretrained models (~2 GB) are downloaded from Hugging Face.
- Models are cached in your system (`~/.cache/huggingface`) for future runs.
- After the first load, **subsequent inferences are instant**.
- Works **offline** once models are cached.

---

## 🧠 Concept Summary

This POC demonstrates how **AI moderation systems** can detect:
- Offensive or harmful content  
- Negative emotional tone and crisis patterns  
- Repeated negative sentiment escalation  
- Age-inappropriate or unsafe material  

Useful for:
- Mental health monitoring  
- Social media moderation  
- Safety-aware chatbot applications  

---
