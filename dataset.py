# -*- coding: utf-8 -*-
"""DATASET.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1l9sc0CgrlTCBONMlbYycQAy6W8glBaT0
"""

from google.colab import files
uploaded = files.upload()

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Supongamos que el archivo se llama "DATASETFINAL.xlsx"
df = pd.read_excel("DATASETFINAL2.xlsx")

# Concatenar las dos columnas y guardar el resultado en una nueva columna
df['Fecha'] = df['Fecha.1'].astype(str) + df['Fecha.2'].astype(str) + df['Hora'].astype(str)
df = df.drop('Fecha.1', axis=1)
df = df.drop('Fecha.2', axis=1)
df = df.drop('Hora', axis=1)

# Mostrar el DataFrame resultante
print(df)

df_con_valores_reemplazados = df.copy()  # Copia el DataFrame original
nuevo_valor = 0

columna_a_actualizar = "SO2"
df_con_valores_reemplazados[columna_a_actualizar].fillna(nuevo_valor, inplace=True)

columna_a_actualizar = "NO"
df_con_valores_reemplazados[columna_a_actualizar].fillna(nuevo_valor, inplace=True)

columna_a_actualizar = "CO"
df_con_valores_reemplazados[columna_a_actualizar].fillna(nuevo_valor, inplace=True)

columna_a_actualizar = "PM10"
df_con_valores_reemplazados[columna_a_actualizar].fillna(nuevo_valor, inplace=True)

columna_a_actualizar = "O3"
df_con_valores_reemplazados[columna_a_actualizar].fillna(nuevo_valor, inplace=True)

columna_a_actualizar = "Fecha"
df_con_valores_reemplazados[columna_a_actualizar].fillna(nuevo_valor, inplace=True)

# Verifica si hay valores NaN en el DataFrame y cualquier valor True indica presencia de NaN en esa columna
valores_nulos_por_columna = df_con_valores_reemplazados.isna().any()

# Imprime los resultados
print("Valores nulos por columna:")
print(valores_nulos_por_columna)

# Visualizar las primeras filas de tus datos
print(df.head())

# Información general sobre tus datos
print(df.info())

# Estadísticas descriptivas de tus datos
print(df.describe())

# Visualización de histogramas para cada columna numérica
df.hist(bins=20, figsize=(12, 8))
plt.show()

# Matriz de correlación y mapa de calor
correlation_matrix = df.corr()
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm")
plt.title("Matriz de Correlación")
plt.show()

# Box plot para cada columna numérica
plt.figure(figsize=(12, 8))
sns.boxplot(data=df, orient="h")
plt.title("Diagrama de Caja (Box Plot)")
plt.show()

# Visualizar relaciones entre pares de columnas numéricas
sns.pairplot(data=df, diag_kind="kde")
plt.show()

# Gráfico de barras para la variable categórica "Calidad del aire"
plt.figure(figsize=(8, 6))
sns.countplot(data=df, x="CalidadF")
plt.title("Distribución de la Calidad del Aire")
plt.show()

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.model_selection import train_test_split, cross_val_score
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

# Cargar los datos
data = df_con_valores_reemplazados  # Asegúrate de cambiar el nombre del archivo a tu conjunto de datos

# Separar las características (X) y la variable objetivo (y)
X = data[['SO2', 'NO', 'CO', 'PM10', 'O3', 'Fecha']]
y = data['CalidadF']

# Divide los datos en entrenamiento (60%), validación (20%) y prueba (20%)
X_train, X_temp, y_train, y_temp = train_test_split(X, y, test_size=0.4, random_state=42)
X_valid, X_test, y_valid, y_test = train_test_split(X_temp, y_temp, test_size=0.5, random_state=42)

# Crea un modelo SVM con un kernel lineal
svm_model = SVC(kernel='linear', C=1)
svm_model.fit(X_train, y_train)

# Realiza predicciones en el conjunto de prueba
y_valid_pred = svm_model.predict(X_valid)
accuracy_valid = accuracy_score(y_valid, y_valid_pred)
print(f"Precisión en el conjunto de validación: {accuracy_valid:.2f}")

# Realiza predicciones en el conjunto de prueba
y_test_pred = svm_model.predict(X_test)

# Evalúa el rendimiento en el conjunto de prueba
accuracy_test = accuracy_score(y_test, y_test_pred)
print(f"Precisión en el conjunto de prueba: {accuracy_test:.2f}")

# Realiza la validación cruzada con 50 pliegues (folds)
scores = cross_val_score(svm_model, X_train, y_train, cv=50)

# Imprime las puntuaciones de cada pliegue
print("Puntuaciones de validación cruzada:", scores)

# Calcula y muestra la puntuación promedio de la validación cruzada
mean_score = np.mean(scores)
print("Puntuación promedio de validación cruzada:", mean_score)