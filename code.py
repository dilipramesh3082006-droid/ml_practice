import pandas as pd
from sklearn.ensemble import RandomForestClassifier

data = {
    'Age': [20, 25, 30, 35, 40],
    'Salary': [20000, 30000, 40000, 50000, 60000],
    'Buy': [0, 0, 1, 1, 1]
}

df = pd.DataFrame(data)

X = df[['Age', 'Salary']]
y = df['Buy']

model = RandomForestClassifier()
model.fit(X, y)

prediction = model.predict([[28, 35000]])

print("Prediction:", prediction[0])