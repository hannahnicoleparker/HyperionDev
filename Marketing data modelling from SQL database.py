#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score
import sqlite3

# Load marketing data from an SQLite database using SQL
conn = sqlite3.connect("marketing_data.db")
query = "SELECT age, income, email_open_rate, conversion FROM customer_data"
data = pd.read_sql_query(query, conn)
conn.close()

# Data preprocessing
X = data.drop("conversion", axis=1)
y = data["conversion"]

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Build a predictive model (Random Forest Classifier)
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Make predictions on the test data
y_pred = model.predict(X_test)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
report = classification_report(y_test, y_pred)

# Print model evaluation results
print(f"Model Accuracy: {accuracy:.2f}")
print("Classification Report:\n", report)

# Data visualization
sns.pairplot(data, hue="conversion")
plt.title("Marketing Data Insights")
plt.show()


# In[ ]:




