from tkinter import *
from tkinter.ttk import Combobox

fields = ["Dirpath","User","Filename","Laser","Modulation","Velocity","X_initial",
"Y_initial","Z_initial","Delta_mod","Delta_vel","Delta_x","Delta_y","Delta_z",
"Repeats"]
users = ["Josh", "Alex", "Chris", "Donato", "George"]
filenames = ["Test", "Square", "Contacts"]

def fetch(entries):
    for entry in entries:
        field = entry[0]
        text = entry[1].get()
        print('%s: "%s"' % (field, text))

def makeform(root, fields, users, filenames):
    entries = []
    initial_dirpath = StringVar(root, value="D:\\LITHO FILES\\")
    for field in fields:
        row = Frame(root)
        lab = Label(row, width=15, text=field, anchor='w')
        row.pack(side=TOP, fill=X, padx=5, pady=5)
        lab.pack(side=LEFT)
        if field=="Dirpath":
            ent = Entry(row, textvariable=initial_dirpath, state="disabled")
        elif field=="User":
            ent = Combobox(row, values=users)
            ent.current(0)
        elif field=="Filename":
            ent = Combobox(row, values=filenames)
            ent.current(0)
        elif field=="Laser":
        else:
            ent = Entry(row)
            ent.current(0)
        ent.pack(side=RIGHT, expand=YES, fill=X)
        entries.append((field, ent))
    return entries

if __name__ == '__main__':
    root = Tk()
    ents = makeform(root, fields, users, filenames)
    #root.bind('', (lambda event, e=ents: fetch(e)))
    b1 = Button(root, text='Show', command=(lambda e=ents: fetch(e)))
    b1.pack(side=LEFT, padx=5, pady=5)
    root.mainloop()
