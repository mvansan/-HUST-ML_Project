import pickle
import numpy as np
import re
from nltk.tokenize import word_tokenize
from sklearn.decomposition import PCA
from nltk.corpus import stopwords

import nltk
nltk.download('stopwords')
nltk.download('punkt')

x_dims = 48
pca = PCA(n_components=x_dims)

def clean_text(text):
    text = text.lower() 
    text = re.sub(r'[^a-z\s]', '', text) 
    text = re.sub(r'\s+', ' ', text).strip() 
    return text

def remove_stopwords(text):
    stop_words = set(stopwords.words('english'))
    words = word_tokenize(text)
    return ' '.join([word for word in words if word not in stop_words])

def preprocess_text(text):
    text = clean_text(text)
    text = remove_stopwords(text)
    return text

with open('rfmodel.pkl', 'rb') as model_file:
    rf_model = pickle.load(model_file)

with open('tfidf.pkl', 'rb') as vectorizer_file:
    vectorizer = pickle.load(vectorizer_file)

new_comments = [
    "I love this, i will buy it again.",
]

new_comments_cleaned = [preprocess_text(comment) for comment in new_comments]

X_new = vectorizer.transform(new_comments_cleaned).toarray()
X_new = pca.transform(X_new)

predictions = rf_model.predict(X_new)

print("Predictions:", predictions)
