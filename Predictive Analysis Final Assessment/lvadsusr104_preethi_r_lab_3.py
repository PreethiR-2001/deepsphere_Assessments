# -*- coding: utf-8 -*-
"""LVADSUSR104_Preethi_R_Lab_3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1X0JUhS3qmAj6fGVR3JnTLGZ6HyK17QT-
"""

from sklearn.model_selection import train_test_split
from sklearn.metrics import silhouette_score, davies_bouldin_score, calinski_harabasz_score
from sklearn.preprocessing import MinMaxScaler
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA

df = pd.read_csv('/content/seeds.csv')
df.head()

print("Null values :", df.isnull().sum())
df.dropna()
print("Any duplicates :", df.duplicated().sum())

sns.boxplot(df)
plt.show()

q1=df['Compactness'].quantile(0.25)
q3=df['Compactness'].quantile(0.75)
iqr=q3-q1
low_limit=q1-(iqr*1.5)
up_limit=q3+(iqr*1.5)
df=df[(df['Compactness']>low_limit) & (df['Compactness']<up_limit)]


q1=df['Asymmetry coefficient'].quantile(0.25)
q3=df['Asymmetry coefficient'].quantile(0.75)
iqr=q3-q1
low_limit=q1-(iqr*1.5)
up_limit=q3+(iqr*1.5)
df=df[(df['Asymmetry coefficient']>low_limit) & (df['Asymmetry coefficient']<up_limit)]

print("Data description :\n", df.describe())
print("\nData Information :\n", df.info)
print("\nData Shape :\n", df.shape)
print("\nData Columns :\n", df.columns)
print(df.head())
print(df.tail())

print(df.corr())
sns.heatmap(df.corr())
plt.show()

l=[]
pca=PCA(n_components=2)
df_s=pca.fit_transform(df)
print(df_s)
for i in range(1,11):
  ml=KMeans(n_clusters=i)
  op=ml.fit_predict(df_s)
  iner_score=ml.inertia_
  l.append(iner_score)
plt.plot(range(1,11),l,marker='x')

ml=KMeans(n_clusters=3)
op=ml.fit_predict(df_s)
labels=ml.labels_
centroids=ml.cluster_centers_
plt.scatter(df_s[:,0],df_s[:,1],c=labels)
plt.scatter(centroids[:,0],centroids[:,1],marker='X',color='r')
plt.title('Clusters Formation')

sil=silhouette_score(df_s,op)
dav=davies_bouldin_score(df_s,op)
cal=calinski_harabasz_score(df_s,op)

print('Silhouette Score:',sil)
print('\nDavies Bouldin Score:',dav)
print('\ncalinski_harabasz_score:',cal)