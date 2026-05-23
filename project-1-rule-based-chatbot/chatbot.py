
help_message = """
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
"""
responses = {
    # 1. Greetings
    "hello": "Hi there! How can I help you today?",
    "hi": "Hello! Nice to meet you.",
    "hey": "Hey! What would you like to ask?",
    "good morning": "Good morning! I hope you have a productive day.",
    "good afternoon": "Good afternoon! How can I assist you?",
    "good evening": "Good evening! What would you like to learn today?",

    # 2. Bot identity
    "what is your name": "I am a rule-based AI chatbot created for the DecodeLabs AI internship Task 1.",
    "who are you": "I am a simple chatbot that responds using predefined rules.",
    "what can you do": "I can answer basic questions about AI, machine learning, Python, and this internship project.",
    "are you ai": "Yes, I am a basic rule-based AI system. I do not learn from data yet, but I follow programmed rules.",
    "who created you": "Mahmoud Yassin created me as part of the DecodeLabs Artificial Intelligence Project 1 task.",

    # 3. AI basics
    "what is ai": "AI stands for Artificial Intelligence. It allows machines to perform tasks that usually require human intelligence.",
    "why is ai important": "AI is important because it can help automate tasks, analyze data, and support decision-making.",
    "give me an example of ai": "Examples of AI include chatbots, recommendation systems, self-driving cars, and voice assistants.",
    "what are ai applications": "AI is used in healthcare, finance, education, transportation, cybersecurity, and customer service.",
    "is ai the future": "AI is expected to play a major role in the future because it can improve efficiency and solve complex problems.",

    # 4. Machine learning basics
    "what is machine learning": "Machine learning is a branch of AI where computers learn patterns from data.",
    "what is supervised learning": "Supervised learning is when a model learns from labeled data, meaning the correct answers are already provided.",
    "what is unsupervised learning": "Unsupervised learning is when a model looks for patterns in data without labeled answers.",
    "what is classification": "Classification is a machine learning task where data is assigned to categories or classes.",
    "what is regression": "Regression is a machine learning task used to predict continuous numerical values.",
    "what is training data": "Training data is the data used to teach a machine learning model.",
    "what is testing data": "Testing data is used to check how well a trained model performs on new information.",
    "what is a dataset": "A dataset is a collection of data used for analysis or machine learning.",

    # 5. Python basics
    "what is python": "Python is a popular programming language used in AI, web development, automation, and data science.",
    "why use python for ai": "Python is widely used for AI because it is simple, readable, and has powerful libraries like scikit-learn and TensorFlow.",
    "what is a variable": "A variable is a name used to store a value in a program.",
    "what is a loop": "A loop is used to repeat a block of code multiple times.",
    "what is while loop": "A while loop keeps running as long as its condition is true.",
    "what is if else": "If-else logic allows a program to make decisions based on conditions.",
    "what is a dictionary": "A dictionary stores data in key-value pairs, like a question linked to its answer.",
    "what is input function": "The input function allows the user to type something into the program.",
    "what is print function": "The print function displays output on the screen.",

    # 6. Chatbot project questions
    "what is this project about": "This project is about building a rule-based chatbot using Python.",
    "what is a rule based chatbot": "A rule-based chatbot responds using predefined rules written by Mahmoud Yassin.",
    "does this chatbot learn": "No, this chatbot does not learn from data. It only follows the rules programmed into it.",
    "how does this chatbot work": "The chatbot takes user input, cleans it, checks it against predefined responses, and prints the matching answer.",
    "what is fallback response": "A fallback response is used when the chatbot does not understand the user's input.",
    "why do we use lower": "We use lower() to convert user input to lowercase, so 'Hello' and 'hello' are treated the same.",
    "why do we use strip": "We use strip() to remove extra spaces from the beginning and end of the user's input.",
    "why do we use break": "We use break to stop the continuous loop when the user wants to exit.",
    "why use a dictionary": "A dictionary makes the chatbot cleaner and easier to expand because responses are stored in one place.",

    # 7. Internship-related
    "what is decodelabs": "DecodeLabs is the organization providing this AI industrial training project.",
    "what is project 1": "Project 1 is about creating a rule-based AI chatbot.",
    "what skills does project 1 teach": "Project 1 teaches control flow, decision-making logic, loops, dictionaries, and basic AI concepts.",
    "what should i submit": "You should submit a working Python chatbot file with predefined responses, a loop, exit commands, and fallback handling.",
    "is this project beginner friendly": "Yes, this project is beginner friendly because it focuses on basic Python logic.",

    # 8. Motivation / help
    "i need help": "Of course. You can ask me about AI, Python, or this chatbot project.",
    "i am confused": "That is normal when learning. Try breaking the problem into small steps.",
    "give me a tip": "Test your code after every small change. This makes debugging much easier.",
    "how can i improve": "You can improve by adding more intents, better responses, and clearer code comments.",
    "thank you": "You are welcome! Keep learning and building.",
    "thanks": "You're welcome! Happy to help.",

    # 9. Exit
    "bye": "Goodbye! Have a great day.",
    "goodbye": "Goodbye! Keep practicing.",
    "see you": "See you later!",
    "exit": "Goodbye! The chatbot is now closing.",
    "quit": "Goodbye! The chatbot is now closing."
}

print("\n""Mahmoud Yassin's DecodeLabs Rule-Based AI Chatbot")
print("Type 'help' to see available commands.")
print("Type 'exit', 'bye', 'goodbye', or 'see you' to stop the chatbot.""\n\n")

while True:
    user_input = input("You: ")

    clean_input = user_input.lower().strip()

    if clean_input in ["exit", "bye", "goodbye", "see you", "quit"]:
        print("Bot:", responses[clean_input])
        break

    reply = responses.get(
        clean_input,
        "I do not understand that yet, but I am still learning. Try asking about AI, Python, or this project."
    )

    print("Bot:", reply)
    