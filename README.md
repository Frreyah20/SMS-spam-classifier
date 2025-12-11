## SMS Spam Classifier
A simple and interactive machine learning–based SMS Spam Detection System built using Python, Scikit-Learn, and Streamlit.
The app predicts whether a given SMS message is Spam or Not Spam using a trained TF-IDF + classifier model.

Features
Text preprocessing (cleaning, tokenization, stopword removal, stemming)
TF-IDF vectorization of input messages
Trained ML model for instant spam prediction
Clean and interactive Streamlit interface
Fast, real-time classification

Project Structure
app.py                            # Streamlit application (UI + prediction)
3_SMS_spam_classifier.ipynb       # Jupyter notebook (training + preprocessing)
vectorizer.pkl                    # Saved TF-IDF vectorizer
model.pkl                         # Trained ML classification model
requirements.txt                  # Project dependencies
README.md                         # Project documentation

How the Model Works
The SMS message is cleaned (lowercasing, removing special characters, stopwords, punctuation, etc.)
The text is transformed into TF-IDF features using the saved vectorizer.pkl.
The trained ML model (model.pkl) predicts whether the message is Spam or Ham (not spam).
Streamlit displays the result instantly on the interface.

Running the App Locally
1. Clone the repository
   git clone your-repo-url](https://github.com/Frreyah20/SMS-spam-classifier.git
   cd https://github.com/Frreyah20/SMS-spam-classifier.git
2. Install dependencies
   pip install -r requirements.txt
3. Ensure NLTK data is installed
   If running for the first time, download required NLTK data:
   python -c "import nltk; nltk.download('stopwords'); nltk.download('punkt')"
4. Run the Streamlit app
   streamlit run app.py
5. Streamlit will open automatically at:
   http://localhost:8501/

Model Files
This project includes:
vectorizer.pkl -> TF-IDF vectorizer
model.pkl -> trained ML classifier
These files are required for predictions and are included in the repository.
If you retrain the model using the notebook, simply replace these files with the updated ones.

Acknowledgements
I referred to multiple online tutorials and learning resources to understand text preprocessing, TF-IDF vectorization, and building the Streamlit interface for this project.
Huge thanks to those creators for providing clear explanations and guidance.
Dataset: https://www.kaggle.com/datasets/uciml/sms-spam-collection-dataset

