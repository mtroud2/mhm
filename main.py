import tkinter as tk
from tkinter import ttk

root = tk.Tk()

lable = tk.Label(root, text="Hello World")
lable.pack()
root.geometry("400x400")
root.title("mtroud")
def click_Me():
    print("الله اكبر")
clk_BUTTON = tk.Button(root, text="تسبيح", command=click_Me)
clk_BUTTON.pack()

root.mainloop()
