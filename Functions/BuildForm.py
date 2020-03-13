import tkinter as tk
import json

def file_path():
    '''
    '''
    res.configure(text="test")


def show(entries):
    '''
    Show function takes an array with entries of the form (text, text) and
    prints the entries as text: text. The function is designed for use with a
    user form, where the first entry is a field, and the second entry is a user
    input.
    Args:
        entries: <array> array with the layout (text, text)
    '''
    for entry in entries:
        field = entry[0]
        text = entry[1].get()
        print('%s: %s' % (field, text))


def make_form(root, fields):
    '''
    '''
    entries = []
    for index, field in enumerate(fields):
        row = tk.Frame(root)
        lab = tk.Label(row, width=15, text=field, anchor='w')
        row.pack(side=tk.TOP, fill=tk.X, padx=5, pady=5)
        lab.pack(side=tk.LEFT)
        if index == 0:
            pass
        else:
            ent = tk.Entry(row)
            ent.pack(side=tk.RIGHT, expand=tk.YES, fill=tk.X)
            entries.append((field, ent))
    return entries


def save(entries):
    '''
    Save function takes an array with entries of the form (text, text) and
    writes the entries as text: text. The function is designed for use with a
    user form, where the first entry is a field, and the second entry is a user
    input. The output is a .config file used in the position builder.
    Args:
        entries: <array> array with the layout (text, text)
    '''
    with open('Params.config', 'w') as outfile:
        out_dict = {}
        for entry in entries:
            field = entry[0]
            text = entry[1].get()
            out_dict[field] = text
        json.dump(out_dict, outfile, indent=2)


def make_window(fields):
    '''
    '''
    root = tk.Tk()
    ents = make_form(root, fields)
    b1 = tk.Button(root, text='Show', command=(lambda e=ents: show(e)))
    b1.pack(side=tk.RIGHT, padx=5, pady=5)
    b2 = tk.Button(root, text='Quit', command=root.quit)
    b2.pack(side=tk.LEFT, padx=5, pady=5)
    b3 = tk.Button(root, text='Save', command=(lambda e=ents: save(e)))
    b3.pack(side=tk.RIGHT, padx=5, pady=5)
    root.mainloop()
