# -*- coding: utf-8 -*-
"""FDS Experiment8.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1htaoaKc1pqYcZ3HKVZsb2WZmv7sIyoE-

1. Data Collection and Preprocessing
● Load the dataset using Pandas.
● Handle missing values.
● Perform exploratory data analysis (EDA) using Matplotlib or Seaborn.
● Normalize/scale the data if necessary.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
dataset = pd.read_excel('cleandata_with_humidity.xlsx')

# Display first few rows
print(dataset.head())

# Summary statistics
print(dataset.describe())

# Continuous variable distributions
plt.figure(figsize=(15, 5))
for i, column in enumerate(['Power Consumption', 'Outdoor Temperature', 'Humidity']):
    plt.subplot(1, 3, i + 1)
    sns.histplot(dataset[column], kde=True, color='blue')
    plt.title(f'{column} Distribution')
plt.tight_layout()
plt.show()

sns.countplot(x='Occupancy', data=dataset, palette='viridis')
plt.title('Occupancy Count')
plt.show()

# Compute correlation matrix
correlation_matrix = dataset.corr()

# Visualize the correlation matrix
plt.figure(figsize=(10, 6))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Correlation Matrix')
plt.show()

sns.scatterplot(x='Outdoor Temperature', y='Power Consumption', data=dataset)
plt.title('Outdoor Temperature vs. Power Consumption')
plt.show()

sns.scatterplot(x='Humidity', y='Power Consumption', data=dataset)
plt.title('Humidity vs. Power Consumption')
plt.show()

sns.boxplot(x='Occupancy', y='Power Consumption', data=dataset)
plt.title('Occupancy vs. Power Consumption')
plt.show()

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler

# Load dataset
data = pd.read_excel('cleandata_with_humidity.xlsx')
# Check for missing values
print(data.isnull().sum())

# Fill missing values (if any)
data.fillna(method='ffill', inplace=True)

# Normalize continuous features
scaler = StandardScaler()
data[['Temperature', 'Humidity']] = scaler.fit_transform(data[['Outdoor Temperature', 'Humidity']])

# Visualize data
sns.pairplot(data, diag_kind='kde')
plt.show()

from sklearn.model_selection import train_test_split
from sklearn.linear_model import Ridge
from sklearn.metrics import mean_squared_error
import pandas as pd # Import pandas

# Load dataset (if not already loaded)
# Assuming 'cleandata_with_humidity.xlsx' is in the same directory
data = pd.read_excel('cleandata_with_humidity.xlsx')

# Split data
X = data[['Outdoor Temperature', 'Humidity', 'Occupancy']]
y = data['Power Consumption']
X_train, X_test, y_train, y_test = train_test_split(X, y,
test_size=0.2, random_state=42)

# Train model
model = Ridge()
model.fit(X_train, y_train)

# Test model
y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
print(f'Mean Squared Error: {mse}')

!pip install streamlit

import streamlit as st
import numpy as np

# Streamlit app
st.title("Energy Consumption Prediction")

# Input fields
temperature = st.number_input("Temperature (°C)")
humidity = st.number_input("Humidity (%)")
occupancy = st.radio("Occupancy", (0, 1))

# Prediction button
if st.button("Predict"):
    # Make prediction
    # Indent the following lines to be inside the 'if' block
    # and use the input values for prediction
    input_features = np.array([[temperature, humidity, occupancy]])
    prediction = model.predict(input_features)[0]
    st.write(f"Predicted Energy Consumption: {prediction:.2f} kWh")

import joblib
joblib.dump(model, 'ridge_model.pkl')