import streamlit as st
import pandas as pd
import numpy as np
import pickle
import string
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
ps = PorterStemmer()
nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('stopwords')


def transform_text(text):
  text = text.lower()
  text = nltk.word_tokenize(text)
  y = []
  for i in text:
    if i.isalnum():
      y.append(i)
  text = y[:];
  y.clear()
  for i in text:
    if i not in stopwords.words('english') and i not in string.punctuation:
      y.append(i)
  text = y[:]
  y.clear()
  for i in text:
    y.append(ps.stem(i))

  return " ".join(y)

tfidf = pickle.load(open('vectorizer.pkl', 'rb'))
model = pickle.load(open('model.pkl', 'rb'))

st.title('SMS Spam Classifier')
input_sms = st.text_input('Enter SMS')


if st.button("Predict"):
    if input_sms.strip():   # only run when user enters text
        transformed_sms = transform_text(input_sms)
        vector_input = tfidf.transform([transformed_sms]).toarray()
        prediction = model.predict(vector_input)
        pred = prediction[0]

        if pred == 1:
            st.header('Spam')
        else:
            st.header('Not Spam')
    else:
        st.warning("Please enter an SMS message.")