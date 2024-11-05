# credit_scoring.py
import tkinter as tk
from tkinter import messagebox
import joblib
import pandas as pd

def predict_score():
    try:
        inputs = [float(entry.get()) for entry in entries]
        data = pd.DataFrame([inputs], columns=feature_names)
        prediction = model.predict(data)[0]
        result_label.config(text=f"Predicted Creditworthiness: {'Good' if prediction == 0 else 'Bad'}")
    except ValueError:
        messagebox.showerror("Input error", "Please enter valid numerical values.")

# Load the model and feature names
model = joblib.load("credit_scoring_model.pkl")
feature_names = model.feature_names_in_

# Set up the main window
app = tk.Tk()
app.title("Credit-Prediction Model")
app.geometry("500x400")  # Set a fixed window size
app.resizable(False, False)

# Create a frame and canvas for scrolling
frame = tk.Frame(app)
frame.pack(fill="both", expand=True)

canvas = tk.Canvas(frame)
scrollbar = tk.Scrollbar(frame, orient="vertical", command=canvas.yview)
scrollable_frame = tk.Frame(canvas)

scrollable_frame.bind(
    "<Configure>",
    lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
)

canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
canvas.configure(yscrollcommand=scrollbar.set)

# Place canvas and scrollbar in the main frame
canvas.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")

# Create entry fields inside the scrollable frame
entries = []
for idx, feature in enumerate(feature_names):
    tk.Label(scrollable_frame, text=feature).grid(row=idx, column=0, padx=10, pady=5, sticky="w")
    entry = tk.Entry(scrollable_frame)
    entry.grid(row=idx, column=1, padx=10, pady=5)
    entries.append(entry)

# Add Predict button and result label in the scrollable frame
predict_button = tk.Button(scrollable_frame, text="Predict", command=predict_score, font=("Arial", 12), padx=20, pady=10)
predict_button.grid(row=len(feature_names) + 1, column=0, columnspan=2, pady=20)

result_label = tk.Label(scrollable_frame, text="", font=("Arial", 12))
result_label.grid(row=len(feature_names) + 2, column=0, columnspan=2)

app.mainloop()
