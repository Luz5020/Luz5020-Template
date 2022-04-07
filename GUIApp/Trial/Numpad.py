import tkinter as tk

import GenerateNames as Gn


# Button Functions
def btn_0_press():
    lbl_out["text"] = "0"


def btn_1_press():
    lbl_out["text"] = "1"


def btn_2_press():
    lbl_out["text"] = "2"


def btn_3_press():
    lbl_out["text"] = "3"


def btn_4_press():
    lbl_out["text"] = "4"


def btn_5_press():
    lbl_out["text"] = "5"


def btn_6_press():
    lbl_out["text"] = "6"


def btn_7_press():
    lbl_out["text"] = "7"


def btn_8_press():
    lbl_out["text"] = "8"


def btn_9_press():
    lbl_out["text"] = "9"


# Main Window
window = tk.Tk()
window.title(Gn.GenName())
frm_main = tk.Frame(master=window, relief=tk.RAISED, borderwidth=1)
# Define Buttons
btn_0 = tk.Button(
    master=frm_main,
    text="0",
    command=btn_0_press
)
btn_1 = tk.Button(
    master=frm_main,
    text="1",
    command=btn_1_press
)
btn_2 = tk.Button(
    master=frm_main,
    text="2",
    command=btn_2_press
)
btn_3 = tk.Button(
    master=frm_main,
    text="3",
    command=btn_3_press
)
btn_4 = tk.Button(
    master=frm_main,
    text="4",
    command=btn_4_press
)
btn_5 = tk.Button(
    master=frm_main,
    text="5",
    command=btn_5_press
)
btn_6 = tk.Button(
    master=frm_main,
    text="6",
    command=btn_6_press
)
btn_7 = tk.Button(
    master=frm_main,
    text="7",
    command=btn_7_press
)
btn_8 = tk.Button(
    master=frm_main,
    text="8",
    command=btn_8_press
)
btn_9 = tk.Button(
    master=frm_main,
    text="9",
    command=btn_9_press
)
# Output Window
frm_out = tk.Frame(master=window, relief=tk.GROOVE, borderwidth=2)
lbl_out = tk.Label(master=frm_out, text="     ")
# Main Render-group
frm_main.grid(row=0, column=0)
btn_0.grid(row=0, column=0)
btn_1.grid(row=0, column=1)
btn_2.grid(row=0, column=2)
btn_3.grid(row=1, column=0)
btn_4.grid(row=1, column=1)
btn_5.grid(row=1, column=2)
btn_6.grid(row=2, column=0)
btn_7.grid(row=2, column=1)
btn_8.grid(row=2, column=2)
btn_9.grid(row=3, column=0)
frm_out.grid(row=0, column=3, sticky="n")
lbl_out.grid(row=0, column=3, sticky="n")
# Run
window.mainloop()
