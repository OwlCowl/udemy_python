import tkinter as tk
from tkinter import ttk

def greet():
    print(f"Hello, {username.get() or 'World'}")

root = tk.Tk()
root.title('Hello')

#frame

main = ttk.Frame(root)
main.pack(side='right', fill='both', expand=True)

#should be put into the method
username = tk.StringVar()

#create label
nameLabel = ttk.Label(root, text='Name')
nameLabel.pack(side='left', padx=(0, 10))

nameEntry = ttk.Entry(root, width=15, textvariable=username)
nameEntry.pack(side='left')
nameEntry.focus()

greetButton = ttk.Button(main, text='Greet', command=greet)
greetButton.pack(side='left', fill='x', expand=True)

quitButton = ttk.Button(main, text="Quit", command=root.destroy)
quitButton.pack(side='right', fill='x', expand=True)


root.mainloop()