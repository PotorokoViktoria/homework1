import pandas as pd
import random
import tkinter as tk
from tkinter import ttk, messagebox

def get_all_genres():
    films = pd.read_csv('imdb_top_250.csv')
    all_genres = []
    for genre_str in films['Genre'].dropna():
        if isinstance(genre_str, str):
            genres = genre_str.split(' | ')
            all_genres.extend(genres)
    return sorted(set(all_genres))

def get_random_film_by_genre(genre):
    films = pd.read_csv('imdb_top_250.csv')
    matching_films = []
    for index, row in films.iterrows():
        if pd.isna(row['Genre']) or not isinstance(row['Genre'], str):
            continue
        film_genres = row['Genre'].split(' | ')
        if genre in film_genres:
            matching_films.append(row)
    return matching_films
def find_and_show_film():
    genre = genre_var.get()
    if not genre:
        messagebox.showwarning("Ошибка", "Выберите жанр!")
        return
    
    films = get_random_film_by_genre(genre)
    if not films:
        messagebox.showinfo("Результат", "Фильмы не найдены!")
        return

    
    film = random.choice(films)
    result_text.delete(1.0, tk.END)
    result_text.insert(tk.END, f"{film['Title']} ({film['Year']})\n\n")
    result_text.insert(tk.END, f"Рейтинг: {film['IMDB rating']}\n")
    result_text.insert(tk.END, f"Жанры: {film['Genre']}\n")
    result_text.insert(tk.END, f"Режиссер: {film['Director']}\n")
    result_text.insert(tk.END, f"Длительность: {film['Duration']}")

root = tk.Tk()
root.title("filmoteka")
root.geometry("500x400")

tk.Label(root, text="Выберите жанр фильма:", font=("Arial", 12)).pack(pady=10)

genre_var = tk.StringVar()
genres = get_all_genres()
genre_combo = ttk.Combobox(root, textvariable=genre_var, values=genres, state="readonly")
genre_combo.pack(pady=5)

tk.Button(root, text="Найти фильм", command=find_and_show_film, font=("Arial", 11)).pack(pady=10)

result_text = tk.Text(root, height=10, width=50, font=("Arial", 10))
result_text.pack(pady=10, padx=20, fill="both", expand=True)

root.mainloop()