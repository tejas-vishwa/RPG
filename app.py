"""
Random Password Generator
A secure desktop application built with Python 3 and Tkinter.
Uses the cryptographically secure `secrets` module for password generation.
"""

import string
import secrets
import tkinter as tk
from tkinter import ttk, messagebox


def generate_secure_password(length: int, use_upper: bool, use_lower: bool, use_digits: bool, use_symbols: bool) -> str:
    """
    Generate a cryptographically secure random password based on the selected options.

    Security guarantees:
    - Uses secrets.choice() and secrets.SystemRandom().shuffle().
    - At least one character from each enabled category is forcibly included.
    - Remaining characters are selected from the combined pool of enabled categories.
    - The character list is securely shuffled before being joined.
    """
    categories = []
    if use_upper:
        categories.append(string.ascii_uppercase)
    if use_lower:
        categories.append(string.ascii_lowercase)
    if use_digits:
        categories.append(string.digits)
    if use_symbols:
        categories.append(string.punctuation)

    if not categories:
        raise ValueError("No character categories selected.")

    if length < len(categories):
        raise ValueError("Password length cannot be shorter than the number of selected categories.")

    # Guarantee at least one character from each enabled category
    password_chars = [secrets.choice(cat) for cat in categories]

    # Combined pool for the remaining characters
    combined_pool = "".join(categories)

    # Fill remaining characters
    remaining_count = length - len(password_chars)
    for _ in range(remaining_count):
        password_chars.append(secrets.choice(combined_pool))

    # Cryptographically secure in-place shuffle
    secrets.SystemRandom().shuffle(password_chars)

    return "".join(password_chars)


class PasswordGeneratorApp:
    """Main GUI Application using Tkinter."""

    def __init__(self, root: tk.Tk):
        self.root = root
        self.root.title("Random Password Generator")
        self.root.geometry("620x560")
        self.root.resizable(False, False)

        # Color Palette - Modern Clean Light Theme
        self.bg_color = "#f4f6f9"
        self.card_bg = "#ffffff"
        self.text_main = "#1e293b"
        self.text_muted = "#64748b"
        self.border_color = "#e2e8f0"
        self.primary_color = "#4f46e5"       # Indigo
        self.primary_hover = "#4338ca"
        self.success_color = "#059669"       # Emerald
        self.clear_btn_bg = "#f1f5f9"
        self.clear_btn_fg = "#475569"

        self.root.configure(bg=self.bg_color)

        # Variables
        self.length_var = tk.StringVar(value="12")
        self.upper_var = tk.BooleanVar(value=True)
        self.lower_var = tk.BooleanVar(value=True)
        self.digits_var = tk.BooleanVar(value=True)
        self.symbols_var = tk.BooleanVar(value=True)
        self.status_var = tk.StringVar(value="Ready.")

        self._build_ui()

    def _build_ui(self):
        # Main Card Container
        main_frame = tk.Frame(
            self.root,
            bg=self.card_bg,
            bd=1,
            relief="solid",
            highlightthickness=0
        )
        main_frame.place(relx=0.5, rely=0.48, anchor="center", width=570, height=490)

        # Header: Title & Subtitle
        header_frame = tk.Frame(main_frame, bg=self.card_bg)
        header_frame.pack(fill="x", padx=30, pady=(22, 10))

        title_label = tk.Label(
            header_frame,
            text="Random Password Generator",
            font=("Segoe UI", 18, "bold"),
            fg=self.text_main,
            bg=self.card_bg
        )
        title_label.pack(anchor="center")

        subtitle_label = tk.Label(
            header_frame,
            text="Create a strong password in a few simple steps",
            font=("Segoe UI", 10),
            fg=self.text_muted,
            bg=self.card_bg
        )
        subtitle_label.pack(anchor="center", pady=(3, 0))

        # Length Input Section
        length_frame = tk.Frame(main_frame, bg=self.card_bg)
        length_frame.pack(fill="x", padx=35, pady=(12, 12))

        length_label = tk.Label(
            length_frame,
            text="Password Length:",
            font=("Segoe UI", 11, "bold"),
            fg=self.text_main,
            bg=self.card_bg
        )
        length_label.pack(side="left")

        self.length_entry = tk.Entry(
            length_frame,
            textvariable=self.length_var,
            font=("Segoe UI", 11),
            width=8,
            justify="center",
            bd=1,
            relief="solid",
            highlightthickness=1,
            highlightbackground=self.border_color,
            highlightcolor=self.primary_color
        )
        self.length_entry.pack(side="left", padx=(12, 10))

        length_hint = tk.Label(
            length_frame,
            text="(Minimum 4 characters, 12+ recommended)",
            font=("Segoe UI", 9),
            fg=self.text_muted,
            bg=self.card_bg
        )
        length_hint.pack(side="left")

        # Labelled Frame for Character Options
        options_frame = tk.LabelFrame(
            main_frame,
            text=" Character Options ",
            font=("Segoe UI", 10, "bold"),
            fg=self.text_main,
            bg=self.card_bg,
            bd=1,
            relief="solid"
        )
        options_frame.pack(fill="x", padx=35, pady=(0, 15), ipady=6)

        # 4 Checkbuttons in a clean 2x2 grid
        cb_grid = tk.Frame(options_frame, bg=self.card_bg)
        cb_grid.pack(fill="both", expand=True, padx=15, pady=8)

        check_style = {
            "font": ("Segoe UI", 10),
            "fg": self.text_main,
            "bg": self.card_bg,
            "activebackground": self.card_bg,
            "activeforeground": self.text_main,
            "selectcolor": "#ffffff",
            "anchor": "w"
        }

        cb_upper = tk.Checkbutton(
            cb_grid,
            text="Uppercase letters (A-Z)",
            variable=self.upper_var,
            **check_style
        )
        cb_upper.grid(row=0, column=0, sticky="w", padx=(0, 15), pady=4)

        cb_lower = tk.Checkbutton(
            cb_grid,
            text="Lowercase letters (a-z)",
            variable=self.lower_var,
            **check_style
        )
        cb_lower.grid(row=0, column=1, sticky="w", padx=(15, 0), pady=4)

        cb_digits = tk.Checkbutton(
            cb_grid,
            text="Numbers (0-9)",
            variable=self.digits_var,
            **check_style
        )
        cb_digits.grid(row=1, column=0, sticky="w", padx=(0, 15), pady=4)

        cb_symbols = tk.Checkbutton(
            cb_grid,
            text="Special symbols (!, @, #, ...)",
            variable=self.symbols_var,
            **check_style
        )
        cb_symbols.grid(row=1, column=1, sticky="w", padx=(15, 0), pady=4)

        # Output Field (Read-only Entry widget, centered, Monospace font)
        output_frame = tk.Frame(main_frame, bg=self.card_bg)
        output_frame.pack(fill="x", padx=35, pady=(0, 14))

        output_label = tk.Label(
            output_frame,
            text="Generated Password:",
            font=("Segoe UI", 10, "bold"),
            fg=self.text_main,
            bg=self.card_bg
        )
        output_label.pack(anchor="w", pady=(0, 4))

        self.output_entry = tk.Entry(
            output_frame,
            font=("Consolas", 14, "bold"),
            justify="center",
            bd=1,
            relief="solid",
            state="readonly",
            readonlybackground="#f8fafc",
            fg="#0f172a"
        )
        self.output_entry.pack(fill="x", ipady=8)

        # Action Buttons Section
        buttons_frame = tk.Frame(main_frame, bg=self.card_bg)
        buttons_frame.pack(fill="x", padx=35, pady=(4, 12))

        # Generate Button
        self.generate_btn = tk.Button(
            buttons_frame,
            text="GENERATE PASSWORD",
            command=self.on_generate,
            font=("Segoe UI", 10, "bold"),
            bg=self.primary_color,
            fg="#ffffff",
            activebackground=self.primary_hover,
            activeforeground="#ffffff",
            bd=0,
            relief="flat",
            cursor="hand2",
            padx=14,
            pady=8
        )
        self.generate_btn.pack(side="left", expand=True, fill="x", padx=(0, 6))

        # Copy Button
        self.copy_btn = tk.Button(
            buttons_frame,
            text="COPY PASSWORD",
            command=self.on_copy,
            font=("Segoe UI", 10, "bold"),
            bg=self.success_color,
            fg="#ffffff",
            activebackground="#047857",
            activeforeground="#ffffff",
            bd=0,
            relief="flat",
            cursor="hand2",
            padx=14,
            pady=8
        )
        self.copy_btn.pack(side="left", expand=True, fill="x", padx=3)

        # Clear Button
        self.clear_btn = tk.Button(
            buttons_frame,
            text="CLEAR",
            command=self.on_clear,
            font=("Segoe UI", 10, "bold"),
            bg=self.clear_btn_bg,
            fg=self.clear_btn_fg,
            activebackground="#e2e8f0",
            activeforeground=self.clear_btn_fg,
            bd=1,
            relief="solid",
            cursor="hand2",
            padx=14,
            pady=8
        )
        self.clear_btn.pack(side="left", expand=True, fill="x", padx=(6, 0))

        # Status Bar at Bottom
        status_bar = tk.Frame(self.root, bg=self.bg_color)
        status_bar.pack(side="bottom", fill="x", padx=25, pady=(0, 10))

        self.status_label = tk.Label(
            status_bar,
            textvariable=self.status_var,
            font=("Segoe UI", 9),
            fg=self.text_muted,
            bg=self.bg_color,
            anchor="w"
        )
        self.status_label.pack(side="left", fill="x")

    def on_generate(self):
        """Validate input and generate a secure password."""
        raw_length = self.length_var.get().strip()

        # Validation: valid whole number
        try:
            length = int(raw_length)
        except ValueError:
            messagebox.showwarning(
                "Invalid Input",
                "Please enter a valid whole number for the password length."
            )
            self.status_var.set("Error: Invalid length input.")
            return

        # Validation: length < 4
        if length < 4:
            messagebox.showwarning(
                "Length Too Short",
                "Password length must be at least 4 characters."
            )
            self.status_var.set("Error: Length must be at least 4.")
            return

        # Check selected categories
        selected_count = sum([
            self.upper_var.get(),
            self.lower_var.get(),
            self.digits_var.get(),
            self.symbols_var.get()
        ])

        # Validation: no character categories selected
        if selected_count == 0:
            messagebox.showwarning(
                "No Options Selected",
                "Please select at least one character category."
            )
            self.status_var.set("Error: No character options selected.")
            return

        # Validation: requested length shorter than number of selected categories
        if length < selected_count:
            messagebox.showwarning(
                "Length Conflict",
                f"Password length ({length}) cannot be shorter than the number of selected categories ({selected_count})."
            )
            self.status_var.set("Error: Length shorter than selected categories.")
            return

        # Generate password
        password = generate_secure_password(
            length=length,
            use_upper=self.upper_var.get(),
            use_lower=self.lower_var.get(),
            use_digits=self.digits_var.get(),
            use_symbols=self.symbols_var.get()
        )

        # Display result in read-only entry
        self.output_entry.config(state="normal")
        self.output_entry.delete(0, tk.END)
        self.output_entry.insert(0, password)
        self.output_entry.config(state="readonly")

        self.status_var.set("Password generated successfully!")

    def on_copy(self):
        """Copy generated password to system clipboard."""
        password = self.output_entry.get()
        if not password:
            messagebox.showwarning(
                "No Password",
                "No password has been generated yet to copy."
            )
            self.status_var.set("Warning: Nothing to copy.")
            return

        self.root.clipboard_clear()
        self.root.clipboard_append(password)
        self.root.update()  # keeps clipboard contents
        self.status_var.set("Password copied to clipboard!")

    def on_clear(self):
        """Reset inputs and output to default state."""
        self.length_var.set("12")
        self.output_entry.config(state="normal")
        self.output_entry.delete(0, tk.END)
        self.output_entry.config(state="readonly")
        self.status_var.set("Ready.")


def main():
    root = tk.Tk()
    app = PasswordGeneratorApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
