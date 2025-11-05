import tkinter as tk
from tkinter import messagebox

def calculate():
    expression = entry.get()
    result = eval(expression)
    result_label.config(text=f"Результат: {result}")
        
def clear_all():
    entry.delete(0, tk.END)
    result_label.config(text="Результат: ")

root = tk.Tk()
root.title("Калькулятор")
root.geometry("400x200")

title_label = tk.Label(root, text="Введите математическое выражение:", font=('Arial', 12))
title_label.pack(pady=10) 

entry = tk.Entry(root, font=('Arial', 14), justify='center', width=30)
entry.pack(pady=5) 

button_frame = tk.Frame(root)
button_frame.pack(pady=10)  

calculate_btn = tk.Button(button_frame, text="Вычислить", font=('Arial', 12),
                         command=calculate, bg='lightgreen', width=10)
calculate_btn.pack(side=tk.LEFT, padx=5)

result_label = tk.Label(root, text="Результат: ", font=('Arial', 14, 'bold'),
                       fg='blue')
result_label.pack(pady=15)

root.mainloop()