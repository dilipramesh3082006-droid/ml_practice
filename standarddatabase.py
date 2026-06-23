import pandas as pd
from sklearn.preprocessing import StandardScaler

# Sample data
data = {'hours': [1, 2, 3, 4, 5],
        'score': [20, 40, 50, 65, 80]}

df = pd.DataFrame(data)

# Standardize data
scaler = StandardScaler()
df_standardized = pd.DataFrame(
    scaler.fit_transform(df),
    columns=df.columns
)

print(df_standardized)