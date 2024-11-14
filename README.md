# Credit Scoring Model

This repository contains a machine learning project for predicting creditworthiness based on user input. The project includes a trained model and a Tkinter GUI to provide an easy-to-use interface for predictions.

## Table of Contents
- [Overview](#overview)
- [Files](#files)
- [Installation](#installation)
- [Usage](#usage)
- [Data](#data)
- [Dependencies](#dependencies)
- [License](#license)

## Overview
The Credit Scoring Model is designed to predict whether a credit applicant is "Good" or "Bad" in terms of creditworthiness based on various financial inputs. The `credit_scoring.py` script provides a graphical interface for inputting applicant data and receiving predictions.

## Files
- `credit_scoring.py`: The GUI application where users can enter data and receive predictions on creditworthiness.
- `train_model.py`: Script for training the credit scoring model. It reads data from a CSV file, preprocesses it, trains a model, and saves the model for later use.
- `credit_data.csv`: The dataset used to train the model (make sure this file is in the same directory as `train_model.py`).

## Installation
1. **Clone the repository:**

    ```bash
   git clone https://github.com/your-username/credit-scoring-model.git
    ```
    
3. **Navigate to the repository folder:**

   ```bash
      cd credit-scoring-model
   ```
5. **Install the required packages:**

    ```bash
       pip install -r requirements.txt
    ```
##  Usage 

1.**Train the Model:** Run train_model.py to train and save the model.
   
   ```bash
     python train_model.py
   ```

2. **Launch the GUI Application:** Run credit_scoring.py to open the GUI for making predictions.
    ```bash
     python credit_scoring.py
    ```

4. Enter Data and Predict: Input values for each feature, and click "Predict" to receive a prediction of either "Good" or "Bad" creditworthiness.

## Data
   The data for training the model is stored in credit_data.csv. It includes various financial attributes of applicants that help predict their creditworthiness.

## Dependencies
- pandas
- sckit-learn
- joblib
- tkinter

Install dependencies with:
  
  ```bash
     pip install -r requirements.txt
  ```
##  License
This project is licensed under the MIT License.
This Markdown text is ready to be saved as `README.md` in your repository. Let me know if there are any additional details you’d like to include!
