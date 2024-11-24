# projects-3
reminder app
# Reminder App

A simple and user-friendly reminder application using Tkinter to add and display reminders.

## Features
- Add reminders with title, date, and time.
- Display all added reminders in a list.
- Simple and intuitive GUI.

## Requirements
- Python 3.x

## Installation
1. Install Python 3.x from [python.org](https://www.python.org/).

## Usage
1. Run the `reminder_app.py` file to start the application.
2. Enter the reminder title, date (YYYY-MM-DD), and time (HH:MM).
3. Click "Add Reminder" to save the reminder.
4. Click "Show Reminders" to display all reminders in the list.

## Code
```python
import tkinter as tk
from tkinter import messagebox
import datetime

class ReminderApp:
    def __init__(__(self, root)):
        self.root = root
        self.root.title("Reminder App")
        self.root.geometry("400x400")

        self.reminders = []

        # Create widgets
        self.label_title = tk.Label(root, text="Reminder Title:")
        self.label_title.pack(pady=5)

        self.entry_title = tk.Entry(root)
        self.entry_title.pack(pady=5)

        self.label_date = tk.Label(root, text="Reminder Date (YYYY-MM-DD):")
        self.label_date.pack(pady=5)

        self.entry_date = tk.Entry(root)
        self.entry_date.pack(pady=5)

