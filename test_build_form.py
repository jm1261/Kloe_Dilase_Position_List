from tkinter import *
from tkinter.ttk import Combobox
import json


def position_list_preview():
    '''
    '''
    preview_window = Tk()
    preview_window.title("Position List - Preview")
    preview_row = Frame(preview_window)
    preview_row.pack(side=TOP, fill=X, padx=5, pady=5)
    preview_entry = Entry(preview_row, textvariable="Test",state="disabled")
    preview_entry.pack(side=LEFT, expand=YES, fill=BOTH, padx=5, pady=5)
    preview_window.mainloop()


def save_position_list(fields, entries):
    '''
    '''
    position_dict = {}
    return position_dict


def position_list_window(users, filenames):
    '''
    '''
    window = Tk()
    window.title("Position List - Pattern Matrix Copy")
    initial_value = StringVar(window,value=0)
    initial_dirpath = StringVar(window, value="D:\\LITHO FILES\\")

    dirpath_row = Frame(window)
    dirpath_row.pack(side=TOP, fill=X, padx=5, pady=5)
    dirpath_label = Label(dirpath_row,width=15,text="Directory Path",font=("Times New Roman", 14))
    dirpath_label.pack(side=LEFT, expand=YES, fill=X, padx=5, pady=5)
    dirpath_entry = Entry(dirpath_row, textvariable=initial_dirpath,state="disabled")
    dirpath_entry.pack(side=LEFT, expand=YES, fill=X, padx=5, pady=5)

    user_row = Frame(window)
    user_row.pack(side=TOP, fill=X, padx=5, pady=5)
    user_label = Label(user_row,width=15,text="User",font=("Times New Roman", 14))
    user_label.pack(side=LEFT, expand=YES, fill=X, padx=5, pady=5)
    user_entry = Combobox(user_row,values=users)
    user_entry.current(0)
    user_entry.pack(side=LEFT, expand=YES, fill=X, padx=5, pady=5)
    dirpath_update = user_entry.get()

    filename_row = Frame(window)
    filename_row.pack(side=TOP, fill=X, padx=5, pady=5)
    filename_label = Label(filename_row,width=15,text="Filename",font=("Times New Roman", 14))
    filename_label.pack(side=LEFT, expand=YES, fill=X, padx=5, pady=5)
    filename_entry = Combobox(filename_row,values=filenames)
    filename_entry.current(0)
    filename_entry.pack(side=LEFT, expand=YES, fill=X, padx=5, pady=5)

    laser_row = Frame(window)
    laser_row.pack(side=TOP, fill=X, padx=5, pady=5)
    laser_label = Label(laser_row,width=15,text="Laser",font=("Times New Roman", 14))
    laser_label.pack(side=LEFT, expand=YES, fill=X, padx=5, pady=5)
    laser_choice_0 = IntVar()
    laser_choice_0.set(0)
    laser_entry_1 = Radiobutton(laser_row,text="0.5μm Line",variable=laser_choice_0,value=0,font=("Times New Roman",14))
    laser_entry_1.pack(side=LEFT, expand=YES, fill=X, padx=5, pady=5)
    laser_entry_2 = Radiobutton(laser_row,text="10μm Line",variable=laser_choice_0,value=1,font=("Times New Roman",14))
    laser_entry_2.pack(side=LEFT, expand=YES, fill=X, padx=5, pady=5)

    modulation_row = Frame(window)
    modulation_row.pack(side=TOP, fill=X, padx=5, pady=5)
    modulation_label = Label(modulation_row,width=15,text="Modulation",font=("Times New Roman", 14))
    modulation_label.pack(side=LEFT, expand=YES, fill=X, padx=5, pady=5)
    modulation_entry = Entry(modulation_row, textvariable=initial_value)
    modulation_entry.pack(side=LEFT, expand=YES, fill=X, padx=5, pady=5)

    velocity_row = Frame(window)
    velocity_row.pack(side=TOP, fill=X, padx=5, pady=5)
    velocity_label = Label(velocity_row,width=15,text="Velocity",font=("Times New Roman", 14))
    velocity_label.pack(side=LEFT, expand=YES, fill=X, padx=5, pady=5)
    velocity_entry = Entry(velocity_row, textvariable=initial_value)
    velocity_entry.pack(side=LEFT, expand=YES, fill=X, padx=5, pady=5)

    x_initial_row = Frame(window)
    x_initial_row.pack(side=TOP, fill=X, padx=5, pady=5)
    x_initial_label = Label(x_initial_row,width=15,text="X Position",font=("Times New Roman", 14))
    x_initial_label.pack(side=LEFT, expand=YES, fill=X, padx=5, pady=5)
    x_initial_entry = Entry(x_initial_row, textvariable=initial_value)
    x_initial_entry.pack(side=LEFT, expand=YES, fill=X, padx=5, pady=5)

    y_initial_row = Frame(window)
    y_initial_row.pack(side=TOP, fill=X, padx=5, pady=5)
    y_initial_label = Label(y_initial_row,width=15,text="Y Position",font=("Times New Roman", 14))
    y_initial_label.pack(side=LEFT, expand=YES, fill=X, padx=5, pady=5)
    y_initial_entry = Entry(y_initial_row, textvariable=initial_value)
    y_initial_entry.pack(side=LEFT, expand=YES, fill=X, padx=5, pady=5)

    z_initial_row = Frame(window)
    z_initial_row.pack(side=TOP, fill=X, padx=5, pady=5)
    z_initial_label = Label(z_initial_row,width=15,text="Z Position",font=("Times New Roman", 14))
    z_initial_label.pack(side=LEFT, expand=YES, fill=X, padx=5, pady=5)
    z_initial_entry = Entry(z_initial_row, textvariable=initial_value)
    z_initial_entry.pack(side=LEFT, expand=YES, fill=X, padx=5, pady=5)

    delta_modulation_row = Frame(window)
    delta_modulation_row.pack(side=TOP, fill=X, padx=5, pady=5)
    delta_modulation_label = Label(delta_modulation_row,width=15,text="Delta Modulation",font=("Times New Roman", 14))
    delta_modulation_label.pack(side=LEFT, expand=YES, fill=X, padx=5, pady=5)
    delta_modulation_entry = Entry(delta_modulation_row, textvariable=initial_value)
    delta_modulation_entry.pack(side=LEFT, expand=YES, fill=X, padx=5, pady=5)

    delta_velocity_row = Frame(window)
    delta_velocity_row.pack(side=TOP, fill=X, padx=5, pady=5)
    delta_velocity_label = Label(delta_velocity_row,width=15,text="Delta Velocity",font=("Times New Roman", 14))
    delta_velocity_label.pack(side=LEFT, expand=YES, fill=X, padx=5, pady=5)
    delta_velocity_entry = Entry(delta_velocity_row, textvariable=initial_value)
    delta_velocity_entry.pack(side=LEFT, expand=YES, fill=X, padx=5, pady=5)

    delta_x_row = Frame(window)
    delta_x_row.pack(side=TOP, fill=X, padx=5, pady=5)
    delta_x_label = Label(delta_x_row,width=15,text="Delta X",font=("Times New Roman", 14))
    delta_x_label.pack(side=LEFT, expand=YES, fill=X, padx=5, pady=5)
    delta_x_entry = Entry(delta_x_row, textvariable=initial_value)
    delta_x_entry.pack(side=LEFT, expand=YES, fill=X, padx=5, pady=5)

    delta_y_row = Frame(window)
    delta_y_row.pack(side=TOP, fill=X, padx=5, pady=5)
    delta_y_label = Label(delta_y_row,width=15,text="Delta Y",font=("Times New Roman", 14))
    delta_y_label.pack(side=LEFT, expand=YES, fill=X, padx=5, pady=5)
    delta_y_entry = Entry(delta_y_row, textvariable=initial_value)
    delta_y_entry.pack(side=LEFT, expand=YES, fill=X, padx=5, pady=5)

    delta_z_row = Frame(window)
    delta_z_row.pack(side=TOP, fill=X, padx=5, pady=5)
    delta_z_label = Label(delta_z_row,width=15,text="Delta Z",font=("Times New Roman", 14))
    delta_z_label.pack(side=LEFT, expand=YES, fill=X, padx=5, pady=5)
    delta_z_entry = Entry(delta_z_row, textvariable=initial_value)
    delta_z_entry.pack(side=LEFT, expand=YES, fill=X, padx=5, pady=5)

    button_row = Frame(window)
    button_row.pack(side=TOP, fill=X, padx=5, pady=5)
    preview_button = Button(button_row, text="Preview List", command=position_list_preview, font=("Times New Roman", 14))
    preview_button.pack(side=LEFT, expand=YES, fill=X, padx=5, pady=5)
    #save_button = Button(button_row, text="Save", command=save_position_list(fields=fields,entries=entries), font=("Times New Roman", 14))
    #save_button.pack(side=LEFT, expand=YES, fill=X, padx=5, pady=5)
    close_button = Button(button_row, text="Exit", command=quit, font=("Times New ROman", 14))
    close_button.pack(side=RIGHT, expand=YES, fill=X, padx=5, pady=5)

    entries = [dirpath_entry, user_entry, filename_entry, laser_choice_0, modulation_entry]

    window.mainloop()
    return entries


if __name__ == "__main__":
    users = ["Josh", "Alex", "Chris", "Donato", "George"]
    all_fields = ["Dirpath","User","Filename","Laser","Modulation","Velocity","X_initial",
    "Y_initial","Z_initial","Delta_mod","Delta_vel","Delta_x","Delta_y","Delta_z",
    "Repeats"]
    filenames = ["Test", "Square", "Contacts"]
    #position_list_window(users=users, filenames=filenames)
    #print(entries)
