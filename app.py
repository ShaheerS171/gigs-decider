import streamlit as st
import joblib
import matplotlib.pyplot as plt
import string
import nltk
import os
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

nltk.download("punkt")
nltk.download("stopwords")

# Use absolute paths with os.path.join
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "xgb.pkl")
VECTORIZER_PATH = os.path.join(BASE_DIR, "vectorizer.pkl")

model = joblib.load(MODEL_PATH)
vectorizer = joblib.load(VECTORIZER_PATH)

stop_words = set(stopwords.words("english"))

def clean_text(txt):
    txt = txt.lower()
    txt = txt.translate(str.maketrans("", "", string.punctuation))
    words = word_tokenize(txt)
    words = [w for w in words if w not in stop_words]
    return " ".join(words)

st.set_page_config(page_title="Gig Quality Classifier", page_icon="🚀", layout="centered")

st.title("🧾 Freelance Gig Quality Classifier")
st.write("Type your gig description and let the model decide if it's **Good** or **Not Good** ✅❌")

gig_text = st.text_area("✍️ Enter your gig description here:")

if st.button("🔮 Predict"):
    if gig_text.strip():
        cleaned_text = clean_text(gig_text)

        vec = vectorizer.transform([cleaned_text])
        pred = model.predict(vec)[0]
        prob = model.predict_proba(vec)[0]  # [prob_not_good, prob_good]

        st.subheader("📊 Prediction Result:")
        st.write("**Good Gig ✅**" if pred == 1 else "**Not Good Gig ❌**")

        labels = ["Not Good ❌", "Good ✅"]
        fig, ax = plt.subplots()
        ax.bar(labels, prob, color=["red", "green"])
        ax.set_ylim((0, 1))
        ax.set_ylabel("Probability")
        ax.set_title("Model Confidence")

        st.pyplot(fig)

    else:
        st.warning("⚠️ Please enter some text before")