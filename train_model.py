import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
import pickle

# Load dataset
df = pd.read_csv('decision.csv')

# Features (X) and target (y)
X = df[['study_hours', 'sleep_hours', 'previous_score', 'distraction_level']]
y = df['passed']

# Split into train/test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = DecisionTreeClassifier()
model.fit(X_train, y_train)

# Save model
with open('decision_tree_model.pkl', 'wb') as f:
    pickle.dump(model, f)

print("✅ Model trained and saved as decision_tree_model.pkl")
