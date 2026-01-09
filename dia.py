import random
import time
import threading
import tkinter as tk

root = tk.Tk()
root.withdraw()  # hide main window

screen_w = root.winfo_screenwidth()
screen_h = root.winfo_screenheight()

def place_windows():
    while True:
        win = tk.Toplevel(root)
        win.overrideredirect(True)
        win.attributes("-topmost", True)

        x = random.randint(0, screen_w - 300)
        y = random.randint(0, screen_h - 60)
        win.geometry(f"300x60+{x}+{y}")

        label = tk.Label(
            win,
            text="you got hacked",
            fg="black",
            bg="white",
            font=("Arial", 14, "bold")
        )
        label.place(relx=0.5, rely=0.5, anchor="center")

        time.sleep(0.1)  # fixed indentation

threading.Thread(target=place_windows, daemon=True).start()

root.mainloop()