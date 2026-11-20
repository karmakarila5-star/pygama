import tkinter as tk

def update_message():
    user_name = name_box.get().strip()
    
    if user_name == "":
        user_name = "Participant"
        
    workshop_date = "November 25, 2026"
    
    welcome_msg = (
        f"Hello {user_name}!\n\n"
        f"Welcome to the Python Programming Workshop.\n"
        f"Date: {workshop_date}\n\n"
        f"We are excited to have you join us today. Please get your laptop ready!"
    )
    
    output_box.config(state="normal")
    output_box.delete("1.0", tk.END)
    output_box.insert(tk.END, welcome_msg)
    output_box.config(state="disabled")

window = tk.Tk()
window.title("Workshop Greeting App")
window.geometry("420x350")
window.configure(padx=20, pady=20)

instruction_lbl = tk.Label(
    window, 
    text="Enter participant's name below to generate a welcome message:",
    font=("Arial", 10)
)
instruction_lbl.pack(anchor="w", pady=(0, 8))

name_box = tk.Entry(window, width=35, font=("Arial", 11))
name_box.pack(anchor="w", pady=(0, 10))

submit_btn = tk.Button(
    window, 
    text="Show Welcome Message", 
    command=update_message,
    bg="#e0e0e0",
    font=("Arial", 10, "bold")
)
submit_btn.pack(anchor="w", pady=(0, 15))

output_lbl = tk.Label(window, text="Workshop Greeting:", font=("Arial", 10))
output_lbl.pack(anchor="w", pady=(0, 5))

output_box = tk.Text(window, height=8, width=45, font=("Arial", 10), wrap="word")
output_box.pack(anchor="w")
output_box.config(state="disabled")

window.mainloop()
