from tkinter import *
import base64
import time


def copy_to_clipboard():
    root.clipboard_clear()
    root.clipboard_append(txtService.get())
    root.update()  # Update clipboard
    update_copied_label()

def update_copied_label():
    copied_label.config(text="Copied to clipboard")
    root.after(2000, clear_copied_label)

def clear_copied_label():
    copied_label.config(text="")

def update_time():
    current_time = time.strftime("%Y-%m-%d %H:%M:%S")
    lblInfo.config(text=current_time)
    root.after(1000, update_time)  # Update time every 1000ms (1 second)

root = Tk()
root.geometry("1200x6000")
root.title("Message Encryption and Decryption")


Tops = Frame(root, width=1600, relief=SUNKEN)
Tops.pack(side=TOP)

f1 = Frame(root, width=800, height=700, relief=SUNKEN)
f1.pack(side=LEFT)

localtime = time.asctime(time.localtime(time.time()))

lblInfo = Label(Tops, font=('cursive', 50, 'bold'),
                text="SECRET MESSAGING \nENCRYPT & DECRYPT",
                fg="Black", bd=10, anchor='w')

lblInfo.grid(row=0, column=0)

lblInfo = Label(Tops, font=('arial', 20, 'bold'),
                text=localtime, fg="Steel Blue",
                bd=10, anchor='w')

lblInfo.grid(row=1, column=0)

Msg = StringVar()
mode = StringVar()
Result = StringVar()

def qExit():
    root.destroy()

def Reset():
    Msg.set("")
    mode.set("")
    Result.set("")

lblMsg = Label(f1, font=('arial', 16, 'bold'),
               text="MESSAGE", bd=16, anchor="w")

lblMsg.grid(row=1, column=0)

txtMsg = Entry(f1, font=('arial', 16, 'bold'),
               textvariable=Msg, bd=10, insertwidth=4,
               bg="powder blue", justify='right')

txtMsg.grid(row=1, column=1)

lblmode = Label(f1, font=('arial', 16, 'bold'),
                text="MODE(e for encrypt, d for decrypt)",
                bd=16, anchor="w")

lblmode.grid(row=3, column=0)

txtmode = Entry(f1, font=('arial', 16, 'bold'),
                textvariable=mode, bd=10, insertwidth=4,
                bg="powder blue", justify='right')


txtmode.grid(row=3, column=1)

lblService = Label(f1, font=('arial', 16, 'bold'),
                   text="The Result-", bd=16, anchor="w")

lblService.grid(row=2, column=2)

txtService = Entry(f1, font=('arial', 16, 'bold'),
                   textvariable=Result, bd=10, insertwidth=4,
                   bg="powder blue", justify='right')

txtService.grid(row=2, column=3)

def encode(clear):
    enc = []
    for i in range(len(clear)):
        enc_c = chr((ord(clear[i]) + 3) % 256)
        enc.append(enc_c)
    return base64.urlsafe_b64encode("".join(enc).encode()).decode()

def decode(enc):
    dec = []
    enc = base64.urlsafe_b64decode(enc).decode()
    for i in range(len(enc)):
        dec_c = chr((256 + ord(enc[i]) - 3) % 256)
        dec.append(dec_c)
    return "".join(dec)

def Ref():
    clear = Msg.get()
    m = mode.get()

    if m == 'e':
        Result.set(encode(clear))
    else:
        Result.set(decode(clear))

btnTotal = Button(f1, padx=16, pady=8, bd=16, fg="black",
                  font=('arial', 16, 'bold'), width=10,
                  text="Show Message", bg="powder blue",
                  command=Ref).grid(row=7, column=1)

btnReset = Button(f1, padx=16, pady=8, bd=16,
                  fg="black", font=('arial', 16, 'bold'),
                  width=10, text="Reset", bg="green",
                  command=Reset).grid(row=7, column=2)

btnExit = Button(f1, padx=16, pady=8, bd=16,
                 fg="black", font=('arial', 16, 'bold'),
                 width=10, text="Exit", bg="red",
                 command=qExit).grid(row=7, column=3)

copy_button = Button(f1, padx=16, pady=8, bd=16, fg="black",
                     font=('arial', 16, 'bold'), width=10,
                     text="Copy", bg="yellow",
                     command=copy_to_clipboard)
copy_button.grid(row=7, column=0)

update_time() 

# Add a label for displaying the "Copied to clipboard" message
copied_label = Label(f1, font=('arial', 16, 'bold'), text="", fg="green")
copied_label.grid(row=8, column=0, columnspan=4)

root.mainloop()

