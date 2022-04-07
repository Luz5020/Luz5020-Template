#  Copyright (c) 2022. luz5020
#  Approved for use in Open Source Projects
import tkinter as tk


# Methods

def calc_add():
    try:
        add_1 = int(ent_add_1.get())
        add_2 = int(ent_add_2.get())
        lbl_add_result["text"] = add_1 + add_2
    except ValueError:
        lbl_add_result["text"] = "ValueError"


def calc_sub():
    try:
        sub_1 = int(ent_sub_1.get())
        sub_2 = int(ent_sub_2.get())
        lbl_sub_result["text"] = sub_1 - sub_2
    except ValueError:
        lbl_sub_result["text"] = "ValueError"


def calc_mut():
    try:
        mut_1 = int(ent_mut_1.get())
        mut_2 = int(ent_mut_2.get())
        lbl_mut_result["text"] = mut_1 * mut_2
    except ValueError:
        lbl_mut_result["text"] = "ValueError"


def calc_div():
    try:
        div_1 = int(ent_div_1.get())
        div_2 = int(ent_div_2.get())
        if div_2 != 0:
            lbl_div_result["text"] = div_1 / div_2
        else:
            lbl_div_result["text"] = "Syntax Error"
    except ValueError:
        lbl_div_result["text"] = "ValueError"


# Graphical Init
# General
window = tk.Tk()
window.title("Calculator")
frm_add = tk.Frame(master=window)
frm_div = tk.Frame(master=window)
frm_multi = tk.Frame(master=window)
frm_sub = tk.Frame(master=window)
for i in range(4):
    window.columnconfigure(i, weight=1, minsize=25)
    window.rowconfigure(i, weight=1, minsize=50)
# Addition
ent_add_1 = tk.Entry(master=frm_add, width=5)
ent_add_2 = tk.Entry(master=frm_add, width=5)
lbl_add_symbol = tk.Label(master=frm_add, text="+")
btn_add = tk.Button(
    master=frm_add,
    text="Calculate",
    command=calc_add
)
lbl_add_result = tk.Label(master=frm_add, text="0")
# Subtraction
ent_sub_1 = tk.Entry(master=frm_sub, width=5)
ent_sub_2 = tk.Entry(master=frm_sub, width=5)
lbl_sub_symbol = tk.Label(master=frm_sub, text="-")
btn_sub = tk.Button(
    master=frm_sub,
    text="Calculate",
    command=calc_sub
)
lbl_sub_result = tk.Label(master=frm_sub, text="0")
# Multiplication
ent_mut_1 = tk.Entry(master=frm_multi, width=5)
ent_mut_2 = tk.Entry(master=frm_multi, width=5)
lbl_mut_symbol = tk.Label(master=frm_multi, text="*")
btn_mut = tk.Button(
    master=frm_multi,
    text="Calculate",
    command=calc_mut
)
lbl_mut_result = tk.Label(master=frm_multi, text="0")
# Division
ent_div_1 = tk.Entry(master=frm_div, width=5)
ent_div_2 = tk.Entry(master=frm_div, width=5)
lbl_div_symbol = tk.Label(master=frm_div, text="/")
btn_div = tk.Button(
    master=frm_div,
    text="Calculate",
    command=calc_div
)
lbl_div_result = tk.Label(master=frm_div, text="0")
# Placement
# Addition
frm_add.grid(row=0, column=0, padx=5)
ent_add_1.grid(row=0, column=0, padx=5)
lbl_add_symbol.grid(row=0, column=1, padx=5)
ent_add_2.grid(row=0, column=2, padx=5)
btn_add.grid(row=0, column=3, padx=5)
lbl_add_result.grid(row=0, column=4, padx=5)
# Subtraction
frm_sub.grid(row=1, column=0, padx=5)
ent_sub_1.grid(row=1, column=0, padx=5)
lbl_sub_symbol.grid(row=1, column=1, padx=5)
ent_sub_2.grid(row=1, column=2, padx=5)
btn_sub.grid(row=1, column=3, padx=5)
lbl_sub_result.grid(row=1, column=4, padx=5)
# Multiplication
frm_multi.grid(row=2, column=0, padx=5)
ent_mut_1.grid(row=2, column=0, padx=5)
lbl_mut_symbol.grid(row=2, column=1, padx=5)
ent_mut_2.grid(row=2, column=2, padx=5)
btn_mut.grid(row=2, column=3, padx=5)
lbl_mut_result.grid(row=2, column=4, padx=5)
# Division
frm_div.grid(row=3, column=0, padx=5)
ent_div_1.grid(row=3, column=0, padx=5)
lbl_div_symbol.grid(row=3, column=1, padx=5)
ent_div_2.grid(row=3, column=2, padx=5)
btn_div.grid(row=3, column=3, padx=5)
lbl_div_result.grid(row=3, column=4, padx=5)
# Draw
window.mainloop()
