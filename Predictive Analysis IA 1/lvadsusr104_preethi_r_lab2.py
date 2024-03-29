# -*- coding: utf-8 -*-
"""LVADSUSR104_Preethi R_LAB2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1uETUBOGvobrz-Ea_h0PNrppaHkStJJ0O
"""

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import warnings
warnings.filterwarnings("ignore")
import seaborn as sns
import matplotlib.pyplot as plt

#1
df = pd.read_csv('/content/booking.csv')
df.head()
print(df.isnull().sum())
print("We don't have any missing values")

Q1 = df.quantile(0.25)
Q3 = df.quantile(0.75)
IQR = Q3 - Q1
ol = ((df < (Q1 - 1.5 * IQR)) | (df > (Q3 + 1.5 * IQR))).any(axis=1)
print("Number of outliers detected:", ol.sum())

#2
label_encoder = LabelEncoder()
categorical_cols = df.select_dtypes(include=['object']).columns
for col in categorical_cols:
  df[col] = label_encoder.fit_transform(df[col])

#3
sns.plot(df[~ol])
plt.show()

df = df.drop_duplicates()
print("Duplicates are dropped")

x = df.drop('booking status', axis=1)
y = df['booking status']

#4
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3)
print("dataset is splitted in ratio of 70:30 for train data:test data")

#5
lr = LogisticRegression()
lr.fit(x_train, y_train)
vop = lr.predict(x_test)

#6
acc = accuracy_score(y_test, vop)
print("Accuracy: ", acc)

print("Classification Report :\n", classification_report(y_test, vop))

print("\nConfusion matrix :\n", confusion_matrix(y_test, vop))