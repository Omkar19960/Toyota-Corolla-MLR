🚗 Toyota Corolla Price Prediction

A Machine Learning web application that predicts the price of a used
Toyota Corolla using Multiple Linear Regression. The trained
model is integrated with a simple and interactive Streamlit
interface.

🌐 Live Application

Try the application:
https://toyota-corolla-mlr-xwfp7uwfgmzrqnzc8cs2ev.streamlit.app/

📌 Project Overview

This project demonstrates an end-to-end Machine Learning workflow:

Data-based price prediction

Multiple Linear Regression

Trained model serialization using Pickle

Interactive Streamlit web application

User input and real-time prediction

The application takes important Toyota Corolla specifications as input
and returns an estimated price in Euros (€).

✨ Features

🚘 Toyota Corolla price prediction

🤖 Multiple Linear Regression model

🌐 Interactive Streamlit application

📊 Simple and user-friendly input interface

⛽ Petrol, Diesel and CNG fuel-type selection

⚙️ Automatic/manual transmission input

💶 Predicted price displayed in Euros

📚 History section for viewing prediction-related information

🧠 Machine Learning Model

The project uses Multiple Linear Regression to predict the price of
a Toyota Corolla from multiple vehicle characteristics.

The trained model is stored in:

MultipleLinearRegression.pkl

The Streamlit application loads this model and sends the user's input to
it for prediction.

📥 Input Features

The application accepts the following vehicle details:

Feature               Description

Age of Car            Age of the car in months
Kilometers            Total distance travelled
Horse Power           Engine horsepower
Engine Capacity       Engine capacity in cc
Number of Doors       Number of doors
Number of Cylinders   Engine cylinder count
Number of Gears       Number of gears
Weight                Vehicle weight in kg
Automatic             Transmission type indicator
Fuel Type             Petrol, Diesel or CNG

🛠️ Technologies Used

Python

Pandas

NumPy

Scikit-learn

Streamlit

Jupyter Notebook

Pickle

📂 Project Structure

Toyota-Corolla-MLR/
│
├── MLR.ipynb
├── MultipleLinearRegression.pkl
├── ToyotaCorolla - MLR.csv
├── app.py
├── requirements.txt
└── README.md

🔄 Project Workflow

Toyota Corolla Dataset
        ↓
Data Preprocessing
        ↓
Feature Selection
        ↓
Multiple Linear Regression
        ↓
Model Training
        ↓
Save Trained Model
        ↓
Streamlit Application
        ↓
User Input
        ↓
Price Prediction

🚀 Run the Project Locally

1. Clone the repository

git clone https://github.com/Omkar19960/Toyota-Corolla-MLR.git

2. Open the project directory

cd Toyota-Corolla-MLR

3. Install dependencies

pip install -r requirements.txt

4. Run the Streamlit application

streamlit run app.py

The application will open in your browser.

🖥️ How to Use

Open the Streamlit application.

Enter the Toyota Corolla's specifications.

Select the transmission type.

Select the fuel type.

Click Predict Price.

The application displays the estimated Toyota Corolla price in
Euros.

Use the History section to review the available prediction
history/information.

📊 Prediction

The application creates a DataFrame from the user's inputs, arranges the
features according to the trained model's expected feature order, and
generates a price prediction.

The prediction is displayed in the following format:

Predicted Toyota Corolla Price: € XX,XXX.XX

📓 Jupyter Notebook

MLR.ipynb contains the Machine Learning development workflow,
including model preparation and training.

📦 Dependencies

The project dependencies are listed in requirements.txt:

streamlit
pandas
numpy
scikit-learn

🎯 Project Objective

The main objective of this project is to demonstrate how a Multiple
Linear Regression model can be used for used-car price prediction and
deployed as an interactive web application using Streamlit.

👨‍💻 Author

Omkar Mortale

GitHub:
https://github.com/Omkar19960
