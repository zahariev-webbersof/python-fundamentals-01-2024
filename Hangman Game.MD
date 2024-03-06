# Hangman Game 🐍

### ✳️ Description:
In this task, you will extend the Hangman game to make it more interactive and engaging for players. You will implement several new features, including the ability for players to choose a category for the secret word, a button to select a new word from the chosen category, and a graphical representation of the hangman that updates with each incorrect guess. Additionally, you will add a scoring system where players earn points for each correct guess and lose points for each incorrect guess.

### ✳️ Requirements:

1. Category Selection: Implement functionality to allow players to choose a category for the secret word. You should provide at least three categories, such as animals, countries, and fruits. Each category should have a set of words associated with it.
2. New Word Button: Add a button that allows players to select a new word from the chosen category. When the button is clicked, a new word should be randomly selected from the category, and the game state should be reset.
3. Gaphical Hangman: Implement a graphical representation of the hangman that updates with each incorrect guess. You can use simple shapes (lines, circles) to represent the hangman's body parts, and draw additional parts with each incorrect guess.
4. Category Feedback: Provide feedback to players about the category they are playing with. Display the chosen category on the game interface to inform players about the theme of the word they are trying to guess.
5. Scoring System: Implement a scoring system where players earn points for each correct guess and lose points for each incorrect guess. You can assign a point value to each correct guess and deduct points for incorrect guesses. Display the player's score on the game interface.

### ✳️ Comments in Code:
1. Use comments to explain the purpose of each method and the overall flow of the game.
2. Use descriptive variable names and comments within the methods to clarify the logic.

➡️ Here's the incomplete code for students to repair and refactor:
```python
import tkinter as tk
from tkinter import messagebox
import random

class HangmanGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Hangman Game")

        self.categories = {
            "Animals": ["cat", "dog", "elephant", "giraffe", "monkey"],
            "Countries": ["india", "japan", "brazil", "australia", "canada"],
            "Fruits": ["apple", "banana", "orange", "grape", "kiwi"]
        }
        self.current_category = ""
        self.secret_word = ""
        self.guesses_left = 6
        self.guesses = set()

        self.canvas = tk.Canvas(master, width=400, height=400)
        self.canvas.pack()

        self.category_label = tk.Label(master, text="Category: ")
        self.category_label.pack()

        self.word_display = tk.Label(master, text="", font=("Helvetica", 20))
        self.word_display.pack()

        self.label = tk.Label(master, text="Guess a letter:")
        self.label.pack()

        self.entry = tk.Entry(master)
        self.entry.pack()

        self.guess_button = tk.Button(master, text="Guess", command=self.guess_letter)
        self.guess_button.pack()

        self.new_word_button = tk.Button(master, text="New Word", command=self.choose_new_word)
        self.new_word_button.pack()

        self.choose_category()

    def choose_category(self):
        # This method should allow the player to choose a category and set the current_category attribute

    def choose_new_word(self):
        # This method should choose a new word from the selected category and reset the game attributes

    def draw_hangman(self):
        # This method should draw the hangman based on the number of incorrect guesses

    def guess_letter(self):
        # This method should handle the player's guess and update the game state accordingly

    def update_word_display(self):
        # This method should update the displayed word with the guessed letters

def main():
    root = tk.Tk()
    game = HangmanGame(root)
    root.mainloop()

if __name__ == "__main__":
    main()


```
