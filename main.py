from tkinter import *
from tkinter.filedialog import askopenfilename
from tkinter.scrolledtext import ScrolledText
import tkinter as tk

root = tk.Tk()
text_area = ScrolledText(root)


def SaveFile():
    print("New File!")
    file_name = askopenfilename()

    if file_name:
        f = text_area.get("1.0", "end")
        f.write(f)
        f.close()

def OpenFile():
    name = askopenfilename()
    file = open(name, "r")
    opened = file.read()
    print(opened)
    text_area.insert(tk.INSERT, opened)

    print(name)


class FileMenu:

    def __init__(self, name):
        self.menu_name = name

    def filemenu(self):
        menu = Menu(root)
        root.config(menu=menu)
        file_menu = Menu(menu)
        menu.add_cascade(label=self.menu_name, menu=file_menu)

        file_menu.add_command(label="Save", command=SaveFile)
        file_menu.add_command(label="Open...", command=OpenFile)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=root.quit)


menu = FileMenu("File")
menu.filemenu()
text_area.pack()

mainloop()
