# -*- coding: utf-8 -*-
"""Breast Cancer prediction system.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1_RgavdC-47f8XrI89BWN3m2cKKWOwQAd

# **Jie-Long Chen**
"""

import pandas as pd
from sklearn.model_selection import train_test_split
import tensorflow as tf

dataset = pd.read_csv('cancer.csv')

x = dataset.drop(columns=["diagnosis(1=m, 0=b)"])
y = dataset["diagnosis(1=m, 0=b)"]

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)

model = tf.keras.models.Sequential()

model.add(tf.keras.layers.Dense(256, input_shape=(x_train.shape[1],), activation='sigmoid'))
model.add(tf.keras.layers.Dense(256, activation='sigmoid'))
model.add(tf.keras.layers.Dense(1, activation='sigmoid'))

model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

model.fit(x_train, y_train, epochs=1000)

def dp(data):
  import numpy as np 
  list_rows = [ ['radius_mean', 'texture_mean', 'perimeter_mean',
                'area_mean', 'smoothness_mean', 'compactness_mean',
                'concavity_mean', 'concave points_mean', 'symmetry_mean', 'fractal_dimension_mean'],
              [data[0],data[1],data[2],data[3],data[4],data[5],data[6],data[7],data[8],data[9]]] 
  np.savetxt("data.csv", list_rows, delimiter =",",fmt ='% s')

while True:
  print("乳癌預測系統(第一筆資料輸入0結束)")
  radius_mean = float(input("radius_mean:"))
  if radius_mean == 0 : break
  texture_mean = float(input("texture_mean:"))
  perimeter_mean = float(input("perimeter_mean:"))
  area_mean = float(input("area_mean:"))
  smoothness_mean = float(input("smoothness_mean:"))
  compactness_mean = float(input("compactness_mean:"))
  concavity_mean = float(input("concavity_mean:"))
  concavepoints_mean = float(input("concave points_mean:"))
  symmetry_mean = float(input("symmetry_mean:"))
  fractal_dimension_mean = float(input("fractal_dimension_mean:"))
  data = []
  data.extend([radius_mean, texture_mean, perimeter_mean,
              area_mean, smoothness_mean, compactness_mean,
              concavity_mean, concavepoints_mean, symmetry_mean, fractal_dimension_mean])
  dp(data)
  data = pd.read_csv('data.csv')
  result = model.predict(data)
  result = str(result)
  result = result.replace("[","")
  result = result.replace("]","")
  print(f"\n得到乳癌的機率:{round(float(result),2)}\n")