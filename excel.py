import pandas as pd
from sklearn.tree import DecisionTreeClassifier

# Sample dataset
data = {
    'Hours_Studied': [1, 2, 3, 4, 5, 6],
    'Pass': [0, 0, 0, 1, 1, 1]
}

df = pd.DataFrame(data)

# Input and Output
X = df[['Hours_Studied']]
y = df['Pass']

# Create Decision Tree Model
model = DecisionTreeClassifier()

# Train Model
model.fit(X, y)

# Predict for 4 hours study
prediction = model.predict([[4]])

print("Prediction:", prediction[0])