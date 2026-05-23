# Project 1: Rule-Based AI Chatbot

## Overview

This project is a simple **rule-based AI chatbot** built using Python for the DecodeLabs Artificial Intelligence Internship.

The chatbot responds to predefined user inputs using dictionary-based rule matching. It does not use machine learning yet. Instead, it follows manually written rules to simulate a basic AI conversation.

---

## Project Goal

The goal of this project is to create a chatbot that can:

- Accept user input
- Understand predefined commands
- Respond with suitable answers
- Continue running in a loop
- Exit when the user enters an exit command
- Show a help menu with available commands
- Provide a fallback response for unknown inputs

---

## Features

- Handles greetings such as `hello`, `hi`, and `hey`
- Answers basic AI-related questions
- Answers basic Python-related questions
- Explains simple machine learning concepts
- Includes internship/project-related responses
- Supports a `help` command
- Supports exit commands such as `exit`, `bye`, `goodbye`, and `see you`
- Uses clean and organized Python code
- Uses a fallback response when the chatbot does not understand the input

---

## Concepts Used

This project demonstrates the following programming concepts:

- Python dictionaries
- User input using `input()`
- Output using `print()`
- String methods such as `lower()` and `strip()`
- Conditional statements
- `while` loops
- `break` statements
- Rule-based AI logic
- Basic chatbot design

---

## How the Chatbot Works

The chatbot follows this process:

```text
1. The user enters a message.
2. The program cleans the input using lower() and strip().
3. The chatbot checks if the input is an exit command.
4. If not, it searches for the input inside the responses dictionary.
5. If a matching response exists, the chatbot prints it.
6. If no matching response exists, the chatbot prints a fallback message.
7. The loop continues until the user exits.ddd
