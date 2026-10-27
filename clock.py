import tkinter as tk
from datetime import datetime


def update_clock():
	now = datetime.now()
	time_label.config(text=now.strftime("%H:%M:%S"))
	date_label.config(text=now.strftime("%A, %B %d, %Y"))
	root.after(1000, update_clock)


root = tk.Tk()
root.title("Clock")
root.configure(bg="#101820")
root.resizable(False, False)

time_label = tk.Label(
	root,
	font=("Segoe UI", 48, "bold"),
	fg="#F2AA4C",
	bg="#101820",
	padx=28,
	pady=24,
)
time_label.pack()

date_label = tk.Label(
	root,
	font=("Segoe UI", 14),
	fg="#F2F2F2",
	bg="#101820",
	padx=28,
	pady=22,
)
date_label.pack()

update_clock()
root.mainloop()
