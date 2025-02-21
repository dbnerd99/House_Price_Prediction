# 🏠 House Price Prediction Web App

This is a **Flask-based web application** that predicts house prices based on input features such as **area, number of bedrooms, bathrooms, and stories**. The model is trained using a **Linear Regression** algorithm on an open-source housing dataset.

---

## 📌 Features
- Predicts **house prices** based on user input.
- Uses **Flask** for the web interface and **Scikit-learn's Linear Regression** for predictions.
- Built with **Bootstrap 4** for a modern and responsive UI.
- **Pickle serialization** for efficient model loading.
- Well-documented **GitHub repository** with snapshots.

---

## 🛠 Tech Stack
- **Frontend:** HTML, CSS, Bootstrap  
- **Backend:** Flask (Python)  
- **Machine Learning Model:** Scikit-learn (Linear Regression)  
- **Data Handling:** Pandas, NumPy  
- **Model Deployment:** Pickle  

---

## 📂 Dataset Information
The dataset used for training is **Housing.csv**, which contains the following columns:
- **area** → Total area of the house (sq. ft.)  
- **bedrooms** → Number of bedrooms  
- **bathrooms** → Number of bathrooms  
- **stories** → Number of floors in the house  
- **price** → Target variable (House price)  

---

## 🚀 Installation & Setup

### 1 Clone the Repository
```sh
git clone https://github.com/dbnerd99/House_price_prediction.git
cd House_price_prediction
```
### 2 Install Dependencies
```
pip install -r requirements.txt
```
### 3 Run the Flask App
```
python app.py
```
### 4 Open the Web App
```
http://127.0.0.1:5000/
```

---

## 🎯 Usage Guide
- 1️⃣ Enter the required house details (area, bedrooms, bathrooms, stories).
- 2️⃣ Click on "Predict Price".
- 3️⃣ View the estimated house price.
