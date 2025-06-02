import json
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")
FILENAME = os.path.join(DATA_DIR, "knowledge.json")

def load_knowledge():
    if os.path.exists(FILENAME):
        with open(FILENAME, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}

def save_knowledge(knowledge):
    with open(FILENAME, "w", encoding="utf-8") as f:
        json.dump(knowledge, f, indent=2)

def get_answer(knowledge, question):
    return knowledge.get(question.lower())

def learn(knowledge, question, answer):
    knowledge[question.lower()] = answer
    save_knowledge(knowledge)
