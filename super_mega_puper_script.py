import tkinter as tk
from tkinter import messagebox
import psutil

def check_ram():
    ram = psutil.virtual_memory()
    usage = ram.percent
    
    status_label.config(text=f"текущая память: {usage}%")

    if usage > 60:
        messagebox.showwarning(
            "Воу щит! память как оказалось перегружена",
            f"предупреждение! использование оперативной памяти превысило 60%!\nиспользуется: {usage}%"
        )
    else:
        messagebox.showinfo(
            "все ок",
            f"использование памяти в норме.\nиспользуется: {usage}%"
        )

# это типо Main окно
root = tk.Tk()
root.title("SUPER MEGA SIGMA ULTRA PRO VIP PLUS RAM MONITOR")
root.geometry("350x200")
root.config(bg="#f0f0f0")

# тут крутой мега заголовок
title_label = tk.Label(root, text="cистемный монитор RAM", font=("Arial", 14, "bold"), bg="#f0f0f0")
title_label.pack(pady=15)

# статус
status_label = tk.Label(root, text="нажмите кнопку для проверки", font=("Arial", 11), bg="#f0f0f0")
status_label.pack(pady=10)

# кнопка
btn = tk.Button(root, text="проверить память", font=("Arial", 11, "bold"), bg="#4CAF50", fg="white", padx=10, pady=5, command=check_ram)
btn.pack(pady=15)

# старт
root.mainloop()