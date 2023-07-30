from alphabets import *

import tkinter as tk


def convert_to_morse():
    # Take user text
    user_text = text_entry.get().upper()
    # Check position of each letter of user text
    morse_message = " "
    for char in user_text:
        if char in text_alphabet:
            position = text_alphabet.index(char)
            # Use the position to get a corresponding character in morse alphabet
            coded_letter = morse_code_alphabet[position]
            morse_message += coded_letter + " "
        else:
            print(f"Sorry, the character {char} is not in the alphabet!")
    morse_output.delete("1.0", tk.END)  # Clear previous content
    morse_output.insert(tk.END, morse_message)


def clear_screen():
    text_entry.delete(0, tk.END)
    morse_output.delete("1.0", tk.END)
    converted_text.config(text="Converted Morse Code: ")


# tkinter window
window = tk.Tk()
window.geometry("400x300")
window.title("Text-Morse Code Converter")

# Text input
text_label = tk.Label(window, text="Enter the text:")
text_label.pack()

text_entry = tk.Entry(window)
text_entry.pack()

# Convert button
convert_button = tk.Button(window, text="Convert", command=convert_to_morse)
convert_button.pack()

# Converted text label
converted_text = tk.Label(window, text="Morse Code: ")
converted_text.pack()

# Morse code output
morse_output = tk.Text(window, wrap="word", width=40, height=8)
morse_output.pack()

# Clear button
clear_button = tk.Button(window, text="Clear", command=clear_screen)
clear_button.pack()

window.mainloop()
