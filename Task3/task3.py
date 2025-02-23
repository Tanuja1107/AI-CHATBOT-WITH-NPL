import spacy
import warnings

# Suppress any warnings (if needed)
warnings.filterwarnings("ignore", category=UserWarning, module="spacy")

# Load the English NLP model from spaCy
nlp = spacy.load("en_core_web_sm")

# Define intents and responses
intents = {
    "greeting": ["hello", "hi", "hey", "greetings"],
    "goodbye": ["bye", "goodbye", "see you later"],
    "thanks": ["thanks", "thank you", "I appreciate it"],
    "help": ["help", "assist", "support"],
    "weather": ["weather", "forecast", "temperature"],
}

responses = {
    "greeting": "Hello! How can I assist you today?",
    "goodbye": "Goodbye! Have a great day!",
    "thanks": "You're welcome! Let me know if you need anything else.",
    "help": "Sure, I'm here to help. Ask me anything!",
    "weather": "I'm not a weather bot, but you can check the weather online!",
    "default": "I'm sorry, I didn't understand that. Can you rephrase?"
}

# Function to classify user input using exact keyword matching
def classify_intent(user_input):
    user_input = user_input.lower()
    for intent, keywords in intents.items():
        for keyword in keywords:
            if keyword in user_input:  # Exact match
                return intent
    return "default"

# Chatbot interaction loop
def chatbot():
    print("AI Chatbot: Hi there! Type 'quit' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "quit":
            print("AI Chatbot: Goodbye!")
            break
        intent = classify_intent(user_input)
        print("AI Chatbot:", responses[intent])

if __name__ == "__main__":
    chatbot()
