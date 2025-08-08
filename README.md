# Simple Rule-Based Chatbot

## What is this project?

This is a basic chatbot that responds to simple user messages with predefined replies. It's a beginner-friendly Python project that demonstrates basic programming concepts like functions, loops, and conditional statements.

## How does it work?

The chatbot works by:
1. Taking user input
2. Converting it to lowercase for easier matching
3. Checking if the input matches any predefined patterns
4. Returning the appropriate response
5. Continuing the conversation until the user says "bye"

## What can the chatbot do?

The chatbot can respond to these messages:
- **"hello"** → "Hi!"
- **"how are you"** → "I'm fine, thanks!"
- **"bye"** → "Goodbye!" (and exits)
- **"what is your name"** → "I'm a simple chatbot!"
- **"help"** → Shows available commands

For any other input, it will say it doesn't understand and suggest using "help".

## Files in this project:

- **chatbot.py** - Main chatbot program
- **run_chatbot.py** - Easy way to run the chatbot
- **README.md** - This explanation file

## How to run the chatbot:

### Method 1 (Easy):
1. Double-click on `run_chatbot.py`
2. The chatbot will start automatically

### Method 2 (Command line):
1. Open terminal/command prompt
2. Navigate to this folder
3. Type: `python chatbot.py`
4. Press Enter

### Method 3 (Alternative):
1. Open terminal/command prompt
2. Navigate to this folder
3. Type: `python run_chatbot.py`
4. Press Enter

## How to use the chatbot:

1. When the program starts, you'll see a welcome message
2. Type your message and press Enter
3. The bot will respond
4. Keep chatting!
5. Type "bye" when you want to stop

## Example conversation:

```
Welcome to the Simple Chatbot!
Type 'bye' to exit the chat
Type 'help' to see available commands
----------------------------------------
You: hello
Bot: Hi!
You: how are you
Bot: I'm fine, thanks!
You: help
Bot: You can say: hello, how are you, bye, what is your name, or help
You: bye
Bot: Goodbye!
```

## Key programming concepts used:

- **Functions**: `get_chatbot_response()` and `main()`
- **Loops**: `while True` for continuous conversation
- **Conditional statements**: `if-elif-else` for response matching
- **Input/Output**: Getting user input and displaying responses
- **String manipulation**: Converting to lowercase for matching

## Requirements:

- Python 3.x installed on your computer
- No additional libraries needed (uses only built-in Python features)

## Note for beginners:

This is a simple rule-based chatbot. It doesn't use artificial intelligence - it just matches exact phrases and gives back pre-written responses. It's a great starting project to learn basic Python programming!
