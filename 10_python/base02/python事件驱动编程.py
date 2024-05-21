#!/usr/bin/env python
# -*- coding : utf-8 -*-
import tkinter as tk

def on_button_click():
    print("Button clicked!")

app = tk.Tk()
button = tk.Button(app, text="Click Me", command=on_button_click)
button.pack()
app.mainloop()