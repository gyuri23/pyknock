# !/usr/bin/python3
from tkinter import *


def donothing():
    filewin = Toplevel(root)
    button = Button(filewin, text="Do nothing button")
    button.pack()


def settings():
    knock1 = 0
    port = 'TCP'

    settings_window = Toplevel(root)
    #settings_window.minsize(500, 500)
    #settings_window.geometry('+550+150')

    r1 = Radiobutton(settings_window, text="TCP", variable=port, value="TCP")
    r2 = Radiobutton(settings_window, text="UDP", variable=port, value="UDP")


    r1.grid(row=0, column=1)
    r2.grid(row=1, column=1)

    # Label(settings_window, text="Protocol: ").grid(row=0, column=0)
    Label(settings_window, text="Port: ").grid(row=0, column=2)
    # Label(settings_window, text="Last Name").grid(row=1)
    #
    e1 = Entry(settings_window)
    # e2 = Entry(settings_window)
    #
    e1.grid(row=0, column=3)
    # e2.grid(row=0, column=3)
    #knock_input.focus()

# Teszt
# ============================= Főprogram =====================================

root = Tk()

menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="New", command=donothing)
filemenu.add_command(label="Open", command=donothing)
filemenu.add_command(label="Save", command=donothing)
filemenu.add_command(label="Save as...", command=donothing)
filemenu.add_command(label="Close", command=donothing)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="File", menu=filemenu)

settingsmenu = Menu(menubar, tearoff=0)
settingsmenu.add_command(label="Settings", command=settings)
menubar.add_cascade(label="Settings", menu=settingsmenu)

helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="Help Index", command=donothing)
helpmenu.add_command(label="About...", command=donothing)
menubar.add_cascade(label="Help", menu=helpmenu)


root.title('PyKnock')
root.config(menu=menubar)
root.mainloop()
