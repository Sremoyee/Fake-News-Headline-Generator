import tkinter as tk
import random

# --- Data Lists ---
subjects = [
    "Ananya Pandey",
    "Khushi Kapoor",
    "Kriti Sanon",
    "A Mumbai Persian Cat",
    "A Group of Monkeys",
    "President Draupadi Murmu",
    "A Truck Driver from Haryana"
]

actions = [
    "launches",
    "cancels",
    "dances with",
    "eats",
    "declares war on",
    "celebrates with",
    "orders"
]

places_or_things = [
    "at Victoria Memorial",
    "in a Mumbai Local Train",
    "a plate of papdi chat",
    "inside The Parliament",
    "at Sarojini Market",
    "during Durga Puja",
    "at the Wagah Border"
]


# --- Core Functionality ---
def generate_headline():
    """Generates a new headline and updates the label text."""
    subject = random.choice(subjects)
    action = random.choice(actions)
    place_or_thing = random.choice(places_or_things)
    
    headline = f"{subject} {action} {place_or_thing}"
    
    # Update the label widget with the new text
    headline_label.config(text=headline)


# --- GUI Setup ---
# 1. Create the main window
root = tk.Tk()
root.title("Fake Headline Generator")
root.geometry("600x200") # Set a decent starting size

# 2. Create the widgets
headline_label = tk.Label(
    root,
    text="Click the button to generate a headline!",
    font=("Helvetica", 14),
    wraplength=550,  # Ensures text wraps within the window width
    justify="center"
)

generate_button = tk.Button(
    root,
    text="Generate New Headline",
    font=("Helvetica", 12, "bold"),
    command=generate_headline  # Link button click to our function
)

# 3. Place the widgets in the window
headline_label.pack(pady=30, padx=20)
generate_button.pack(pady=10)

# 4. Start the main event loop
root.mainloop()