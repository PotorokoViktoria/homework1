import tkinter as tk

def hex_to_dec(hex_str):
    return int(hex_str, 16)

def dec_to_hex(dec_num):
    hex_str = hex(dec_num)[2:].upper()
    return hex_str.zfill(2)

def calculate_complementary_color():
    color_hex = entry.get().strip().upper()
    
    if not color_hex.startswith('#'):
        color_hex = '#' + color_hex
    
    r_hex = color_hex[1:3]
    g_hex = color_hex[3:5]
    b_hex = color_hex[5:7]
    
    r_dec = hex_to_dec(r_hex)
    g_dec = hex_to_dec(g_hex)
    b_dec = hex_to_dec(b_hex)
    
    r_comp_dec = 255 - r_dec
    g_comp_dec = 255 - g_dec
    b_comp_dec = 255 - b_dec
    
    r_comp_hex = dec_to_hex(r_comp_dec)
    g_comp_hex = dec_to_hex(g_comp_dec)
    b_comp_hex = dec_to_hex(b_comp_dec)
    
    complementary_color = f"#{r_comp_hex}{g_comp_hex}{b_comp_hex}"
    
    update_color_display(color_hex, complementary_color)

def update_color_display(color1, color2):
    canvas1.config(bg=color1)
    canvas2.config(bg=color2)

root = tk.Tk()
root.title("Подбор противоположного цвета")
root.geometry("400x300")

main_frame = tk.Frame(root, padx=20, pady=20)
main_frame.pack(fill="both", expand=True)

tk.Label(main_frame, text="Калькулятор противоположного цвета", 
         font=("Arial", 14, "bold")).pack(pady=10)

tk.Label(main_frame, text="Введите цвет в формате #XXYYZZ:", 
         font=("Arial", 10)).pack(pady=5)

input_frame = tk.Frame(main_frame)
input_frame.pack(pady=10)

entry = tk.Entry(input_frame, font=("Arial", 12), width=15)
entry.pack(side="left", padx=5)

tk.Button(input_frame, text="Рассчитать", command=calculate_complementary_color, 
          font=("Arial", 10), bg="#4CAF50", fg="white").pack(side="left", padx=5)

colors_frame = tk.Frame(main_frame)
colors_frame.pack(pady=20)

canvas1 = tk.Canvas(colors_frame, width=120, height=120, bg="white", relief="solid", bd=2)
canvas1.grid(row=0, column=0, padx=10)

canvas2 = tk.Canvas(colors_frame, width=120, height=120, bg="white", relief="solid", bd=2)
canvas2.grid(row=0, column=1, padx=10)

tk.Label(colors_frame, text="Исходный цвет", font=("Arial", 10)).grid(row=1, column=0)
tk.Label(colors_frame, text="Подходящий цвет", font=("Arial", 10)).grid(row=1, column=1)

root.mainloop()