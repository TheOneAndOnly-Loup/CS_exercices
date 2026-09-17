import tkinter as tk

root = tk.Tk()
label = tk.Label(text="Choose")
new_task = tk.Button(
    text="Add a task",
    width=25,
    height=5,
    bg="grey",
    fg="black",
    borderwidth=10
)
remove_task = tk.Button(
    text="Mark as completed",
    width=25,
    height=5,
    bg="grey",
    fg="black",
    borderwidth=10,
)
label.pack()
new_task.pack()
remove_task.pack()              
root.mainloop()