import tkinter as tk
from tkinter import messagebox
import datetime

class ReminderApp:
    def __init__(self, root):
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

        self.label_time = tk.Label(root, text="Reminder Time (HH:MM):")
        self.label_time.pack(pady=5)

        self.entry_time = tk.Entry(root)
        self.entry_time.pack(pady=5)

        self.button_add = tk.Button(root, text="Add Reminder", command=self.add_reminder)
        self.button_add.pack(pady=10)

        self.button_show = tk.Button(root, text="Show Reminders", command=self.show_reminders)
        self.button_show.pack(pady=10)

        self.listbox_reminders = tk.Listbox(root, height=10, width=50)
        self.listbox_reminders.pack(pady=10)

    def add_reminder(self):
        title = self.entry_title.get()
        date = self.entry_date.get()
        time = self.entry_time.get()

        if not title or not date or not time:
            messagebox.showerror("Error", "All fields must be filled out")
            return

        try:
            reminder_datetime = datetime.datetime.strptime(f"{date} {time}", "%Y-%m-%d %H:%M")
        except ValueError:
            messagebox.showerror("Error", "Invalid date or time format")
            return

        reminder = {"title": title, "datetime": reminder_datetime}
        self.reminders.append(reminder)
        self.clear_entries()
        messagebox.showinfo("Success", "Reminder added successfully")

    def show_reminders(self):
        self.listbox_reminders.delete(0, tk.END)
        for reminder in self.reminders:
            self.listbox_reminders.insert(tk.END, f"{reminder['title']} - {reminder['datetime'].strftime('%Y-%m-%d %H:%M')}")

    def clear_entries(self):
        self.entry_title.delete(0, tk.END)
        self.entry_date.delete(0, tk.END)
        self.entry_time.delete(0, tk.END)

# Create the main window
root = tk.Tk()
app = ReminderApp(root)
root.mainloop()
