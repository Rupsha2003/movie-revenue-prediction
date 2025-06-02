Movie Revenue Prediction System

This repository contains a complete **machine learning pipeline and deployment-ready application** for predicting movie revenue based on essential movie attributes. 
Developed as a data science project, it leverages a regression model trained on curated data and presents predictions through an intuitive **Streamlit web application**.

Project Objective

The goal of this project is to **build a machine learning model** capable of estimating the **revenue of a movie** based on factors such as its budget, runtime, and popularity score.
These features are known to be strongly correlated with box office performance. The final application enables users—such as filmmakers, producers, 
or analysts—to interactively explore how various factors influence projected earnings.


 Machine Learning Model

- **Algorithm Used**: Regression (e.g., Linear Regression, Random Forest, etc. – adjust based on your actual model)
- **Trained Features**:
  - Budget (in millions of USD)
  - Popularity Score (e.g., based on search or social metrics)
  - Runtime (in minutes)

- Output:
  - Predicted Revenue in USD

- Model File:
  - Saved using `pickle` as `trained_model.sav` for efficient loading during inference.

Streamlit Web App

An interactive and minimalistic web interface was created using **Streamlit**, allowing users to:

- Input values for:
  - Budget
  - Popularity
  - Runtime
- Click a button to trigger prediction
- Instantly receive a projected revenue output in a user-friendly format

User Interface Features

- **Clean and intuitive layout** for ease of use
- **Input widgets**: number inputs and sliders
- **Success message** displays revenue prediction with formatting
- Responsive layout that works across devices (desktop/tablet)

 Repository Contents
 movie-revenue-predictor/
│
├── app(movie).py # Streamlit app for user interaction
├── trained_model.sav # Pre-trained ML model (pickled)
├── requirements.txt # Full list of Python dependencies
├── README.md # Project documentation 

Use the App
Enter the movie's budget, popularity score, and runtime
Click "Predict Revenue"
View the predicted revenue instantly

Example Use Case
Say you’re a producer planning a new movie:

Budget: $70 million
Popularity Score: 60
Runtime: 130 minutes
Enter these into the app and get an instant revenue forecast, helping you make informed production or marketing decisions.

![image](https://github.com/user-attachments/assets/4b194487-33c2-4d13-9f56-56f063b9fef7)






