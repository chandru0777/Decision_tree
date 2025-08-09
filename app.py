from flask import Flask, request, render_template
import pickle
import numpy as np

app = Flask(__name__)

# Load trained Decision Tree model
with open('decision_tree_model.pkl', 'rb') as f:
    model = pickle.load(f)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        study_hours = float(request.form['study_hours'])
        sleep_hours = float(request.form['sleep_hours'])
        previous_score = float(request.form['previous_score'])
        distraction_level = float(request.form['distraction_level'])

        # Prepare data for prediction
        features = np.array([[study_hours, sleep_hours, previous_score, distraction_level]])
        prediction = model.predict(features)[0]

        # Convert numeric prediction to Pass/Fail
        result = "Pass ✅" if prediction == 1 else "Fail ❌"

        return render_template('result.html', prediction=result)

    except Exception as e:
        return f"❌ Error: {e}"

if __name__ == "__main__":
    app.run(debug=True)
