from tkinter import *
from text_file import FileMod


def create_file():
    filemod.create_file()
    text_widget.delete(1.0, END)
    text_widget.insert(END, filemod.read())


def add_line():
    filemod.add_line(add_entry.get())
    text_widget.delete(1.0, END)
    text_widget.insert(END, filemod.read())


def read():
    text_widget.delete(1.0, END)
    text_widget.insert(END, filemod.read())


def erase():
    text_widget.delete(1.0, END)
    text_widget.insert(END, filemod.erase())


def find_adv():
    symbol = str(find_adv_entry1.get())
    length = int(find_adv_entry2.get())
    text_widget.delete(1.0, END)
    text_widget.insert(END, filemod.finder_adv(symbol, length))


def find():
    symbol = find_entry.get()
    text_widget.delete(1.0, END)
    text_widget.insert(END, filemod.finder(symbol))


filemod = FileMod()
filemod.erase()

mainframe = Tk()

text_widget = Text(mainframe)
text_widget.pack(side=BOTTOM)

create_button = Button(mainframe, text="Create File", command=create_file)
create_button.pack(side=RIGHT)

erase_button = Button(mainframe, text="Erase File", command=erase)
erase_button.pack(side=RIGHT)

read_button = Button(mainframe, text="Read File", command=read)
read_button.pack(side=RIGHT)

add_entry = Entry(mainframe)
add_entry.pack(side=BOTTOM)
add_button = Button(mainframe, text="Add Line", command=add_line)
add_button.pack(side=BOTTOM)

find_entry = Entry(mainframe)
find_entry.pack(side=BOTTOM)
find_button = Button(mainframe, text="Find symbol", command=find)
find_button.pack(side=BOTTOM)

find_adv_button = Button(mainframe, text="Find #1symbol and #2length", command=find_adv)
find_adv_button.pack(side=TOP)
find_adv_entry1 = Entry(mainframe)
find_adv_entry1.pack(side=TOP)
find_adv_entry2 = Entry(mainframe)
find_adv_entry2.pack(side=TOP)

mainframe.mainloop()
