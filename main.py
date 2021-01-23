from tkinter import *
from tkinter.filedialog import askopenfilename
from tkinter import filedialog
from tkinter.scrolledtext import ScrolledText
import tkinter as tk

root = tk.Tk()
text_area = ScrolledText(root)
global entry1


def savefile():
    print("New File!")
    file_name = filedialog.asksaveasfilename(initialdir="/Desktop", title="Select file",
                                             filetypes=(("text files", ".txt"), ("all files", ".")))

    if file_name:
        file = open(file_name, "w")
        text = text_area.get("1.0", END)
        file.writelines(text)
        file = open(file_name)
        content = file.read()
        file.close()
        print(content)


def openfile():
    name = askopenfilename()
    file = open(name, "r")
    opened = file.read()
    print(opened)
    text_area.insert(tk.INSERT, opened)

    print(name)


def check():
    try:
        print(text_area.get("1.0", END))
    except:
        print("nothing")


def newfile():
    file_name = filedialog.asksaveasfilename(initialdir="/Desktop", title="Select file",
                                 filetypes=(("text files", ".txt"), ("all files", ".")))

    if file_name:
        file = open(file_name, "w")
        file.writelines(" ")
        file.close()


class FileMenu:

    def __init__(self, name):
        self.menu_name = name

    def filemenu(self):
        menu = Menu(root)
        root.config(menu=menu)
        file_menu = Menu(menu)
        menu.add_cascade(label=self.menu_name, menu=file_menu)

        file_menu.add_command(label="New", command=newfile)
        file_menu.add_command(label="Save", command=savefile)
        file_menu.add_command(label="Open...", command=openfile)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=root.quit)
        file_menu.add_command(label="check", command=check())


menu = FileMenu("File")
menu.filemenu()
text_area.pack()



mainloop()
