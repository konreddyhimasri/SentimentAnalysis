import pandas as pd
import pickle as pk
import streamlit as st
from sklearn.feature_extraction.text import TfidfVectorizer

# Load trained model and vectorizer
model = pk.load(open("model.pkl", "rb"))
vectorizer = pk.load(
    open("scaler.pkl", "rb")
)  # Renaming scaler to vectorizer for clarity

# Streamlit UI
st.title("Movie Review Sentiment Analysis")
review = st.text_area("Enter your movie review here:")

if st.button("Predict"):
    if review.strip() == "":
        st.write("Please enter a review to analyze.")
    else:
        # Transform user input using the trained vectorizer
        review_transformed = vectorizer.transform([review])

        # Predict sentiment
        result = model.predict(review_transformed)

        # Display the result
        if result[0] == 0:
            st.write("Negative Review 😞")
        else:
            st.write("Positive Review 😊")
