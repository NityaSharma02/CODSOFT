
import tkinter as tk
from tkinter import messagebox
import random
import os

# Define the choices
choices = ['Rock', 'Paper', 'Scissors']

# Function to determine the winner
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'Rock' and computer_choice == 'Scissors') or (user_choice == 'Scissors' and computer_choice == 'Paper') or (user_choice == 'Paper' and computer_choice == 'Rock'):
        return "You win!"
    else:
        return "You lose!"

# Function to handle the user's choice
def user_choice(choice):
    computer_choice = random.choice(choices)
    result = determine_winner(choice, computer_choice)
    
    user_choice_label.config(text=f"User chose: {choice}")
    user_image_label.config(image=image_files[choice.lower()])
    
    computer_choice_label.config(text=f"Computer chose: {computer_choice}")
    computer_image_label.config(image=image_files[computer_choice.lower()])
    
    result_label.config(text=result)
    update_score(result)

# Function to update the score
def update_score(result):
    global user_score, computer_score
    if "win" in result:
        user_score += 1
    elif "lose" in result:
        computer_score += 1
    score_label.config(text=f"User: {user_score} Computer: {computer_score}")

# Function to reset the game
def reset_game():
    global user_score, computer_score
    user_score, computer_score = 0, 0
    user_choice_label.config(text="User chose:")
    user_image_label.config(image='')
    computer_choice_label.config(text="Computer chose:")
    computer_image_label.config(image='')
    result_label.config(text="")
    score_label.config(text=f"User: {user_score} Computer: {computer_score}")

# Main application
app = tk.Tk()
app.title("Rock-Paper-Scissors Game")

# User and computer score
user_score, computer_score = 0, 0

# Define the path to the image files
image_files = {
    'rock': r'C:\Users\91975\OneDrive\Desktop\codsoft\rock_paper_scissor\rock.png',
    'paper': r'C:\Users\91975\OneDrive\Desktop\codsoft\rock_paper_scissor\paper.png',
    'scissors': r'C:\Users\91975\OneDrive\Desktop\codsoft\rock_paper_scissor\scissors.png'
}

# Check if image files exist
missing_files = [file for file in image_files.values() if not os.path.isfile(file)]

if missing_files:
    messagebox.showerror("Error", f"Missing image files: {', '.join(missing_files)}")
    app.destroy()
else:
    # Load images
    for key in image_files:
        image_files[key] = tk.PhotoImage(file=image_files[key])

    # Frames for layout
    top_frame = tk.Frame(app)
    top_frame.pack(pady=20)

    middle_frame = tk.Frame(app)
    middle_frame.pack(pady=10)

    bottom_frame = tk.Frame(app)
    bottom_frame.pack(pady=10)

    # Labels for user and computer choices
    user_choice_label = tk.Label(top_frame, text="User chose:", font=('Arial', 14))
    user_choice_label.grid(row=0, column=0, padx=20)

    user_image_label = tk.Label(top_frame)
    user_image_label.grid(row=1, column=0, padx=20)

    computer_choice_label = tk.Label(top_frame, text="Computer chose:", font=('Arial', 14))
    computer_choice_label.grid(row=0, column=1, padx=20)

    computer_image_label = tk.Label(top_frame)
    computer_image_label.grid(row=1, column=1, padx=20)

    # Label for displaying results and score
    result_label = tk.Label(middle_frame, text="", font=('Arial', 14))
    result_label.pack(pady=10)

    score_label = tk.Label(middle_frame, text=f"User: {user_score} Computer: {computer_score}", font=('Arial', 14))
    score_label.pack(pady=10)

    # Buttons for user choices
    rock_button = tk.Button(bottom_frame, image=image_files['rock'], command=lambda: user_choice('Rock'))
    rock_button.pack(side='left', padx=10)

    paper_button = tk.Button(bottom_frame, image=image_files['paper'], command=lambda: user_choice('Paper'))
    paper_button.pack(side='left', padx=10)

    scissors_button = tk.Button(bottom_frame, image=image_files['scissors'], command=lambda: user_choice('Scissors'))
    scissors_button.pack(side='left', padx=10)

    # Reset button
    reset_button = tk.Button(app, text="Reset Game", command=reset_game)
    reset_button.pack(pady=20)

app.mainloop()
