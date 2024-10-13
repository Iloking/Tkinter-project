import tkinter as tk
import random
import string

# Function to generate a random password
def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

# Function to handle button click and display the generated password
def on_generate_click():
    password_length = 12  # You can adjust this as needed
    password = generate_password(password_length)
    password_label.config(text=f"Generated Password: {password}")

# Create the Tkinter window
root = tk.Tk()
root.geometry("400x200")
root.title("Random Password Generator")

# Label to display the password
password_label = tk.Label(root, text="Generated Password will appear here", bg="lightblue", fg="black")
password_label.pack(pady=20)

# Button to generate a new password
generate_button = tk.Button(root, text="Generate Password", command=on_generate_click)
generate_button.pack(pady=10)

# Run the Tkinter event loop
root.mainloop()
