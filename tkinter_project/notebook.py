import os
import tkinter as tk
from tkinter import ttk, filedialog


def create_file(content='', title='Untitled'):
    textArea = tk.Text(notebook)
    textArea.insert("end", content)
    textArea.pack(fill='both', expand=True)
    notebook.add(textArea, text=title)
    notebook.select(textArea)

def file_save():
    filePath = filedialog.asksaveasfile()

    try:
        filename=os.path.basename(filePath)
        textWidget = root.nametowidget(notebook.select())
        content = textWidget.get('1.0', 'end-1c')

        with open(filePath, 'w') as file:
            file.write(content)

    except (AttributeError, FileNotFoundError):
        print('Save operation cancelled')
        return

    notebook.tab("current", text=filename)


def open_file():
    filePath = filedialog.askopenfilename()

    try:
        filename=os.path.basename(filePath)

        with open(filePath, 'r') as file:
            content = file.read()

    except (AttributeError, FileNotFoundError):
        print('Open operation cancelled')
        return

    create_file(content, filename)





root=tk.Tk()
root.title('Yana notebook')
root.option_add('*tearOff', False)

#make a frame
main = ttk.Frame(root)
main.pack(fill='both', expand = True, padx=1, pady=(4,0))

menubar = tk.Menu()
root.config(menu=menubar)

fileMenu = tk.Menu(menubar)
menubar.add_cascade(menu = fileMenu, label='File')
fileMenu.add_command(label='New', command=create_file)
fileMenu.add_command(label='Open...', command=open_file)
fileMenu.add_command(label='Save', command=file_save)

notebook = ttk.Notebook(main)
notebook.pack(fill='both', expand=True)
create_file()

root.mainloop()