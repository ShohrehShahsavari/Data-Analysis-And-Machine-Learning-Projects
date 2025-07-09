from sklearn.datasets import fetch_california_housing
import pandas as pd
import numpy as np

housing = fetch_california_housing()
# Create a DataFrame from the housing data
df = pd.DataFrame(housing.data, columns=housing.feature_names)
df['target'] = housing.target

# Export to Excel
df.to_csv('california_housing.csv', index=False)