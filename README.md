# 📚 Smart Study Hour Predictor

This project is a **Machine Learning web application** built using **Flask** that predicts whether a student will **pass or fail** based on their study habits, sleep hours, previous exam score, and distraction level.  
It uses a **Decision Tree Classifier** for prediction.

---

##  Features
- Predicts **Pass/Fail** results based on input data.
- Simple **Flask web interface** with a **light-themed CSS**.
- Trained using a **custom dataset**.
- Easy to modify and retrain with new data.

---

##  Project Structure
```
Decision_tree/
│
├── static/
│ └── style.css # CSS styling (light theme)
│
├── templates/
│ └── index.html # Frontend HTML form
│
├── study_data.csv # Dataset
├── train_model.py # Trains the ML model and saves it
├── app.py # Flask app to serve predictions
├── model.pkl # Saved trained model
└── README.md # Documentation
```


## 📊 Dataset
**`study_data.csv`** contains the following columns:
- `study_hours` → Hours spent studying daily.
- `sleep_hours` → Hours of sleep per day.
- `previous_score` → Previous exam score (out of 100).
- `distraction_level` → Distraction scale (1-10).
- `passed` → `1` for pass, `0` for fail.

Example:
```csv
study_hours,sleep_hours,previous_score,distraction_level,passed
5,7,65,3,1
6,8,70,2,1
3,5,50,7,0
```
## Installation & Setup
## 1️ Clone the repository
```
git clone https://github.com/your-username/smart-study-predictor.git
cd smart-study-predictor
```
## 2️ Install dependencies
```
pip install pandas scikit-learn flask
```
## 3️ Train the model
```
python train_model.py
```
## 4️ Run the Flask app
```
python app.py
```
## 5️ Open in browser
```
http://127.0.0.1:5000
```
## Model Details
Algorithm: Decision Tree Classifier

Library: scikit-learn

Target Variable: passed

Accuracy: Varies based on dataset (typically >85%)


## Future Improvements
Add data visualization for predictions.

Allow CSV upload for bulk predictions.

Implement Random Forest for better accuracy.


