import math
import tkinter as tk

def clk(key):
    if(key == "="):
        if("/" in entry.get() and "." not in entry.get()):
            entry.insert(tk.END, ".0")
        string1 = "-+0123456789."

        if(entry.get()[0] not in string1):
            entry.insert(tk.END, "Char not in " + string1)

        try:
            result = eval(entry.get())
            entry.insert(tk.END, " = " + str(result))
        except:
            entry.insert(tk.END, " ERROR")
    elif(key == "C"):
        entry.delete(0, tk.END)
    elif(key == "->M"):
        memory = entry.get()
        if("=" in memory):
            x = memory.find("=")
            memory = memory[x + 2:]
        root.title("M=" + memory)
    elif(key == "M->"):
        entry.insert(tk.END, memory)
    elif(key == "neg"):
        if("=" in entry.get()):
            entry.delete(0, tk.END)
        try:
            if(entry.get()[0] == "-"):
                entry.delete(0)
            else: entry.insert(0, "-")
        except IndexError:
            pass
    else:
        if("=" in entry.get()):
            entry.delete(0, tk.END)
        entry.insert(tk.END, key)
