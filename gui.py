import tkinter as tk
from tkinter import messagebox
from datetime import datetime

root = tk.Tk()
root.title("To Do List")
root.geometry("500x600")
root.resizable(False, False)
root.configure(bg="#d3d3d3")

title_label = tk.Label(root, text="To Do List", font=("Times New Roman", 20, "bold"), bg="#d3d3d3")
title_label.pack(pady=20)

frame_input = tk.Frame(root, bg="#d3d3d3")
frame_input.pack(pady=5)

task_entry = tk.Entry(frame_input, width=25, font=("Times New Roman", 13))
task_entry.pack(side=tk.LEFT, padx=5)

category_entry = tk.Entry(frame_input, width=15, font=("Times New Roman", 14))
category_entry.pack(side=tk.LEFT, padx=5)
category_entry.insert(0, "Category")  # پیش‌فرض

task_listbox = tk.Listbox(root, width=60, height=12, selectmode=tk.SINGLE, font=("Times New Roman", 13))
task_listbox.pack(pady=10)


def add_task():
    task = task_entry.get().strip()
    category = category_entry.get().strip()

    if task == "":
        messagebox.showwarning("Error", "Enter a task")
        return

    if category == "" or category.lower() == "category":
        category = "General"

    now = datetime.now().strftime("%Y-%m-%d %H:%M")
    task_with_time = f"[{category}] {task} — {now}"

    task_listbox.insert(tk.END, task_with_time)
    task_entry.delete(0, tk.END)
    category_entry.delete(0, tk.END)
    category_entry.insert(0, "Category")


def delete_task():
    try:
        selected_index = task_listbox.curselection()[0]
        task_listbox.delete(selected_index)
    except IndexError:
        messagebox.showwarning("Error", "Choose a task")


def clear_tasks():
    if messagebox.askyesno("Confirmation", "Are you sure you want to clear all tasks?"):
        task_listbox.delete(0, tk.END)


def mark_done():
    try:
        selected_index = task_listbox.curselection()[0]
        task_text = task_listbox.get(selected_index)
        if not task_text.startswith("✔ "):
            task_listbox.delete(selected_index)
            task_listbox.insert(selected_index, "✔ " + task_text)
    except IndexError:
        messagebox.showwarning("Error", "Choose a task")


add_button = tk.Button(frame_input, text="Add Task", command=add_task, bg="blue", fg="black")
add_button.pack(side=tk.LEFT, padx=5)

frame_buttons = tk.Frame(root, bg="#d3d3d3")
frame_buttons.pack(pady=10)

delete_button = tk.Button(frame_buttons, text="Delete Task", command=delete_task, bg="green", fg="black", width=12)
delete_button.grid(row=0, column=0, padx=5)

mark_button = tk.Button(frame_buttons, text="Mark Done", command=mark_done, bg="purple", fg="black", width=12)
mark_button.grid(row=0, column=1, padx=5)

clear_button = tk.Button(frame_buttons, text="Clear All", command=clear_tasks, bg="yellow", fg="black", width=12)
clear_button.grid(row=0, column=2, padx=5)

root.mainloop()
