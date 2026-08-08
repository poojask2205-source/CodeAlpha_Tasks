import tkinter as tk
import random
import time

# Words + hints (5 only)
words = {
    "apple": "A red or green fruit",
    "banana": "A long yellow fruit",
    "grapes": "Small fruits in bunches",
    "orange": "A citrus fruit",
    "mango": "King of fruits"
}

# Colors
BG = "#0f172a"
CARD = "#1e293b"
PRIMARY = "#3b82f6"
SUCCESS = "#22c55e"
DANGER = "#ef4444"
TEXT = "#e2e8f0"
MUTED = "#94a3b8"
ACCENT = "#38bdf8"

class HangmanUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Hangman Pro 🎮")
        self.root.geometry("800x550")
        self.root.configure(bg=BG)

        self.show_login()

    def clear(self):
        for w in self.root.winfo_children():
            w.destroy()

    # -------- LOGIN --------
    def show_login(self):
        self.clear()

        card = tk.Frame(self.root, bg=CARD, padx=50, pady=40)
        card.place(relx=0.5, rely=0.5, anchor="center")

        tk.Label(card, text="🎮 Hangman",
                 font=("Segoe UI", 28, "bold"),
                 bg=CARD, fg=TEXT).pack(pady=10)

        tk.Label(card, text="Enter your name",
                 bg=CARD, fg=MUTED).pack()

        self.name_entry = tk.Entry(card, font=("Segoe UI", 14),
                                  justify="center", bg="#334155",
                                  fg="white", insertbackground="white")
        self.name_entry.pack(pady=15, ipadx=10, ipady=5)

        tk.Button(card, text="Start Game",
                  bg=PRIMARY, fg="white",
                  command=self.start_game).pack(pady=10)

    def start_game(self):
        self.player = self.name_entry.get()
        if not self.player:
            return
        self.show_game()

    # -------- GAME --------
    def show_game(self):
        self.clear()

        self.word = random.choice(list(words.keys()))
        self.hint = words[self.word]
        self.guessed = []
        self.lives = 6
        self.score = 0
        self.start_time = time.time()
        self.hint_used = False
        self.game_over = False
        self.buttons = []

        # Top bar
        top = tk.Frame(self.root, bg=BG)
        top.pack(pady=10)

        self.name_label = tk.Label(top, text=f"👤 {self.player}", bg=BG, fg=MUTED)
        self.name_label.grid(row=0, column=0, padx=15)

        self.timer_label = tk.Label(top, text="⏱️ 0s", bg=BG, fg=MUTED)
        self.timer_label.grid(row=0, column=1, padx=15)

        self.score_label = tk.Label(top, text="⭐ 0", bg=BG, fg=MUTED)
        self.score_label.grid(row=0, column=2, padx=15)

        self.lives_label = tk.Label(top, text="❤️ 6", bg=BG, fg=MUTED)
        self.lives_label.grid(row=0, column=3, padx=15)

        # Card
        card = tk.Frame(self.root, bg=CARD, padx=30, pady=25)
        card.pack(pady=10)

        self.word_label = tk.Label(card, font=("Segoe UI", 34, "bold"),
                                  bg=CARD, fg="yellow")
        self.word_label.pack(pady=15)

        self.hint_label = tk.Label(card, text="", bg=CARD, fg=ACCENT)
        self.hint_label.pack()

        self.hint_btn = tk.Button(card, text="💡 Show Hint (-1 life)",
                                  bg="#475569", fg="white",
                                  command=self.show_hint)
        self.hint_btn.pack(pady=8)

        self.result = tk.Label(card, font=("Segoe UI", 16, "bold"),
                               bg=CARD)
        self.result.pack(pady=5)

        # Keyboard
        keyboard = tk.Frame(card, bg=CARD)
        keyboard.pack(pady=10)

        for i, letter in enumerate("ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
            btn = tk.Button(keyboard, text=letter,
                            width=4, height=2,
                            bg=PRIMARY, fg="white",
                            command=lambda l=letter.lower(): self.guess(l))
            btn.grid(row=i//9, column=i%9, padx=4, pady=4)
            self.buttons.append(btn)

        self.update_display()
        self.update_timer()

    # -------- LOGIC --------
    def update_display(self):
        display = " ".join([l if l in self.guessed else "_" for l in self.word])
        self.word_label.config(text=display)
        self.lives_label.config(text=f"❤️ {self.lives}")

    def show_hint(self):
        if not self.hint_used and not self.game_over:
            self.hint_label.config(text=f"💡 {self.hint}")
            self.lives -= 1
            self.hint_used = True
            self.hint_btn.config(state="disabled")
            self.update_display()
            self.check_game()

    def guess(self, letter):
        if self.game_over or letter in self.guessed:
            return

        # while loop (requirement)
        while True:
            self.guessed.append(letter)

            if letter in self.word:
                self.score += 10
            else:
                self.lives -= 1

            break

        self.update_display()
        self.score_label.config(text=f"⭐ {self.score}")
        self.check_game()

    def check_game(self):
        if all(l in self.guessed for l in self.word):
            self.result.config(text="🎉 YOU WIN!", fg=SUCCESS)
            self.end_game()

        elif self.lives <= 0:
            self.result.config(text=f"💀 LOST! Word: {self.word}", fg=DANGER)
            self.end_game()

    def end_game(self):
        self.game_over = True
        for btn in self.buttons:
            btn.config(state="disabled")

    def update_timer(self):
        if self.game_over:
            return

        t = int(time.time() - self.start_time)
        self.timer_label.config(text=f"⏱️ {t}s")
        self.root.after(1000, self.update_timer)


# Run
root = tk.Tk()
app = HangmanUI(root)
root.mainloop()