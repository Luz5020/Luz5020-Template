#  Copyright (c) 2022. luz5020
#  Approved for use in Open Source Projects
import random
import tkinter as tk

import pandas as pd


# Methods
def namegen():
    col_list = ["yr", "sex", "FirstForename", "number", "rank", "position"]
    df = pd.read_csv("../NameGen(m)/Names_Short_M.csv", usecols=col_list)
    for x in df.index:
        if df.loc[x, "yr"] < 2010:
            df.drop(x, inplace=True)
    dl = df['FirstForename'].tolist()
    n = random.randint(0, len(dl))
    # print(dl[n])
    name = dl[n]
    lbl_name["text"] = name


# Graphical Init
window = tk.Tk()
window.title("Name Generator(m)")
frm_btn = tk.Frame(master=window)
frm_out = tk.Frame(master=window)
for i in range(2):
    window.columnconfigure(i, weight=1, minsize=75)
    window.rowconfigure(i, weight=1, minsize=10)
btn_gen = tk.Button(
    master=frm_btn,
    text="Generate",
    command=namegen
)
lbl_name = tk.Label(master=frm_out, text="Generated Name")
# Placement
frm_btn.grid(row=0, column=0, padx=2)
btn_gen.grid(row=0, column=0, padx=2)
frm_out.grid(row=0, column=1, padx=4)
lbl_name.grid(row=0, column=1, padx=4)
# Draw
window.mainloop()
