# SentimentAnalysis
This project focuses on Sentiment Analysis, likely using machine learning or NLP techniques to classify text as positive, negative, or neutral. It may include preprocessing steps, a trained model, and visualizations to analyze sentiments effectively.


**📢 Sentiment Analysis** – Project Overview

The Sentiment Analysis project is a Streamlit-based web application that predicts whether a given movie review is positive or negative. It utilizes a machine learning model trained on a dataset of movie reviews, transforming input text into numerical features using TF-IDF vectorization before making predictions.

**🌟 Features**

Text Input for Review Analysis – Users can enter a movie review for sentiment prediction.

Machine Learning-Based Sentiment Detection – A pre-trained model classifies the review as either Positive 😊 or Negative 😞.

Real-Time Predictions – Instantly analyzes reviews upon user input.

User-Friendly Web Interface – Implemented using Streamlit for an interactive experience.

TF-IDF Vectorization – Converts text into numerical features for model prediction.

Pre-Trained Model Integration – Uses a pickled model for quick and efficient sentiment classification.

**🛠️ Technologies Used**

Python – Core programming language.

Streamlit – Creates an interactive web-based UI.

Pandas – Handles data processing.

Scikit-Learn – Provides ML model and text vectorization.

Pickle – Loads the pre-trained model and vectorizer.

**🚀 How It Works?**

1️⃣ User Inputs a Movie Review

The user types a review into the text area in the Streamlit web app.

2️⃣ Data Transformation Using TF-IDF

The review text is converted into a numerical format using the TF-IDF vectorizer (pre-trained and loaded from scaler.pkl).

3️⃣ Sentiment Prediction Using Machine Learning

The processed text is passed to the trained sentiment analysis model (loaded from model.pkl).

The model predicts whether the review is Positive (1) or Negative (0).

4️⃣ Displaying the Prediction

If the sentiment is positive, the app displays "Positive Review 😊".

If the sentiment is negative, the app displays "Negative Review 😞".

5️⃣ User-Friendly Interface

Built using Streamlit, allowing for real-time interaction and predictions.

**📂 Project Components**

app.py – The main script that runs the Streamlit web application.

model.pkl – A pre-trained sentiment analysis model used for prediction.

scaler.pkl – Stores the TF-IDF vectorizer, which transforms text into numerical data.

Movie_Review.csv – The dataset used for training the model.

sentiment_analysis.ipynb – A Jupyter Notebook containing the training process and model development.

**🖥️ User Interface Design**

The web app has a simple, interactive layout with:

A title ("Movie Review Sentiment Analysis").

A text box for users to enter their movie review.

A "Predict" button to analyze the sentiment.

A sentiment output message displaying whether the review is Positive or Negative.

**📌 Future Enhancements**

✅ Support for More Sentiments – Instead of binary classification, introduce Neutral and Mixed Sentiments.
✅ More Advanced NLP Models – Implement Deep Learning (LSTMs or Transformers) for better accuracy.
✅ Multilingual Sentiment Analysis – Extend support to multiple languages.
✅ Sentiment Confidence Score – Display how confident the model is in its prediction.

![Image](https://github.com/user-attachments/assets/a95fe2b7-4d4a-4bd5-a887-03ea3755a38b)

![Image](https://github.com/user-attachments/assets/e07e7ec4-9d7b-48ef-b244-7091d264ce2b)
