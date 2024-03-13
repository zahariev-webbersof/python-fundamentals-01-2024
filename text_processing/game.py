import tkinter as tk
from tkinter import messagebox
import random


class HangmanGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Hangman Game")

        self.words = ["python", "hello"]
        self.secret_word = random.choice(self.words)
        self.guesses_left = 6
        self.guesses = set()

        self.canvas = tk.Canvas(master, width=400, height=400)
        self.canvas.pack()

        self.word_display = tk.Label(master, text=" ".join("_" for _ in self.secret_word), font=("Helvetica", 20))
        self.word_display.pack()

        self.label = tk.Label(master, text="Guess a letter:")
        self.label.pack()

        self.entry = tk.Entry(master)
        self.entry.pack()

        self.button = tk.Button(master, text="Guess", command=self.guess_letter)
        self.button.pack()

        self.draw_hangman()

    def draw_hangman(self):
        self.canvas.create_line(100, 350, 300, 350, width=3)  # Base
        self.canvas.create_line(200, 350, 200, 100, width=3)  # Pole
        self.canvas.create_line(200, 100, 250, 100, width=3)  # Beam
        self.canvas.create_line(250, 100, 250, 150, width=3)  # Rope

    def guess_letter(self):
        guessed_letter = self.entry.get().lower()
        if len(guessed_letter) != 1 or not guessed_letter.isalpha():
            messagebox.showerror("Error", "Please enter a single alphabetical character!")
        elif guessed_letter in self.guesses:
            messagebox.showinfo("Info", "You already guessed that letter!")
        else:
            self.guesses.add(guessed_letter)
            if guessed_letter in self.secret_word:
                self.update_word_display()
            else:
                self.guesses_left -= 1
                if self.guesses_left == 0:
                    messagebox.showinfo("Game Over", f"You ran out of guesses! The word was {self.secret_word}.")
                    self.master.quit()
                else:
                    messagebox.showinfo("Info", f"Wrong guess! You have {self.guesses_left} guesses left.")
                    self.draw_hangman()

    def update_word_display(self):
        word = ""
        for letter in self.secret_word:
            if letter in self.guesses:
                word += letter
            else:
                word += "_"
        self.word_display.config(text=word)
        if "_" not in word:
            messagebox.showinfo("Congratulations", f"Congratulations! You guessed the word: {self.secret_word}.")
            self.master.quit()


def main():
    root = tk.Tk()
    game = HangmanGame(root)
    root.mainloop()


if __name__ == "__main__":
    main()