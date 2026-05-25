 🤖 ChatBot 
---

## 📌 What This Project Does

This is a **rule-based chatbot** that runs in your terminal. You type something, it finds the best matching response, and replies.

---

## 🚀 How to Run It

You'll see this in your terminal:

```
=============================================
       Welcome to ChatBot 🤖
  Type 'help' to see what I can do.
  Type 'bye' or 'quit' to exit.
=============================================

ChatBot: Hey! I'm ChatBot — your friendly assistant. How can I help?

You: _
```

Just start typing!

---

## 💬 What Can It Talk About?

| Topic | Example Input | What it Does |
|-------|--------------|--------------|
| Greetings | `hello`, `hi`, `hey` | Welcomes you |
| Identity | `what's your name`, `who are you` | Tells you its name |
| Feelings | `how are you` | Responds in a friendly way |
| Jokes | `tell me a joke`, `something funny` | Tells a random joke |
| AI info | `what is AI`, `explain AI` | Gives a short explanation |
| Time | `what time is it` | Prints the current time |
| Date | `what's today's date` | Prints today's date |
| Help | `help`, `what can you do` | Lists all features |
| Thanks | `thank you`, `thx` | Responds politely |
| Exit | `bye`, `quit`, `exit` | Ends the conversation |

---

## 🔑 Key Functions

| Function | What it does |
|----------|-------------|
| `get_bot_reply(user_input)` | Matches input to a category and returns a reply |
| `is_exit(user_input)` | Checks if the user typed a goodbye word |
| `main()` | Runs the chat loop — keeps going until user exits |

---


## 📦 Built With

| Tool | Purpose |
|------|---------|
| `Python 3` | Core language |
| `random` | Pick a random reply from a list |
| `datetime` | Generate live time and date responses |