# Project 1: Rule-Based AI Chatbot

## Overview

This project is a simple **rule-based AI chatbot** built using Python for the **DecodeLabs Artificial Intelligence Internship**.

The chatbot responds to predefined user inputs using dictionary-based rule matching. It does not use machine learning yet. Instead, it follows manually written rules to simulate a basic AI conversation.

This project represents the foundation stage of the AI track because it focuses on control flow, decision-making logic, input handling, and basic chatbot behavior.

---

## Project Goal

The goal of this project is to create a chatbot that can:

- Accept user input
- Clean and process the input
- Match predefined user commands with predefined responses
- Respond with suitable answers
- Continue running in a loop
- Exit when the user enters an exit command
- Show a help menu with available commands
- Provide a fallback response for unknown inputs

---

## Features

This chatbot includes:

- Greeting responses such as `hello`, `hi`, and `hey`
- Basic AI-related responses
- Basic machine learning explanations
- Basic Python programming explanations
- Internship/project-related responses
- A `help` command that shows available commands
- Exit commands such as `exit`, `bye`, `goodbye`, and `see you`
- Input cleaning using `lower()` and `strip()`
- Dictionary-based response matching
- Continuous conversation using a `while` loop
- Fallback response for unknown inputs

---

## Concepts Used

This project demonstrates the following programming and AI concepts:

- Python dictionaries
- User input using `input()`
- Output using `print()`
- String methods such as `lower()` and `strip()`
- Conditional statements
- `while` loops
- `break` statements
- Rule-based AI logic
- Basic chatbot design
- Intent-response matching
- Fallback handling

---

## How the Chatbot Works

```text
1. The chatbot starts and displays an introduction message.
2. The user types a message.
3. The program cleans the input using lower() and strip().
4. The chatbot checks whether the input is an exit command.
5. If it is an exit command, the chatbot prints a goodbye message and stops.
6. If it is not an exit command, the chatbot searches for the input in the responses dictionary.
7. If a matching command exists, the chatbot prints the matching response.
8. If no matching command exists, the chatbot prints a fallback message.
9. The loop continues until the user exits.
```

---

## File Structure

```text
project-1-rule-based-chatbot/
│
├── chatbot.py
└── README.md
```

---

## How to Run

From the root repository folder, run:

```bash
python project-1-rule-based-chatbot/chatbot.py
```

On Windows, if `python` does not work, run:

```bash
py project-1-rule-based-chatbot/chatbot.py
```

You can also open the project folder and run:

```bash
python chatbot.py
```

or:

```bash
py chatbot.py
```

---

## Example Usage

```text
DecodeLabs Rule-Based AI Chatbot
Type 'help' to see available commands.
Type 'exit', 'bye', 'goodbye', or 'see you' to stop the chatbot.
--------------------------------------------------

You: hello
Bot: Hi there! How can I help you today?

You: what is ai
Bot: AI stands for Artificial Intelligence. It allows machines to perform tasks that usually require human intelligence.

You: help
Bot:
Available Commands:

1. Greetings:
   - hello
   - hi
   - hey
   - good morning
   - good afternoon
   - good evening

2. Bot Information:
   - what is your name
   - who are you
   - what can you do
   - are you ai

3. AI Basics:
   - what is ai
   - why is ai important
   - give me an example of ai
   - what are ai applications

4. Machine Learning:
   - what is machine learning
   - what is supervised learning
   - what is classification
   - what is a dataset

5. Python Basics:
   - what is python
   - what is a loop
   - what is if else
   - what is a dictionary

6. Project Help:
   - what is this project about
   - how does this chatbot work
   - why do we use lower
   - why do we use strip
   - why do we use break

7. Exit Commands:
   - exit
   - bye
   - goodbye
   - see you

You: random question
Bot: I do not understand that yet. Type 'help' to see the commands I can respond to.

You: exit
Bot: Goodbye! The chatbot is now closing.
```

---

## Available Commands

Some example commands the chatbot can understand:

```text
hello
hi
hey
good morning
good afternoon
good evening
what is your name
who are you
what can you do
are you ai
what is ai
why is ai important
give me an example of ai
what are ai applications
what is machine learning
what is supervised learning
what is classification
what is a dataset
what is python
what is a loop
what is if else
what is a dictionary
what is this project about
how does this chatbot work
why do we use lower
why do we use strip
why do we use break
help
commands
show commands
exit
bye
goodbye
see you
```

---

## Main Code Logic

The chatbot stores predefined responses in a dictionary:

```python
responses = {
    "hello": "Hi there! How can I help you today?",
    "what is ai": "AI stands for Artificial Intelligence.",
    "bye": "Goodbye! Have a great day."
}
```

The user input is cleaned before matching:

```python
clean_input = user_input.lower().strip()
```

This allows inputs like:

```text
Hello
   hello
HELLO
```

to be treated as:

```text
hello
```

The chatbot checks for exit commands:

```python
if clean_input in ["exit", "bye", "goodbye", "see you"]:
    print("Bot:", responses[clean_input])
    break
```

The chatbot searches for a matching response:

```python
reply = responses.get(
    clean_input,
    "I do not understand that yet. Type 'help' to see the commands I can respond to."
)
```

If the input exists in the dictionary, the chatbot returns the matching response. If it does not exist, it returns the fallback response.

---

## Why This Is Rule-Based AI

This chatbot is called rule-based because it follows predefined rules written by the programmer.

It does not train on data or learn from previous conversations. Instead, it checks whether the user's input matches a known command and then returns the matching response.

Example:

```text
User input: what is ai
Matched rule: "what is ai"
Bot response: AI stands for Artificial Intelligence.
```

---

## Limitations

This chatbot has some limitations:

- It only understands exact or predefined commands.
- It does not understand complex sentences unless they are added manually.
- It does not learn from user conversations.
- It does not use natural language processing or machine learning.
- It cannot generate new answers like advanced AI models.

These limitations are expected because this project focuses on foundational rule-based AI logic.

---

## Possible Improvements

Future improvements could include:

- Adding more commands and responses
- Supporting multiple versions of the same question
- Using keyword matching instead of exact matching
- Adding simple natural language processing
- Saving conversation history
- Creating a graphical user interface
- Connecting the chatbot to a web app
- Upgrading it later into a machine-learning-based chatbot

---

## Project Status

Completed.

---

## Author

**Mahmoud Yassin**

Created as part of the DecodeLabs Artificial Intelligence Internship.
