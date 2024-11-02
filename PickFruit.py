import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import random
import os

# Listing of 100 different fruits, sorted alphabetically
fruits = sorted([
    "Acerola", "Apple", "Apricot", "Avocado", "Banana", "Bilberry", "Blackberry", "Blackcurrant",
    "Blueberry", "Breadfruit", "Camu Camu", "Cantaloupe", "Cape Gooseberry", "Cherimoya", "Cherry",
    "Clementine", "Cloudberry", "Coconut", "Cranberry", "Custard Apple", "Date", "Dragonfruit", "Durian",
    "Eggfruit", "Feijoa", "Fig", "Gac", "Gac Fruit", "Gooseberry", "Grape", "Grapefruit", "Guava",
    "Hackberry", "Honeydew", "Huckleberry", "Indian Fig", "Jackfruit", "Java Apple", "Jocote", "Jujube",
    "Kiwano", "Kiwi", "Kumquat", "Lemon", "Lilly Pilly", "Lime", "Longan", "Loquat", "Lychee", "Mamey",
    "Mandarin", "Mango", "Mangosteen", "Marionberry", "Medlar", "Miracle Fruit", "Mulberry", "Nectarine",
    "Noni", "Olive", "Orange", "Papaya", "Passionfruit", "Pawpaw", "Peach", "Pear", "Pepino", "Persimmon",
    "Pineapple", "Pineberry", "Pitaya", "Plantain", "Plum", "Pomegranate", "Prickly Pear", "Quince",
    "Raisin", "Rambutan", "Raspberry", "Redcurrant", "Rhubarb", "Salak", "Santol", "Sapodilla",
    "Snake Fruit", "Soursop", "Starfruit", "Strawberry", "Sugar Apple", "Surinam Cherry", "Sweetsop",
    "Tamarillo", "Tamarind", "Tangerine", "Ugli Fruit", "Watermelon", "White Currant", "White Sapote",
    "Yellow Passionfruit", "Yuzu", "Zapote", "Zucchini"
])

collected_fruits = []  # List to keep track of collected fruits


# Function for binary search
def binary_search(fruits, target):
    left, right = 0, len(fruits) - 1
    attempts = 0

    # Converting all fruits to lowercase for case-insensitive search
    fruits_lower = [fruit.lower() for fruit in fruits]

    while left <= right:
        attempts += 1
        mid = (left + right) // 2

        if fruits_lower[mid] == target:
            return mid, attempts
        elif fruits_lower[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1, attempts


# Function to handle the fruit search and collection
def pick_fruit():
    chosen_fruit = entry.get().strip().lower()

    if not chosen_fruit:
        messagebox.showwarning("Input Error", "Please enter the name of a fruit.")
        return

    index, attempts = binary_search(fruits, chosen_fruit)

    if index != -1:
        fruit_name = fruits[index]
        collected_fruits.append(fruit_name)
        update_basket()  # Update the basket display
        mood = mood_entry.get().strip()

        if mood:
            messagebox.showinfo("Fruit Found", f"🎉 We've picked your fruit: {fruit_name}!\n"
                                               f"Description: {mood.capitalize()}\nAttempts: {attempts}")
        else:
            messagebox.showinfo("Fruit Found", f"🎉 We've picked your fruit: {fruit_name}!\nAttempts: {attempts}")

        mood_entry.delete(0, tk.END)  # Clear the mood input

        if len(collected_fruits) >= 5:
            messagebox.showinfo("Fruit Blast!",
                                "🍇🥝🍉 Congratulations! You've collected 5 fruits! Have a fruit blast! 🎉")
            collected_fruits.clear()  # Clear the basket for the next round
            update_basket()  # Update the basket display
    else:
        messagebox.showerror("Fruit Not Found",
                             "❌ Sorry, the fruit was not found in the basket.\nMake sure to check the spelling!")


# Function to update the fruit basket display
def update_basket():
    basket_label.config(text="Your Fruit Basket: " + ", ".join(collected_fruits))


# Creating the main window
root = tk.Tk()
root.title("Fruit Picker Game")
root.geometry("800x600")
root.configure(bg="#f2ffe6")

# Loading and displaying the animated fruit image
image_path = "animated_fruits.png"
try:
    image = Image.open(image_path).resize((400, 300))  # Resize image
    fruit_image = ImageTk.PhotoImage(image)
    image_label = tk.Label(root, image=fruit_image, bg="#f2ffe6")
    image_label.pack(pady=10)
except Exception as e:
    print(f"Error loading image: {e}")

# Creating and placing widgets
label_title = tk.Label(root, text="🍓 Fruit Picker Game 🍍", font=("Helvetica", 16, "bold"), bg="#f2ffe6", fg="#333")
label_title.pack(pady=10)

label_instruction = tk.Label(root, text="Pick your favorite fruit from the basket below:", font=("Helvetica", 12),
                             bg="#f2ffe6", fg="#666")
label_instruction.pack(pady=5)

entry = tk.Entry(root, font=("Helvetica", 12), width=30)
entry.pack(pady=10)

label_mood = tk.Label(root, text="Describe the fruit with a word (your mood):", font=("Helvetica", 12), bg="#f2ffe6",
                      fg="#666")
label_mood.pack(pady=5)

mood_entry = tk.Entry(root, font=("Helvetica", 12), width=30)
mood_entry.pack(pady=5)

btn_pick = tk.Button(root, text="Pick Fruit", font=("Helvetica", 12, "bold"), bg="#b3ff66", fg="#333",
                     command=pick_fruit)
btn_pick.pack(pady=10)

basket_label = tk.Label(root, text="Your Fruit Basket: ", font=("Helvetica", 12), bg="#f2ffe6", fg="#333")
basket_label.pack(pady=10)

# Running the main loop
root.mainloop()
