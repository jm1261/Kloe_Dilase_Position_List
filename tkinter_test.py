# Import tkinter module
from tkinter import *
from tkinter.ttk import Combobox

# Tk() creates a top-level window (root)
window = Tk()

# A button can be created using the Button class, Button(window, attributes)
btn = Button(window, text="This is a button widget", fg='blue')
btn.place(x=200, y=10)

# Radiobutton is a widget displaying a toggle button having an on/off state
# There may be more than one but only one will be on at any time
v0 = IntVar()
v0.set(1)
r1 = Radiobutton(window, text="0.5", variable=v0, value=1)
r2 = Radiobutton(window, text="10", variable=v0, value=2)
r1.place(x=100, y=50)
r2.place(x=180, y=50)

# Checkbutton is also a toggle button, a rectangular check box appears before
# its caption. Its on state is displayed by the tick mark, disappears when off
v1 = IntVar()
v2 = IntVar()
C1 = Checkbutton(window, text="Matrix Copy Object", variable=v1)
C2 = Checkbutton(window, text="Matrix Copy Positions", variable=v2)
C1.place(x=100, y=100)
C2.place(x=180, y=100)

# Combobox is defined in the ttk module, it populates drop down data from a
# collection data type, such as a tuple or list as value parameters
data = ("one", "two", "three", "four")
cb = Combobox(window, values=data)
cb.place(x=60, y=450)

# Listbox is a widget that dsplays the entire collection of string items,
# the user can select one or multiple items
lb = Listbox(window, height=5, selectmode='multiple')
for num in data:
    lb.insert(END,num)
lb.place(x=250, y=150)

# A label can be created in the UI in python using the label class
# The label constructor requires top-level window object and options parameters
lbl = Label(window, text="This is a label widget", fg='red', font=("Helvetica", 16))
lbl.place(x=60, y=500)

# The entry widget renders a single-line text box for accepting the user input
# For multi-line text input use the Text widget
# The entry class also accepts bd [border size] and show [to covert text into
# a password field, set show to "*"]
txtfld = Entry(window, text="This is an entry widget", bd=5)
txtfld.place(x=80, y=150)

# Give the window a title at the top of the window
window.title("Position List")

# The geometry() method defines the width height and coordinates of the top
# left corner of the frame in pixels. ("widthxheight+XPOS+YPOS")
window.geometry("500x500+100+100")

# The application object enters an event listening loop by calling mainloop()
window.mainloop()
