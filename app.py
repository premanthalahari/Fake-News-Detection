import streamlit as st
import joblib

vectorizer = joblib.load("vectorizer.jb")
model = joblib.load("lr_model.jb")

st.title("Fake News Detector")
st.write("Enter the news headline and content to check if it is fake or real.")

news_input = st.text_area("Enter the news headline and content", "")

if st.button("Check news"):
    if news_input.strip():
        transform_input = vectorizer.transform([news_input])
        prediction = model.predict(transform_input)

        if prediction[0] == 1:
            st.success("Real News")
        else:
            st.error("Fake News")
    else:
        st.success("Please enter the news headline and content.")