"""
Diary app
"""
from tkinter import Tk
from tkinter import ttk

long_list = [
    "this",
    "list",
    "contains",
    "too",
    "many",
    "elements",
    "for",
    "one",
    "line",
]
for i in long_list:
    print(i)
root = Tk()
ttk.Button(root, text="Hello World").grid()
root.mainloop()
