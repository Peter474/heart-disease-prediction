# heart-disease-prediction
markdown
# ❤️ Heart Disease Prediction - Machine Learning Project

This project uses machine learning techniques to analyze and predict the risk of heart disease using the UCI Heart Disease dataset.

## 🧠 Project Overview

- Perform data preprocessing and cleaning
- Dimensionality reduction using PCA
- Feature selection using statistical and ML-based techniques
- Train supervised models: Logistic Regression, Decision Tree, Random Forest, SVM
- Apply unsupervised clustering: K-Means, Hierarchical Clustering
- Hyperparameter tuning using GridSearchCV
- Build a simple Streamlit web interface for real-time predictions (Bonus)
- Deploy the Streamlit app using Ngrok (Bonus)

---

## 📊 Dataset

- **Source:** [UCI Heart Disease Dataset](https://archive.ics.uci.edu/ml/datasets/heart+Disease)
- **Attributes:** Age, Sex, Chest Pain, Blood Pressure, Cholesterol, etc.
- **Target:** Presence (1) or absence (0) of heart disease

---

## 🧪 Models Used

### ✅ Supervised Learning
- Logistic Regression
- Decision Tree
- Random Forest
- SVM

### 🔍 Unsupervised Learning
- K-Means Clustering
- Hierarchical Clustering

---

## 🧰 Tools & Libraries

- Python
- Pandas, NumPy, Matplotlib, Seaborn
- Scikit-learn
- Streamlit
- Pyngrok
- Joblib

---

## 🚀 Instructions to Run

### 1. Clone the project:
```bash
git clone https://github.com/your-username/heart-disease-prediction.git
cd heart-disease-prediction
````

### 2. Install dependencies:

```bash
pip install -r requirements.txt
```

### 3. Run the Streamlit App:

```bash
streamlit run app.py
```

### 4. (Optional) Deploy with Ngrok:

```bash
ngrok authtoken ngrok config add-authtoken 30s8SOuyOUBLFTHwPioAxXcAjWs_DteQVmAB3VPoB8XMKZtA
ngrok http 8501
```

---

## 📁 Folder Structure

```
heart-disease-prediction/
│
├── app.py                     # Streamlit app
├── heart.ipynb                # Main notebook with all steps
├── heart_disease_model.pkl    # Trained model
├── scaler.pkl                 # Scaler used in preprocessing
├── requirements.txt           # Python dependencies
├── README.md                  # Project documentation
```

---

## ✅ Final Deliverables

* Cleaned dataset
* PCA reduced data
* Supervised and unsupervised models
* Evaluation reports
* Optimized model
* .pkl model file
* Streamlit UI (Bonus)
* Ngrok deployment (Bonus)
* GitHub repository with all code

---

## 🧑‍💻 Author

Peter Emad



