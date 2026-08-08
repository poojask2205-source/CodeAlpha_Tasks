import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime

# ---------------- STOCK DATA ----------------

stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 150,
    "AMZN": 200,
    "MSFT": 420
}

portfolio = []
total_investment = 0


# ---------------- FUNCTIONS ----------------

def add_stock():
    global total_investment

    stock = stock_combo.get()
    quantity_text = quantity_entry.get()

    if not stock:
        messagebox.showwarning("Missing Stock", "Please select a stock.")
        return

    try:
        quantity = int(quantity_text)

        if quantity <= 0:
            messagebox.showwarning(
                "Invalid Quantity",
                "Quantity must be greater than 0."
            )
            return

    except ValueError:
        messagebox.showerror(
            "Invalid Input",
            "Please enter a valid quantity."
        )
        return

    price = stock_prices[stock]
    investment = price * quantity

    total_investment += investment

    portfolio.append({
        "stock": stock,
        "quantity": quantity,
        "price": price,
        "investment": investment
    })

    # Add to table
    portfolio_table.insert(
        "",
        "end",
        values=(
            stock,
            quantity,
            f"${price}",
            f"${investment}"
        )
    )

    total_label.config(
        text=f"${total_investment:,}"
    )

    quantity_entry.delete(0, tk.END)

    status_label.config(
        text=f"✓ {quantity} shares of {stock} added successfully"
    )


def save_portfolio():
    if not portfolio:
        messagebox.showwarning(
            "Empty Portfolio",
            "There is no investment data to save."
        )
        return

    with open("stock_investment.txt", "w") as file:

        file.write("STOCK INVESTMENT SUMMARY\n")
        file.write("========================\n\n")

        file.write(
            f"Date: {datetime.now().strftime('%d-%m-%Y %H:%M')}\n\n"
        )

        for item in portfolio:

            file.write(
                f"Stock: {item['stock']}\n"
                f"Quantity: {item['quantity']}\n"
                f"Price: ${item['price']}\n"
                f"Investment: ${item['investment']}\n"
                f"--------------------------\n"
            )

        file.write(
            f"\nTOTAL INVESTMENT: ${total_investment}\n"
        )

    messagebox.showinfo(
        "Saved",
        "Portfolio saved successfully!\n\n"
        "File: stock_investment.txt"
    )


def clear_portfolio():
    global total_investment

    if not portfolio:
        return

    answer = messagebox.askyesno(
        "Clear Portfolio",
        "Are you sure you want to clear the portfolio?"
    )

    if answer:

        portfolio.clear()
        total_investment = 0

        for item in portfolio_table.get_children():
            portfolio_table.delete(item)

        total_label.config(text="$0")

        status_label.config(
            text="Portfolio cleared successfully"
        )


def exit_app():
    answer = messagebox.askyesno(
        "Exit",
        "Do you want to exit the application?"
    )

    if answer:
        root.destroy()


# ---------------- MAIN WINDOW ----------------

root = tk.Tk()

root.title("Stock Investment Tracker")
root.geometry("1000x650")
root.minsize(900, 600)
root.configure(bg="#101827")


# ---------------- COLORS ----------------

BG = "#101827"
CARD = "#182235"
CARD2 = "#1F2B40"
WHITE = "#FFFFFF"
GRAY = "#9CA8BA"
GREEN = "#22C55E"
BLUE = "#3B82F6"
RED = "#EF4444"


# ---------------- HEADER ----------------

header = tk.Frame(
    root,
    bg=BG,
    height=90
)

header.pack(
    fill="x",
    padx=30,
    pady=(20, 5)
)

title = tk.Label(
    header,
    text="📈 Stock Investment Tracker",
    font=("Segoe UI", 24, "bold"),
    bg=BG,
    fg=WHITE
)

title.pack(side="left")

subtitle = tk.Label(
    header,
    text="Manage your stock investments easily",
    font=("Segoe UI", 11),
    bg=BG,
    fg=GRAY
)

subtitle.pack(
    side="left",
    padx=20,
    pady=(10, 0)
)


# ---------------- TOP CARDS ----------------

cards_frame = tk.Frame(
    root,
    bg=BG
)

cards_frame.pack(
    fill="x",
    padx=30,
    pady=10
)


# Total Investment Card

investment_card = tk.Frame(
    cards_frame,
    bg=CARD,
    height=120
)

investment_card.pack(
    side="left",
    fill="both",
    expand=True,
    padx=(0, 10)
)

tk.Label(
    investment_card,
    text="TOTAL INVESTMENT",
    font=("Segoe UI", 10, "bold"),
    bg=CARD,
    fg=GRAY
).pack(
    anchor="w",
    padx=20,
    pady=(15, 5)
)

total_label = tk.Label(
    investment_card,
    text="$0",
    font=("Segoe UI", 28, "bold"),
    bg=CARD,
    fg=GREEN
)

total_label.pack(
    anchor="w",
    padx=20
)


# Available Stocks Card

stocks_card = tk.Frame(
    cards_frame,
    bg=CARD,
    height=120
)

stocks_card.pack(
    side="left",
    fill="both",
    expand=True,
    padx=(10, 0)
)

tk.Label(
    stocks_card,
    text="AVAILABLE STOCKS",
    font=("Segoe UI", 10, "bold"),
    bg=CARD,
    fg=GRAY
).pack(
    anchor="w",
    padx=20,
    pady=(15, 5)
)

tk.Label(
    stocks_card,
    text="AAPL   TSLA   GOOGL   AMZN   MSFT",
    font=("Segoe UI", 14, "bold"),
    bg=CARD,
    fg=WHITE
).pack(
    anchor="w",
    padx=20
)


# ---------------- INPUT CARD ----------------

input_card = tk.Frame(
    root,
    bg=CARD,
    padx=20,
    pady=20
)

input_card.pack(
    fill="x",
    padx=30,
    pady=10
)


tk.Label(
    input_card,
    text="Add Investment",
    font=("Segoe UI", 16, "bold"),
    bg=CARD,
    fg=WHITE
).grid(
    row=0,
    column=0,
    columnspan=5,
    sticky="w",
    pady=(0, 15)
)


# Stock

tk.Label(
    input_card,
    text="Stock",
    font=("Segoe UI", 10),
    bg=CARD,
    fg=GRAY
).grid(
    row=1,
    column=0,
    sticky="w"
)


stock_combo = ttk.Combobox(
    input_card,
    values=list(stock_prices.keys()),
    state="readonly",
    width=18,
    font=("Segoe UI", 11)
)

stock_combo.grid(
    row=2,
    column=0,
    padx=(0, 20),
    pady=5
)

stock_combo.set("AAPL")


# Quantity

tk.Label(
    input_card,
    text="Quantity",
    font=("Segoe UI", 10),
    bg=CARD,
    fg=GRAY
).grid(
    row=1,
    column=1,
    sticky="w"
)


quantity_entry = tk.Entry(
    input_card,
    width=20,
    font=("Segoe UI", 11),
    bg=CARD2,
    fg=WHITE,
    insertbackground=WHITE,
    relief="flat"
)

quantity_entry.grid(
    row=2,
    column=1,
    padx=(0, 20),
    ipady=8
)


# Add Button

add_button = tk.Button(
    input_card,
    text="＋ Add Stock",
    font=("Segoe UI", 11, "bold"),
    bg=BLUE,
    fg=WHITE,
    activebackground="#2563EB",
    activeforeground=WHITE,
    relief="flat",
    cursor="hand2",
    command=add_stock
)

add_button.grid(
    row=2,
    column=2,
    padx=10,
    ipadx=15,
    ipady=6
)


# ---------------- TABLE ----------------

table_frame = tk.Frame(
    root,
    bg=CARD
)

table_frame.pack(
    fill="both",
    expand=True,
    padx=30,
    pady=10
)


tk.Label(
    table_frame,
    text="Your Portfolio",
    font=("Segoe UI", 16, "bold"),
    bg=CARD,
    fg=WHITE
).pack(
    anchor="w",
    padx=20,
    pady=15
)


columns = (
    "Stock",
    "Quantity",
    "Price",
    "Investment"
)

portfolio_table = ttk.Treeview(
    table_frame,
    columns=columns,
    show="headings",
    height=7
)


for column in columns:

    portfolio_table.heading(
        column,
        text=column
    )

    portfolio_table.column(
        column,
        anchor="center",
        width=180
    )


portfolio_table.pack(
    fill="both",
    expand=True,
    padx=20,
    pady=(0, 15)
)


# ---------------- BUTTONS ----------------

button_frame = tk.Frame(
    root,
    bg=BG
)

button_frame.pack(
    fill="x",
    padx=30,
    pady=(0, 5)
)


save_button = tk.Button(
    button_frame,
    text="💾 Save Portfolio",
    font=("Segoe UI", 10, "bold"),
    bg=GREEN,
    fg=WHITE,
    relief="flat",
    cursor="hand2",
    command=save_portfolio
)

save_button.pack(
    side="left",
    ipadx=15,
    ipady=7
)


clear_button = tk.Button(
    button_frame,
    text="🗑 Clear",
    font=("Segoe UI", 10, "bold"),
    bg=RED,
    fg=WHITE,
    relief="flat",
    cursor="hand2",
    command=clear_portfolio
)

clear_button.pack(
    side="left",
    padx=10,
    ipadx=15,
    ipady=7
)


exit_button = tk.Button(
    button_frame,
    text="✕ Exit",
    font=("Segoe UI", 10, "bold"),
    bg=CARD2,
    fg=WHITE,
    relief="flat",
    cursor="hand2",
    command=exit_app
)

exit_button.pack(
    side="right",
    ipadx=20,
    ipady=7
)


# ---------------- STATUS ----------------

status_label = tk.Label(
    root,
    text="Ready to add your first investment",
    font=("Segoe UI", 9),
    bg=BG,
    fg=GRAY
)

status_label.pack(
    anchor="w",
    padx=30,
    pady=(0, 10)
)


# ---------------- STYLE ----------------

style = ttk.Style()

style.theme_use("clam")

style.configure(
    "Treeview",
    background=CARD2,
    foreground=WHITE,
    fieldbackground=CARD2,
    rowheight=35,
    font=("Segoe UI", 10)
)

style.configure(
    "Treeview.Heading",
    background="#26344D",
    foreground=WHITE,
    font=("Segoe UI", 10, "bold")
)

style.map(
    "Treeview",
    background=[("selected", BLUE)]
)


# ---------------- RUN APP ----------------

root.mainloop()