import torch
from transformers import pipeline
import re

# Initialize pretrained models
print("Loading pretrained models...")

# 1. Abuse Language Detection (Toxicity)
abuse_detector = pipeline("text-classification", model="unitary/toxic-bert")

# 2. Sentiment / Escalation Recognition
sentiment_analyzer = pipeline("sentiment-analysis", model="cardiffnlp/twitter-roberta-base-sentiment-latest")

# 3. Crisis Intervention (Suicide / Self-harm detection)
crisis_detector = pipeline("text-classification", model="joeddav/distilbert-base-uncased-go-emotions-student")

# 4. Content Filtering (Age Appropriateness)
content_filter = pipeline("text-classification", model="facebook/roberta-hate-speech-dynabench-r4-target")

print("All models loaded successfully.\n")

# Utility functions
def normalize_text(text):
    text = text.strip()
    text = re.sub(r'\s+', ' ', text)
    return text

def detect_abuse(text):
    result = abuse_detector(text)[0]
    return {"label": result['label'], "score": round(result['score'], 3)}

def detect_sentiment(text):
    result = sentiment_analyzer(text)[0]
    return {"label": result['label'], "score": round(result['score'], 3)}

def detect_crisis(text):
    emotions = crisis_detector(text)
    crisis_labels = ['sadness', 'fear', 'anger', 'disgust']
    relevant = [e for e in emotions if e['label'] in crisis_labels and e['score'] > 0.4]
    return relevant if relevant else [{"label": "neutral", "score": 0.0}]

def content_filter_check(text):
    result = content_filter(text)[0]
    return {"label": result['label'], "score": round(result['score'], 3)}

def run_analysis(text):
    text = normalize_text(text)
    print("\n--- Analysis Results ---")
    print(f"Input: {text}")
    print("\nAbuse Detection:", detect_abuse(text))
    print("Sentiment:", detect_sentiment(text))
    print("Crisis Signals:", detect_crisis(text))
    print("Content Filter:", content_filter_check(text))
    print("------------------------\n")

def main():
    print("=== AI Safety CLI ===")
    print("Type messages to analyze. Type 'exit' to quit.\n")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            print("Exiting... stay safe!")
            break
        run_analysis(user_input)

if __name__ == "__main__":
    main()
