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
app.geometry("400x300")
app.resizable(False, False)  # Fixed size

# Create entry fields
entries = []
for idx, feature in enumerate(feature_names):
    tk.Label(app, text=feature).grid(row=idx, column=0, padx=10, pady=5)
    entry = tk.Entry(app)
    entry.grid(row=idx, column=1, padx=10, pady=5)
    entries.append(entry)

# Prediction button and result display
predict_button = tk.Button(app, text="Predict", command=predict_score, font=("Arial", 12), padx=20, pady=10)
predict_button.grid(row=len(feature_names), column=0, columnspan=2, pady=10)

result_label = tk.Label(app, text="", font=("Arial", 12))
result_label.grid(row=len(feature_names)+1, column=0, columnspan=2)

app.mainloop()
