import tkinter as tk
from tkinter import messagebox
import mysql.connector

# Connect to MySQL
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Aanidhay_2004",
    database="message_encoder_decoder"
)
cursor = db.cursor()

def encode_message():
    message = entry.get()
    encoded_message = ""
    for char in message:
        encoded_message += chr(ord(char) + 1)
    encoded_entry.delete(0, tk.END)
    encoded_entry.insert(0, encoded_message)

def decode_message():
    encoded_message = encoded_entry.get()
    decoded_message = ""
    for char in encoded_message:
        decoded_message += chr(ord(char) - 1)
    decoded_entry.delete(0, tk.END)
    decoded_entry.insert(0, decoded_message)

def save_to_database():
    encoded_message = encoded_entry.get()
    decoded_message = decoded_entry.get()

    try:
        cursor.execute("INSERT INTO messages (encoded_message, decoded_message) VALUES (%s, %s)",
                       (encoded_message, decoded_message))
        db.commit()
        messagebox.showinfo("Success", "Message saved to database")
    except Exception as e:
        db.rollback()
        messagebox.showerror("Error", str(e))

# Create GUI
root = tk.Tk()
root.title("Message Encoder & Decoder")

label1 = tk.Label(root, text="Enter Message:")
label1.pack()

entry = tk.Entry(root)
entry.pack()

encode_button = tk.Button(root, text="Encode", command=encode_message)
encode_button.pack()

encoded_entry = tk.Entry(root)
encoded_entry.pack()

decode_button = tk.Button(root, text="Decode", command=decode_message)
decode_button.pack()

decoded_entry = tk.Entry(root)
decoded_entry.pack()

save_button = tk.Button(root, text="Save to Database", command=save_to_database)
save_button.pack()

root.mainloop()
