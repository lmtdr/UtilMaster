import tkinter as tk
import sys
import os
import shutil
from tkinter import Tk, Label, filedialog
from PIL import Image, ImageTk

# Load template.txt
def get_template_file():
    try:

        script_dir = os.path.dirname(os.path.abspath(sys.argv[0]))
        template_file = os.path.join(script_dir, "template.txt")
        
        with open(template_file, 'r') as file:
            return template_file
            
    except FileNotFoundError:
        
        script_dir = os.path.dirname(os.path.abspath(__file__))
        template_file = os.path.join(script_dir, "template.txt")
        return template_file
        
# Managing input forms    
def write_to_file():

    input1 = entry1.get()
    input2 = entry2.get()
    input3 = entry3.get()
    input4 = entry4.get()
    input5 = entry5.get()
    input6 = entry6.get()
    input7 = entry7.get()
    input8 = entry8.get()
    
    template_file = get_template_file()
    with open(template_file, "r") as file:
        template_text = file.read()
        
        output_text = template_text.format(input1=input1, input2=input2, input3=input3, input4=input4, input5=input5, input6=input6, input7=input7, input8=input8)

    # Open file dialog to choose the save location
    file_path = filedialog.asksaveasfilename(defaultextension=".cfg", filetypes=(("Config files", "*.cfg"), ("All files", "*.*")))
    if file_path:
        file_name = os.path.basename(file_path)  # Extract only the file name without the path
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(output_text)
        result_label.config(text=f"Config {file_name}\nwas created!")
    else:
        result_label.config(text="Not saved!")
        
# Function to clear the placeholder text on entry click
def on_entry_click(event):
    entry = event.widget
    if entry.get() == entry.placeholder_text:
        entry.delete(0, tk.END)
        entry.config(fg="black")

# Function to restore the placeholder text on focus loss
def on_focus_loss(event):
    entry = event.widget
    if entry.get() == "":
        entry.insert(0, entry.placeholder_text)
        entry.config(fg="gray")
        
# Create the main window
window = tk.Tk()
script_dir = os.path.dirname(os.path.abspath(__file__))
icon_path = os.path.join(script_dir, "favicon.ico")
window.title("UtilMaster by czMarv")
window.iconbitmap(icon_path)
window.geometry("500x600")  # Set the window size
window.resizable(False, False)  # Disable window resizing

# Load the background image
image_path = os.path.join(script_dir, "background.png")
image = Image.open(image_path)
photo = ImageTk.PhotoImage(image)
background_label = Label(window, image=photo)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

# Placeholder text for the entry fields
placeholder_text_1 = "Your key"

# Frame positioning collumn 1
frame1 = tk.Frame(window, bd=2, relief="solid", bg="IndianRed4")
frame1.pack(side="left", anchor="sw", padx=10, pady=10)

# Frame positioning collumn 2
frame2 = tk.Frame(window, bd=2, relief="solid", bg="IndianRed4")
frame2.pack(side="right", anchor="se", padx=10, pady=10)

# Frame positioning collumn 3
frame3 = tk.Frame(window, relief="solid", bg="black")
frame3.pack(side="bottom", anchor="s", padx=0, pady=10)

# Label 1
text_label = tk.Label(frame1, text="bind for moly", font=("Arial", 12, "bold"), fg="gold", bg="IndianRed4", relief="raised", borderwidth=4)
text_label.pack(fill="both", expand=True)

# Entry 1
entry1 = tk.Entry(frame1, width=14, font=("Arial", 12), justify='center', fg="grey")
entry1.placeholder_text = placeholder_text_1
entry1.insert(0, entry1.placeholder_text)
entry1.bind("<FocusIn>", on_entry_click)
entry1.bind("<FocusOut>", on_focus_loss)
entry1.pack()

# Label 2
text_label = tk.Label(frame1, text="bind for smoke", font=("Arial", 12, "bold"), fg="gold", bg="IndianRed4", relief="raised", borderwidth=4)
text_label.pack(fill="both", expand=True)

# Entry 2
entry2 = tk.Entry(frame1, width=14, font=("Arial", 12), justify='center', fg="gray44")
entry2.placeholder_text = placeholder_text_1
entry2.insert(0, entry2.placeholder_text)
entry2.bind("<FocusIn>", on_entry_click)
entry2.bind("<FocusOut>", on_focus_loss)
entry2.pack()

# label 3
text_label = tk.Label(frame1, text="bind for flash", font=("Arial", 12, "bold"), fg="gold", bg="IndianRed4", relief="raised", borderwidth=4)
text_label.pack(fill="both", expand=True)

# Entry 3
entry3 = tk.Entry(frame1, width=14, font=("Arial", 12), justify='center', fg="gray44")
entry3.placeholder_text = placeholder_text_1
entry3.insert(0, entry3.placeholder_text)
entry3.bind("<FocusIn>", on_entry_click)
entry3.bind("<FocusOut>", on_focus_loss)
entry3.pack()

# Label 4
text_label = tk.Label(frame1, text="bind for nade", font=("Arial", 12, "bold"), fg="gold", bg="IndianRed4", relief="raised", borderwidth=4)
text_label.pack(fill="both", expand=True)

# Entry 4
entry4 = tk.Entry(frame1, width=14, font=("Arial", 12), justify='center', fg="gray44")
entry4.placeholder_text = placeholder_text_1
entry4.insert(0, entry4.placeholder_text)
entry4.bind("<FocusIn>", on_entry_click)
entry4.bind("<FocusOut>", on_focus_loss)
entry4.pack()

# Label 5
text_label = tk.Label(frame1, text="bind for decoy", font=("Arial", 12, "bold"), fg="gold", bg="IndianRed4", relief="raised", borderwidth=4)
text_label.pack(fill="both", expand=True)

# Entry 5
entry5 = tk.Entry(frame1, width=14, font=("Arial", 12), justify='center', fg="gray44")
entry5.placeholder_text = placeholder_text_1
entry5.insert(0, entry5.placeholder_text)
entry5.bind("<FocusIn>", on_entry_click)
entry5.bind("<FocusOut>", on_focus_loss)
entry5.pack()

# Label 6
text_label = tk.Label(frame2, text="+ for buy", font=("Arial", 12, "bold"), fg="gold", bg="IndianRed4", relief="raised", borderwidth=4)
text_label.pack(fill="both", expand=True)

# Entry 6
entry6 = tk.Entry(frame2, width=14, font=("Arial", 12), justify='center', fg="gray44")
entry6.placeholder_text = placeholder_text_1
entry6.insert(0, entry6.placeholder_text)
entry6.bind("<FocusIn>", on_entry_click)
entry6.bind("<FocusOut>", on_focus_loss)
entry6.pack()

# Label 7
text_label = tk.Label(frame2, text="+ for drop", font=("Arial", 12, "bold"), fg="gold", bg="IndianRed4", relief="raised", borderwidth=4)
text_label.pack(fill="both", expand=True)

# Entry 7
entry7 = tk.Entry(frame2, width=14, font=("Arial", 12), justify='center', fg="gray44")
entry7.placeholder_text = placeholder_text_1
entry7.insert(0, entry7.placeholder_text)
entry7.bind("<FocusIn>", on_entry_click)
entry7.bind("<FocusOut>", on_focus_loss)
entry7.pack()

# Label 8
text_label = tk.Label(frame2, text="+ for give", font=("Arial", 12, "bold"), fg="gold", bg="IndianRed4", relief="raised", borderwidth=4)
text_label.pack(fill="both", expand=True)

# Entry 8
entry8 = tk.Entry(frame2, width=14, font=("Arial", 12), justify='center', fg="gray44")
entry8.placeholder_text = placeholder_text_1
entry8.insert(0, entry8.placeholder_text)
entry8.bind("<FocusIn>", on_entry_click)
entry8.bind("<FocusOut>", on_focus_loss)
entry8.pack()

# Create a button to write the inputs to a file
save_button = tk.Button(frame3, text="Save Config", bg="green", width=444, height=2, command=write_to_file)
save_button.pack(padx=10, pady=10)

# Create the result label
result_label = tk.Label(window, fg="orange", bg="black")
result_label.pack(padx=10, pady=30)

# Start the main loop
window.mainloop()
