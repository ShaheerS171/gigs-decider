# 🚀 Freelance Gig Quality Classifier

This project is an AI-powered tool that predicts whether a **freelancing gig description** is **Good ✅** or **Not Good ❌**.  
It’s built using **Python, Scikit-learn, XGBoost, and Streamlit** to provide a simple and interactive web app.  

---

## 📌 Features
- 🧹 **Smart Text Cleaning** – Removes punctuation, numbers, links, emojis, and stopwords.  
- 🔮 **Machine Learning Model (XGBoost)** – Trained on real gig data with TF-IDF vectorization.  
- 📊 **Prediction Confidence Chart** – Shows how confident the model is about your gig being good or not.  
- 🌐 **Streamlit Web App** – Easy-to-use interface for non-technical users.  

---

## 🛠️ Tech Stack
- **Python 3.10+**
- **Pandas / NumPy** – Data handling  
- **NLTK** – Text preprocessing  
- **Scikit-learn** – Vectorization & model evaluation  
- **XGBoost** – Classification model  
- **Streamlit** – Web app deployment  

---

## 📦 Installation
Clone the repo and install dependencies:

```bash
git clone https://github.com/your-username/gig-quality-classifier.git
cd gig-quality-classifier

# Create virtual environment (recommended)
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate

# Install requirements
pip install -r requirements.txt

▶️ Usage
streamlit run app.py
📦 gig-quality-classifier
 ┣ 📜 app.py                # Streamlit app
 ┣ 📜 xgb.pkl               # Trained ML model
 ┣ 📜 vectorizer.pkl        # TF-IDF vectorizer
 ┣ 📜 requirements.txt      # Dependencies
 ┣ 📜 README.md             # Documentation
 ┗ 📂 data (optional)       # Dataset if shared
