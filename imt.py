import tkinter as tk
from tkinter import ttk

class BMICalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Калькулятор ИМТ")
        self.root.geometry("400x300")
        self.root.resizable(False, False)
        
        main_frame = ttk.Frame(root, padding="20")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        title_label = ttk.Label(main_frame, text="Калькулятор Индекса Массы Тела", 
                               font=("Arial", 14, "bold"))
        title_label.grid(row=0, column=0, columnspan=2, pady=(0, 20))
        
        ttk.Label(main_frame, text="Вес (кг):").grid(row=1, column=0, sticky=tk.W, pady=5)
        self.weight_entry = ttk.Entry(main_frame, width=15)
        self.weight_entry.grid(row=1, column=1, sticky=tk.W, pady=5)
        
        ttk.Label(main_frame, text="Рост (см):").grid(row=2, column=0, sticky=tk.W, pady=5)
        self.height_entry = ttk.Entry(main_frame, width=15)
        self.height_entry.grid(row=2, column=1, sticky=tk.W, pady=5)

        self.calculate_button = ttk.Button(main_frame, text="Рассчитать ИМТ", 
                                          command=self.calculate_bmi)
        self.calculate_button.grid(row=3, column=0, columnspan=2, pady=15)

        ttk.Label(main_frame, text="Результат:").grid(row=4, column=0, sticky=tk.W, pady=5)
        self.result_label = ttk.Label(main_frame, text="", font=("Arial", 12, "bold"))
        self.result_label.grid(row=4, column=1, sticky=tk.W, pady=5)
        
        ttk.Label(main_frame, text="Интерпретация:").grid(row=5, column=0, sticky=tk.W, pady=5)
        self.interpretation_label = ttk.Label(main_frame, text="", wraplength=300)
        self.interpretation_label.grid(row=5, column=1, sticky=tk.W, pady=5)
        
        self.root.bind('<Return>', lambda event: self.calculate_bmi())
    
    def calculate_bmi(self):
        weight = float(self.weight_entry.get().replace(',', '.'))
        height_cm = float(self.height_entry.get().replace(',', '.'))
           
        height_m = height_cm / 100
        bmi = weight / (height_m ** 2)
        bmi_rounded = round(bmi, 1)

        category, color = self.get_bmi_category(bmi_rounded)

        self.result_label.config(text=f"{bmi_rounded}", foreground=color)
        self.interpretation_label.config(text=category, foreground=color)
    
    def get_bmi_category(self, bmi):
        if bmi < 16:
            return "Выраженный дефицит массы тела", "red"
        elif 16 <= bmi < 18.5:
            return "Недостаточная (дефицит) масса тела", "orange"
        elif 18.5 <= bmi < 25:
            return "Норма", "green"
        elif 25 <= bmi < 30:
            return "Избыточная масса тела (предожирение)", "orange"
        elif 30 <= bmi < 35:
            return "Ожирение 1 степени", "red"
        elif 35 <= bmi < 40:
            return "Ожирение 2 степени", "red"
        else:
            return "Ожирение 3 степени", "darkred"

root = tk.Tk()
app = BMICalculator(root)
root.mainloop()