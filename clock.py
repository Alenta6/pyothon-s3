import tkinter as tk
from datetime import datetime

def update_clock():
    now = datetime.now()
    time_string = now.strftime("%H:%M:%S")
    date_string = now.strftime("%Y-%m-%d")
    day_string = now.strftime("%A")
    
    time_label.config(text=time_string)
    date_label.config(text=date_string)
    day_label.config(text=day_string)
    
    root.after(1000, update_clock)

root = tk.Tk()
root.title("Digital Clock")
root.attributes('-fullscreen', True)
root.configure(bg='black')
font_large = ("Helvetica", 80, "bold")
font_small = ("Helvetica", 30)
frame = tk.Frame(root, bg='black')
frame.place(relx=0.5, rely=0.5, anchor='center')
time_label = tk.Label(frame, font=font_large, fg="lime", bg="black")
time_label.pack(pady=10)
date_label = tk.Label(frame, font=font_small, fg="cyan", bg="black")
date_label.pack()
day_label = tk.Label(frame, font=font_small, fg="yellow", bg="black")
day_label.pack()

update_clock()
root.mainloop()



