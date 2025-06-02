
import joblib
import pickle

diccionario= {'Área (m²)': 0, 
              'Habitaciones_1.0': 1, 
 'Habitaciones_2.0': 2, 
 'Habitaciones_3.0': 3, 
 'Habitaciones_4.0': 4, 
 'Habitaciones_5.0': 5, 
 'Baños_1.0': 6,
 'Baños_2.0': 7, 
 'Baños_3.0': 8, 
 'Baños_4.0': 9,
 'Baños_5.0': 10, 
 'Antigüedad_menor-a-1-anio': 11, 
 'Antigüedad_de-1-a-8-anios': 12,
 'Antigüedad_de-9-a-15-anios': 13, 
 'Antigüedad_de-16-a-30-anios': 14, 
 'Antigüedad_mas-de-30-anios': 15, 
 'Estrato_2.0': 16, 
 'Estrato_3.0': 17, 
 'Estrato_4.0': 18, 
 'Estrato_5.0': 19, 
 'Estrato_6.0': 20, 
 'Parqueaderos_0.0': 21, 
 'Parqueaderos_1.0': 22, 
 'Parqueaderos_2.0': 23, 
 'Parqueaderos_3.0': 24, 
 'Parqueaderos_4.0': 25,
 'LOCALIDAD_BARRIOS UNIDOS': 26,
 'LOCALIDAD_BOSA': 27, 
 'LOCALIDAD_CHAPINERO': 28, 
 'LOCALIDAD_CIUDAD BOLIVAR': 29, 
 'LOCALIDAD_ENGATIVA': 30, 
 'LOCALIDAD_FONTIBON': 31, 
 'LOCALIDAD_KENNEDY': 32, 
 'LOCALIDAD_PUENTE ARANDA': 33, 
 'LOCALIDAD_SANTAFE': 34, 
 'LOCALIDAD_SUBA': 35, 
 'LOCALIDAD_TEUSAQUILLO': 36, 
 'LOCALIDAD_USAQUEN': 37, 
 'LOCALIDAD_USME': 38}


#Saving a dictionary with all the columns
joblib.dump(diccionario, "indice_diccionario.pkl")


print("Diccionario de columnas:")

print(diccionario)    