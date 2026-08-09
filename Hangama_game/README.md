# TASK 1 : Hangman Game 🎮

## Description

This project is a simple **Hangman Game** developed using Python and Tkinter. The player enters their name and tries to guess a randomly selected word one letter at a time.

The game contains **5 predefined words**, each with a hint. The player gets **6 lives** and loses one life for each incorrect guess. A hint can also be used, but it costs one life.

The game has a simple desktop interface with a keyboard, score counter, lives counter, timer, and hint option.

## Features

* 🎮 Simple desktop-based Hangman game
* 👤 Player name input
* 📝 5 predefined words
* 💡 Hint system
* ❤️ Maximum 6 incorrect guesses
* ⭐ Score system
* ⏱️ Game timer
* 🔤 On-screen keyboard
* 🎉 Win and lose messages
* 🚫 Keyboard buttons are disabled after the game ends

## Technologies Used

* **Python**
* **Tkinter** – for the graphical user interface
* **Random** – to select a word randomly
* **Time** – to track the game duration

## Concepts Used

* Lists and dictionaries
* Strings
* `if-else` conditions
* `while` loop
* Functions
* Classes and objects
* Random word selection
* GUI programming

## How the Game Works

1. Enter your name.
2. Click **Start Game**.
3. A random word is selected from the predefined word list.
4. Guess the letters using the on-screen keyboard.
5. Correct guesses increase the score.
6. Incorrect guesses reduce the number of lives.
7. You can use a hint once, but it costs one life.
8. Guess the complete word before losing all 6 lives to win.

## How to Run

Make sure Python is installed on your computer.

Run the program using:

```bash
python hangman.py
```

The Hangman desktop window will open.

## Word List

The game uses these 5 predefined words:

* Apple
* Banana
* Grapes
* Orange
* Mango

## Result

The game displays **"YOU WIN!"** when the player guesses the word correctly. If all 6 lives are used, it displays **"LOST!"** along with the correct word.
