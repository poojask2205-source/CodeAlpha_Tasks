import customtkinter as ctk
from datetime import datetime


# =========================================================
# APPLICATION SETTINGS
# =========================================================

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")


# =========================================================
# CHATBOT RULES
# =========================================================

def chatbot_response(message):

    message = message.lower().strip()

    # Greeting
    if message in ["hello", "hi", "hey", "hii"]:
        return "Hello! 👋 It's nice to meet you. How can I help you?"

    # How are you
    elif message in ["how are you", "how are you?"]:
        return "I'm doing great! 😊 Thanks for asking."

    # Name
    elif message in ["what is your name", "what's your name",
                     "who are you"]:
        return "My name is SmartBot 🤖. I'm a simple rule-based chatbot."

    # Purpose
    elif message in ["what can you do", "help", "features"]:
        return (
            "I can have simple conversations using predefined rules. "
            "I can greet you, tell you the date and time, "
            "and answer some basic questions."
        )

    # Time
    elif message in ["time", "what is the time", "current time"]:
        current_time = datetime.now().strftime("%I:%M %p")
        return f"The current time is {current_time} ⏰"

    # Date
    elif message in ["date", "today", "what is today's date"]:
        current_date = datetime.now().strftime("%d %B %Y")
        return f"Today's date is {current_date} 📅"

    # Thank you
    elif message in ["thanks", "thank you"]:
        return "You're welcome! 😊"

    # Good morning
    elif message == "good morning":
        return "Good morning! ☀️ I hope you have a great day."

    # Good afternoon
    elif message == "good afternoon":
        return "Good afternoon! 🌤️ How can I help you?"

    # Good evening
    elif message == "good evening":
        return "Good evening! 🌆 What would you like to talk about?"

    # Goodbye
    elif message in ["bye", "goodbye", "see you", "exit"]:
        return "Goodbye! 👋 Have a wonderful day!"

    # Unknown question
    else:
        return (
            "I'm still learning! 🤔\n\n"
            "Try asking me:\n"
            "• Hello\n"
            "• How are you?\n"
            "• What is your name?\n"
            "• What can you do?\n"
            "• What is the time?\n"
            "• What is today's date?\n"
            "• Bye"
        )


# =========================================================
# MAIN APPLICATION
# =========================================================

class SmartBot(ctk.CTk):

    def __init__(self):

        super().__init__()

        # Window
        self.title("SmartBot - Rule Based Chatbot")
        self.geometry("1100x700")
        self.minsize(900, 600)

        # Main grid
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # Create interface
        self.create_sidebar()
        self.create_chat_area()

        # Welcome message
        self.add_bot_message(
            "Hello! 👋\n\n"
            "I'm SmartBot, your simple rule-based assistant.\n\n"
            "Choose a quick question below or type your own message."
        )


    # =====================================================
    # SIDEBAR
    # =====================================================

    def create_sidebar(self):

        self.sidebar = ctk.CTkFrame(
            self,
            width=250,
            corner_radius=0
        )

        self.sidebar.grid(
            row=0,
            column=0,
            sticky="nsew"
        )

        self.sidebar.grid_propagate(False)

        # Logo
        self.logo = ctk.CTkLabel(
            self.sidebar,
            text="🤖  SmartBot",
            font=ctk.CTkFont(
                size=25,
                weight="bold"
            )
        )

        self.logo.pack(
            pady=(35, 5)
        )

        # Status
        self.status = ctk.CTkLabel(
            self.sidebar,
            text="●  Online",
            text_color="#4CAF50",
            font=ctk.CTkFont(size=13)
        )

        self.status.pack(
            pady=(0, 30)
        )

        # New Chat
        self.new_chat_button = ctk.CTkButton(
            self.sidebar,
            text="+   New Chat",
            height=45,
            corner_radius=10,
            font=ctk.CTkFont(size=14),
            command=self.new_chat
        )

        self.new_chat_button.pack(
            padx=25,
            fill="x"
        )

        # Section title
        self.quick_title = ctk.CTkLabel(
            self.sidebar,
            text="QUICK QUESTIONS",
            font=ctk.CTkFont(
                size=11,
                weight="bold"
            ),
            text_color="gray"
        )

        self.quick_title.pack(
            anchor="w",
            padx=25,
            pady=(35, 15)
        )

        # Quick questions
        questions = [
            "👋  Say Hello",
            "😊  How are you?",
            "🤖  Who are you?",
            "💡  What can you do?",
            "⏰  Tell me the time",
            "📅  Today's date"
        ]

        for question in questions:

            button = ctk.CTkButton(
                self.sidebar,
                text=question,
                height=38,
                anchor="w",
                fg_color="transparent",
                hover_color=("#DCEBFF", "#263B55"),
                command=lambda q=question: self.quick_question(q)
            )

            button.pack(
                padx=15,
                pady=2,
                fill="x"
            )

        # Bottom settings
        self.settings = ctk.CTkButton(
            self.sidebar,
            text="⚙  Settings",
            height=40,
            fg_color="transparent",
            anchor="w",
            command=self.toggle_theme
        )

        self.settings.pack(
            side="bottom",
            padx=15,
            pady=20,
            fill="x"
        )


    # =====================================================
    # CHAT AREA
    # =====================================================

    def create_chat_area(self):

        self.chat_area = ctk.CTkFrame(
            self,
            corner_radius=0,
            fg_color=("white", "#111827")
        )

        self.chat_area.grid(
            row=0,
            column=1,
            sticky="nsew"
        )

        self.chat_area.grid_columnconfigure(0, weight=1)
        self.chat_area.grid_rowconfigure(1, weight=1)

        # Header
        self.chat_header = ctk.CTkFrame(
            self.chat_area,
            height=75,
            corner_radius=0,
            fg_color=("white", "#111827")
        )

        self.chat_header.grid(
            row=0,
            column=0,
            sticky="ew"
        )

        self.chat_header.grid_columnconfigure(0, weight=1)

        self.bot_title = ctk.CTkLabel(
            self.chat_header,
            text="SmartBot 🤖",
            font=ctk.CTkFont(
                size=20,
                weight="bold"
            )
        )

        self.bot_title.grid(
            row=0,
            column=0,
            sticky="w",
            padx=30,
            pady=(15, 0)
        )

        self.bot_subtitle = ctk.CTkLabel(
            self.chat_header,
            text="Rule-based assistant • Always available",
            text_color="gray",
            font=ctk.CTkFont(size=11)
        )

        self.bot_subtitle.grid(
            row=1,
            column=0,
            sticky="w",
            padx=30
        )

        # Clear button
        self.clear_button = ctk.CTkButton(
            self.chat_header,
            text="Clear",
            width=80,
            height=32,
            fg_color="transparent",
            border_width=1,
            command=self.clear_chat
        )

        self.clear_button.grid(
            row=0,
            column=1,
            rowspan=2,
            padx=25
        )

        # Messages area
        self.messages = ctk.CTkScrollableFrame(
            self.chat_area,
            corner_radius=0,
            fg_color=("white", "#111827")
        )

        self.messages.grid(
            row=1,
            column=0,
            sticky="nsew",
            padx=20,
            pady=10
        )

        self.messages.grid_columnconfigure(0, weight=1)

        # Input section
        self.input_frame = ctk.CTkFrame(
            self.chat_area,
            height=80,
            fg_color=("white", "#111827")
        )

        self.input_frame.grid(
            row=2,
            column=0,
            sticky="ew",
            padx=20,
            pady=(5, 20)
        )

        self.input_frame.grid_columnconfigure(0, weight=1)

        # Input box
        self.message_entry = ctk.CTkEntry(
            self.input_frame,
            height=50,
            placeholder_text="Type your message here...",
            font=ctk.CTkFont(size=14),
            corner_radius=15
        )

        self.message_entry.grid(
            row=0,
            column=0,
            sticky="ew",
            padx=(5, 10)
        )

        # Send button
        self.send_button = ctk.CTkButton(
            self.input_frame,
            text="Send  ➤",
            width=110,
            height=50,
            corner_radius=15,
            font=ctk.CTkFont(
                size=14,
                weight="bold"
            ),
            command=self.send_message
        )

        self.send_button.grid(
            row=0,
            column=1
        )

        # Enter key
        self.message_entry.bind(
            "<Return>",
            lambda event: self.send_message()
        )


    # =====================================================
    # ADD USER MESSAGE
    # =====================================================

    def add_user_message(self, message):

        frame = ctk.CTkFrame(
            self.messages,
            fg_color="#2563EB",
            corner_radius=15
        )

        frame.grid(
            row=self.messages.grid_size()[1],
            column=0,
            sticky="e",
            padx=(150, 10),
            pady=8
        )

        label = ctk.CTkLabel(
            frame,
            text=message,
            text_color="white",
            font=ctk.CTkFont(size=13),
            wraplength=450,
            justify="left"
        )

        label.pack(
            padx=15,
            pady=10
        )


    # =====================================================
    # ADD BOT MESSAGE
    # =====================================================

    def add_bot_message(self, message):

        frame = ctk.CTkFrame(
            self.messages,
            fg_color=("#F1F5F9", "#1F2937"),
            corner_radius=15
        )

        frame.grid(
            row=self.messages.grid_size()[1],
            column=0,
            sticky="w",
            padx=(10, 150),
            pady=8
        )

        label = ctk.CTkLabel(
            frame,
            text=message,
            font=ctk.CTkFont(size=13),
            wraplength=500,
            justify="left"
        )

        label.pack(
            padx=15,
            pady=10
        )


    # =====================================================
    # SEND MESSAGE
    # =====================================================

    def send_message(self):

        message = self.message_entry.get().strip()

        if message == "":
            return

        # Show user message
        self.add_user_message(message)

        # Get response
        response = chatbot_response(message)

        # Show bot response
        self.add_bot_message(response)

        # Clear input
        self.message_entry.delete(0, "end")


    # =====================================================
    # QUICK QUESTIONS
    # =====================================================

    def quick_question(self, question):

        questions = {
            "👋  Say Hello": "Hello",
            "😊  How are you?": "How are you",
            "🤖  Who are you?": "Who are you",
            "💡  What can you do?": "What can you do",
            "⏰  Tell me the time": "What is the time",
            "📅  Today's date": "What is today's date"
        }

        message = questions[question]

        self.add_user_message(message)

        response = chatbot_response(message)

        self.add_bot_message(response)


    # =====================================================
    # NEW CHAT
    # =====================================================

    def new_chat(self):

        for widget in self.messages.winfo_children():
            widget.destroy()

        self.add_bot_message(
            "New conversation started! 👋\n\n"
            "How can I help you?"
        )


    # =====================================================
    # CLEAR CHAT
    # =====================================================

    def clear_chat(self):

        for widget in self.messages.winfo_children():
            widget.destroy()

        self.add_bot_message(
            "Chat cleared successfully. 🧹\n\n"
            "Let's start again!"
        )


    # =====================================================
    # CHANGE THEME
    # =====================================================

    def toggle_theme(self):

        current = ctk.get_appearance_mode()

        if current == "Dark":
            ctk.set_appearance_mode("light")
        else:
            ctk.set_appearance_mode("dark")


# =========================================================
# RUN APPLICATION
# =========================================================

if __name__ == "__main__":

    app = SmartBot()

    app.mainloop()