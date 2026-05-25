import random
import datetime

# ─────────────────────────────────────────
#  Response Database
# ─────────────────────────────────────────

responses = {
    "greetings": {
        "triggers": ["hello", "hi", "hey", "howdy", "greetings", "sup", "good morning", "good evening"],
        "replies": [
            "Hey there! 👋 Great to see you! How can I help?",
            "Hello! I'm your chatbot assistant. What's on your mind?",
            "Hi! Hope you're having a wonderful day. What can I do for you?",
        ],
    },
    "how_are_you": {
        "triggers": ["how are you", "how are you doing", "you okay", "you good", "how do you do"],
        "replies": [
            "I'm just a bot, but I'm doing great! Thanks for asking 😊",
            "All systems running smoothly! How about you?",
        ],
    },
    "name": {
        "triggers": ["what is your name", "what's your name", "who are you", "your name"],
        "replies": [
            "I'm ChatBot — your friendly rule-based assistant! 🤖",
            "They call me ChatBot. Nice to meet you!",
        ],
    },
    "joke": {
        "triggers": ["joke", "tell me a joke", "make me laugh", "something funny", "funny"],
        "replies": [
            "Why do programmers prefer dark mode? Because light attracts bugs! 🐛😄",
            "Why did the computer go to the doctor? Because it had a virus! 💻😂",
            "I told my computer I needed a break… now it won't stop sending me Kit-Kat ads. 🍫",
        ],
    },
    "help": {
        "triggers": ["help", "what can you do", "capabilities", "commands", "options", "features"],
        "replies": [
            (
                "Here's what I can do:\n"
                "  • Greet you 👋\n"
                "  • Tell jokes 😄\n"
                "  • Discuss AI & tech 🤖\n"
                "  • Tell you the time and date 🕐\n"
                "  • Keep you company!\n\n"
                "Just type anything!"
            )
        ],
    },
    "ai": {
        "triggers": ["what is ai", "artificial intelligence", "tell me about ai", "explain ai"],
        "replies": [
            "AI (Artificial Intelligence) is the simulation of human intelligence in machines. "
            "It includes machine learning, deep learning, NLP, and more! 🤖",
            "Artificial Intelligence lets computers learn, reason, and solve problems like humans. "
            "It powers everything from chatbots to self-driving cars! 🚗",
        ],
    },
    "time": {
        "triggers": ["what time", "current time", "what's the time", "time now"],
        "replies": ["dynamic_time"],
    },
    "date": {
        "triggers": ["what date", "today's date", "what day is it", "current date", "date today"],
        "replies": ["dynamic_date"],
    },
    "thanks": {
        "triggers": ["thanks", "thank you", "thx", "ty", "appreciate it"],
        "replies": [
            "You're welcome! 😊 Anything else I can help with?",
            "Happy to help! Let me know if you need anything else.",
        ],
    },
    "bye": {
        "triggers": ["bye", "goodbye", "exit", "quit", "see you", "later", "farewell", "cya"],
        "replies": [
            "Goodbye! Have an amazing day! 👋😊",
            "See you later! Take care! 🌟",
            "Bye! It was great chatting with you! 👋",
        ],
    },
}

fallbacks = [
    "Hmm, I'm not sure about that. Try asking me something else! 🤔",
    "I didn't quite catch that. Type 'help' to see what I can do!",
    "That's beyond my current knowledge. I'm still learning! 🌱",
]

EXIT_TRIGGERS = responses["bye"]["triggers"]

# ─────────────────────────────────────────
#  Core Logic
# ─────────────────────────────────────────

def get_bot_reply(user_input: str) -> str:
    """Match user input to a category and return a response."""
    lower = user_input.lower().strip()

    for category, data in responses.items():
        # Check if any trigger keyword is found in the user input
        if any(trigger in lower for trigger in data["triggers"]):
            reply = random.choice(data["replies"])

            # Handle dynamic replies
            if reply == "dynamic_time":
                return f"The current time is {datetime.datetime.now().strftime('%I:%M %p')} ⏰"
            elif reply == "dynamic_date":
                return f"Today is {datetime.datetime.now().strftime('%A, %B %d, %Y')} 📅"

            return reply

    # No match found — return a fallback
    return random.choice(fallbacks)


def is_exit(user_input: str) -> bool:
    """Check if the user wants to quit."""
    lower = user_input.lower().strip()
    return any(trigger in lower for trigger in EXIT_TRIGGERS)


# ─────────────────────────────────────────
#  Main Loop
# ─────────────────────────────────────────

def main():
    print("=" * 45)
    print("       Welcome to ChatBot 🤖")
    print("  Type 'help' to see what I can do.")
    print("  Type 'bye' or 'quit' to exit.")
    print("=" * 45)
    print("\nChatBot: Hey! I'm ChatBot — your friendly assistant. How can I help?\n")

    # Continuous loop — keeps running until user exits
    while True:
        user_input = input("You: ").strip()

        # Skip empty input
        if not user_input:
            continue

        # Check for exit command
        if is_exit(user_input):
            reply = random.choice(responses["bye"]["replies"])
            print(f"ChatBot: {reply}\n")
            break  # Exit the loop

        # Get and display bot reply
        reply = get_bot_reply(user_input)
        print(f"ChatBot: {reply}\n")


if __name__ == "__main__":
    main()


    