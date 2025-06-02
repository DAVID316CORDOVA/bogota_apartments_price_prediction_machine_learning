import pandas as pd 
import joblib
from sklearn.ensemble import GradientBoostingRegressor
import pickle
import numpy as np 

pd.options.display.float_format="{:.2f}".format

df=pd.read_csv("dataset_final.csv")

print(df.head())

df=df[['Precio','Área (m²)', 
'Habitaciones_1.0', 
 'Habitaciones_2.0', 
 'Habitaciones_3.0', 
 'Habitaciones_4.0', 
 'Habitaciones_5.0', 
 'Baños_1.0',
 'Baños_2.0', 
 'Baños_3.0', 
 'Baños_4.0',
 'Baños_5.0', 
 'Antigüedad_menor-a-1-anio', 
 'Antigüedad_de-1-a-8-anios',
 'Antigüedad_de-9-a-15-anios', 
 'Antigüedad_de-16-a-30-anios', 
 'Antigüedad_mas-de-30-anios', 
 'Estrato_2.0', 
 'Estrato_3.0', 
 'Estrato_4.0', 
 'Estrato_5.0', 
 'Estrato_6.0', 
 'Parqueaderos_0.0', 
 'Parqueaderos_1.0', 
 'Parqueaderos_2.0', 
 'Parqueaderos_3.0', 
 'Parqueaderos_4.0',
 'LOCALIDAD_BARRIOS UNIDOS',
 'LOCALIDAD_BOSA', 
 'LOCALIDAD_CHAPINERO', 
 'LOCALIDAD_CIUDAD BOLIVAR', 
 'LOCALIDAD_ENGATIVA' , 
 'LOCALIDAD_FONTIBON', 
 'LOCALIDAD_KENNEDY', 
 'LOCALIDAD_PUENTE ARANDA', 
 'LOCALIDAD_SANTAFE', 
 'LOCALIDAD_SUBA', 
 'LOCALIDAD_TEUSAQUILLO', 
 'LOCALIDAD_USAQUEN', 
 'LOCALIDAD_USME']]


#Defining X and y

X=df.drop(columns=["Precio"])
y=df[["Precio"]]


#Standardization the data

from sklearn.preprocessing import StandardScaler

scaler_x=StandardScaler()
scaler_y=StandardScaler()

scaler_x.fit(X)
scaler_y.fit(y)

X_scaled=pd.DataFrame(scaler_x.transform(X),columns=X.columns)
y_scaled=pd.DataFrame(scaler_y.transform(y),columns=y.columns)


# Define los hiperparámetros

# Crea el modelo
# Define el modelo con todos los hiperparámetros
gbr = GradientBoostingRegressor(
    learning_rate=np.float64(0.024265383115208886),
    max_depth=7,
    max_features='sqrt',
    min_samples_leaf=1,
    min_samples_split=5,
    n_estimators=373,
    subsample=np.float64(0.5000518092504698),
    random_state=42  # Recomendado para reproducibilidad
)

# Entrena el modelo
gbr.fit(X_scaled, y_scaled)


# Guarda el modelo
with open('modelo_gbr.pkl', 'wb') as archivo:
    pickle.dump(gbr, archivo)
    
    
joblib.dump(scaler_x,"scaler_x.pkl")


joblib.dump(scaler_y,"scaler_y.pkl")


print("Modelo guardado")


    



