# TASK 3 : Simple Basic Chatbot 🤖

## Description

This project is a simple **rule-based chatbot** developed using Python and CustomTkinter. The chatbot interacts with the user through a desktop graphical interface and provides predefined responses based on the user's input.

The chatbot can respond to greetings, basic questions, date and time requests, and goodbye messages. It also includes quick-question buttons, a new chat option, clear chat option, and light/dark theme support.

## Features

* 🤖 Simple rule-based chatbot
* 💬 User and chatbot message display
* 👋 Greeting responses
* 😊 "How are you?" response
* 🧑‍💻 Chatbot name and purpose information
* 💡 Displays available chatbot features
* ⏰ Shows the current time
* 📅 Shows the current date
* 🙏 Responds to "Thank you"
* 🌅 Good morning, afternoon, and evening responses
* 👋 Goodbye response
* ⚡ Quick question buttons
* 🆕 New Chat option
* 🧹 Clear Chat option
* 🌙 Light and dark theme
* ⌨️ Send messages using the Enter key
* 🖥️ User-friendly desktop interface

## How It Works

The chatbot uses predefined rules to understand the user's message.

For example:

```text
User: Hello
Bot: Hello! 👋 It's nice to meet you. How can I help you?

User: How are you?
Bot: I'm doing great! 😊 Thanks for asking.

User: What is your name?
Bot: My name is SmartBot 🤖. I'm a simple rule-based chatbot.

User: Bye
Bot: Goodbye! 👋 Have a wonderful day!
```

The chatbot converts the user's input to lowercase and removes extra spaces before checking the message against predefined conditions.

## Supported Questions

The chatbot can respond to questions such as:

* `Hello`
* `Hi`
* `How are you?`
* `What is your name?`
* `Who are you?`
* `What can you do?`
* `What is the time?`
* `What is today's date?`
* `Thanks`
* `Good morning`
* `Good afternoon`
* `Good evening`
* `Bye`
* `Goodbye`

If the chatbot does not recognize the input, it displays a list of questions that the user can try.

## Technologies Used

* **Python**
* **CustomTkinter** – for creating the modern desktop GUI
* **datetime** – for displaying the current date and time

## Key Concepts Used

* `if-elif-else` conditions
* Functions
* Loops
* Strings
* Lists
* Dictionaries
* User input and output
* GUI programming
* Event handling
* Date and time handling

## Main Components

### 1. Chatbot Response Function

The `chatbot_response()` function contains the rules and predefined responses. It checks the user's message and returns the appropriate response.

### 2. SmartBot Class

The `SmartBot` class creates the main desktop application and manages the chatbot interface.

### 3. Quick Questions

The sidebar provides quick buttons for common questions so users can interact with the chatbot without typing.

### 4. Chat Management

The application provides **New Chat** and **Clear Chat** options to manage conversations.

### 5. Theme

Users can switch between **dark mode and light mode** using the Settings button.

## Installation

Install the required CustomTkinter library using:

```bash
pip install customtkinter
```

## How to Run

Save the Python program as:

```text
chatbot.py
```

Run the application using:

```bash
python chatbot.py
```

The SmartBot desktop application will open.



## Result

The Simple Basic Chatbot successfully provides a simple desktop-based conversation system using predefined rules. It demonstrates the use of Python conditions, functions, loops, input/output, and GUI programming to create an interactive chatbot.
