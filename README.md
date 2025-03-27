# 📰 Fake News Detection - Machine Learning Project

Classify news articles as real or fake using machine learning and deploy your model with Streamlit! This project provides a step-by-step guide to building a text classification system, from preprocessing raw text data to deploying an interactive web application.

![Streamlit Demo](https://img.shields.io/badge/Streamlit-Demo-FF4B4B?logo=streamlit) [![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](fake-news-detector0.streamlit.app/)

## 📌 Project Overview
This project uses the [Fake and Real News Dataset](https://www.kaggle.com/datasets/clmentbisaillon/fake-and-real-news-dataset) to train a machine learning model for fake news detection. The deployed Streamlit app allows users to input news text and instantly classify it as real or fake.

## ✨ Features
- **Text Preprocessing:** Clean and normalize text data (lowercasing, removing special characters, etc.).
- **Feature Extraction:** Convert text to numerical features using TF-IDF Vectorizer.
- **Model Training:** Test algorithms like Logistic Regression, Naive Bayes, and **Random Forest** (best-performing model).
- **Model Evaluation:** Metrics include accuracy, precision, recall, and F1-score.
- **Streamlit Deployment:** Interactive web interface for real-time classification.

## 🛠️ Installation
1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/fake-news-detection.git
   cd fake-news-detection

2. **Install dependencies:**

    ```bash
    pip install -r requirements.txt

🚀 Usage

Run the Streamlit app locally:

    ```bash
    streamlit run app.py

📊 Dataset

The dataset contains two CSV files:


True.csv: 21,417 real news articles.


Fake.csv: 23,481 fake news articles.


Key Preprocessing Steps:


Balancing classes (real vs. fake).


Removing stopwords, punctuation, and non-alphanumeric characters.


Stemming/Lemmatization using NLTK.


Splitting data into training (80%) and testing (20%) sets.


Feature extraction with TF-IDF Vectorizer.


Download the dataset from Kaggle.






🤖 Model Training

Algorithms Tested

Logistic Regression (Final Model)

Multinomial Naive Bayes

Random Forest Classifier 

Support Vector Machine (SVM)


    ```bash
    Evaluation Metrics
    Model	          Accuracy	  Precision	  Recall	  F1-Score
    Random Forest	   96.2%	      96.5%	    96.0%	      96.2%

🌐 Deployment

The model is deployed using Streamlit with the following app features:

Text input box for news articles.

Real-time classification (Real/Fake) with confidence score.

Responsive design for seamless use on all devices.



---

### 🔍 Tips for Customization
1. Replace `YOUR-STREAMLIT-APP-URL-HERE` with your app's live URL.
2. Add screenshots of your app/EDA under the **Deployment** section.
3. Update the **Evaluation Metrics** table with your model’s actual performance.
4. Include additional preprocessing steps (e.g., lemmatization) if implemented.
