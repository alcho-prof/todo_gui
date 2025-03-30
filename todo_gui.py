import tkinter as tk
from tkinter import messagebox
import os

TASKS_FILE = "tasks.txt"

# Load tasks from file
def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r") as f:
            return [line.strip() for line in f.readlines()]
    return []

# Save tasks to file
def save_tasks():
    with open(TASKS_FILE, "w") as f:
        for task in task_listbox.get(0, tk.END):
            f.write(task + "\n")

# Add task function
def add_task():
    task = task_entry.get()
    if task:
        task_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
        save_tasks()
    else:
        messagebox.showwarning("Warning", "Task cannot be empty!")

# Mark task as done
def mark_done():
    try:
        selected_index = task_listbox.curselection()[0]
        task = task_listbox.get(selected_index)
        if "✔" not in task:
            task_listbox.delete(selected_index)
            task_listbox.insert(selected_index, task + " ✔")
            save_tasks()
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task!")

# Remove task
def remove_task():
    try:
        selected_index = task_listbox.curselection()[0]
        task_listbox.delete(selected_index)
        save_tasks()
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task!")

# Create main window
root = tk.Tk()
root.title("To-Do List")
root.geometry("400x500")

# Task Entry Field
task_entry = tk.Entry(root, width=40)
task_entry.pack(pady=10)

# Buttons
add_button = tk.Button(root, text="Add Task", command=add_task)
add_button.pack()

mark_done_button = tk.Button(root, text="Mark Done", command=mark_done)
mark_done_button.pack()

remove_button = tk.Button(root, text="Remove Task", command=remove_task)
remove_button.pack()

# Task Listbox
task_listbox = tk.Listbox(root, width=50, height=15)
task_listbox.pack(pady=10)

# Load tasks into the listbox
for task in load_tasks():
    task_listbox.insert(tk.END, task)

# Run the application
root.mainloop()
