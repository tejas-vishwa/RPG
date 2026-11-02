# Random Password Generator

A clean, modern, and cryptographically secure Random Password Generator desktop application built with Python 3 and the standard library (`tkinter`, `secrets`, `string`).

---

## Features

- **Tkinter GUI**:
  - Fixed 620x560 desktop window with a clean, modern light theme.
  - Header with title and descriptive subtitle: *"Create a strong password in a few simple steps"*.
  - Configurable password length (defaults to `12`).
  - Labelled **Character Options** frame with 4 independent checkboxes (all defaulting to checked):
    - Uppercase letters (`A-Z`) &mdash; uses `string.ascii_uppercase`
    - Lowercase letters (`a-z`) &mdash; uses `string.ascii_lowercase`
    - Numbers (`0-9`) &mdash; uses `string.digits`
    - Special symbols (`!, @, #, ...`) &mdash; uses `string.punctuation`
  - Read-only centered output field formatted in **Consolas** monospace font for visual clarity.
  - Three action buttons:
    - **GENERATE PASSWORD**: Validates parameters and creates a secure password.
    - **COPY PASSWORD**: Copies the password directly to the system clipboard.
    - **CLEAR**: Resets input fields, clears output, and restores status to *"Ready."*
  - Real-time status bar at the bottom providing feedback for every action.

- **Cryptographic Security**:
  - Implements the `secrets` standard library module (`secrets.choice` and `secrets.SystemRandom().shuffle`).
  - **Guaranteed Coverage**: At least one character from each enabled category is forcibly included.
  - **Cryptographic Shuffling**: The assembled list of characters is securely shuffled before joining.

- **Validation & Error Handling**:
  - Handles non-integer lengths with try-except `ValueError` checks.
  - Warns with `tkinter.messagebox.showwarning` if:
    - Length is less than 4.
    - No categories are selected.
    - Requested length is shorter than the number of selected categories.

---

## Running the Application

To launch the desktop app, run:

```powershell
py -3 app.py
```

or with Python 3.9+:

```powershell
python app.py
```

---

## Running the Tests

A comprehensive test suite covering generation constraints, entropy distribution, and GUI widget behaviors is included:

```powershell
py -3.9 -m unittest test_generator.py
```
