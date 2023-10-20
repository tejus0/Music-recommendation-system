from tkinter import ttk
import tkinter as tk
from tkinter import * 
root1 = tk.Tk()
root1.title("Your Playlist")
root1.configure(bg='black')

""" df = get_results(emotion_code)
cols = list(df.columns)
tree = ttk.Treeview(root1)
tree.pack(side=tk.TOP, fill=tk.X)
tree["columns"] = cols
for k in cols:
    tree.column(k, anchor="w")
    tree.heading(k, text=k, anchor='w')

for index, row in df.iterrows():
    print(list(row))
    tree.insert("", 0,  """ """text=index, values=list(row)) """

pred = tk.Button(root1, text="Play",
                fg="white", bg="black",
                width=20, height=3, activebackground="Red",
                font=('times', 15, ' bold '))
pred.place(x=200, y=500)
root1.mainloop()