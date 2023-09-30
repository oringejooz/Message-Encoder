from tkinter import *


root = Tk()
root.geometry("500x300")
root.resizable(0,0)
root.title("Decoder Python World and Encoder")

# Custom Fonts
custom_font_title = ("Helvetica", 20, "bold")
custom_font_label = ("Helvetica", 12)
custom_font_button = ("Helvetica", 10, "bold")

# Background Colors
bg_color = "lightgray"
button_bg_color = "lightblue"
button_fg_color = "white"


Label(root, text="ENCODE DECODE", font=custom_font_title).pack()
Label(root, text="Python World", font=custom_font_title, fg="blue").pack(side=BOTTOM)

Text = StringVar()
Result = StringVar()

def Encode(message):
        encoded = ""
        for char in message:
            encoded += chr(ord(char) + 1)  # Caesar cipher with a shift of 1
        return encoded

def Decode(encoded_message):
    decoded = ""
    for char in encoded_message:
        decoded += chr(ord(char) - 1)  # Reverse the Caesar cipher
    return decoded

def Mode():
    input_text = Text.get()
    encoded_text = Encode(input_text)
    Result.set(encoded_text)

def DecodeText():
    encoded_text = Text.get()
    decoded_text = Decode(encoded_text)
    Result.set(decoded_text)

def Exit():
    root.destroy()

def Reset():
    Text.set("")
    Result.set("")

Label(root, font="arial 12 bold", text="MESSAGE").place(x=60, y=60)
Entry(root, font="arial 10", textvariable=Text, bg="ghost white").place(x=290, y=60)

Entry(root, font="arial 10 bold", textvariable=Result, bg="ghost white").place(x=290, y=150)

Button(root, font="arial 10 bold", text="ENCODE", command=Mode, bg="LightGrey", padx=2).place(x=60, y=150)
Button(root, font="arial 10 bold", text="DECODE", command=DecodeText, bg="LightGrey", padx=2).place(x=60, y=190)
Button(root, font="arial 10 bold", text="RESET", width=6, command=Reset, bg="LimeGreen", padx=2).place(x=80, y=230)
Button(root, font="arial 10 bold", text="EXIT", width=6, command=Exit, bg="OrangeRed", padx=2, pady=2).place(x=180, y=230)

root.mainloop()
