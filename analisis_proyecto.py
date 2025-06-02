import pandas as pd

df=pd.read_csv("propiedades.csv")

print("ELIMINANDO DUPLICADOS")

df=df.drop_duplicates()

print("Tamaño luego de eliminar duplicados")

print("ANALIZANDO LOS VALORES NULOS")

df.isnull().sum().sort_values(ascending=False)

print("ELIMINANDO LAS COLUMNAS CARACTERISTICAS, ESTADO, CONSTRUCTOR Y NOMBRE DEL PROYECTO")

df2=df.drop(columns=["Características","Estado","Constructor","Nombre del Proyecto"])

print("ELIMINANDO FILAS CON ESTRADO NULO")
df2=df2[~df2["Estrato"].isnull()]

### Llenamos con 0 los datos donde parqueadero tiene datos nulos
df2["Parqueaderos"]=df2["Parqueaderos"].fillna(0)

## Eliminamos las filas que muestren un valor NULL en la columna habitaciones

df2=df2.dropna()

### Verificando los nulos

df2.isnull().sum().sort_values(ascending=False)


print("SE CREA LA COLUMNA CATEGORIA")

df2["Categoria"] = df2["URL Proyecto"].str.extract(r"/([^/]+)/")

print("CON LA COLUMNA CATEGORIA CREAMOS LA COLUMNA TIPO")

df2['Tipo'] = df2['Categoria'].apply(lambda x: 'departamento' if 'apartamento' in x.lower()
                                   else 'casa' if 'casa' in x.lower()
                                   else 'otro')


print("NOS QUEDAMOS SOLO CON LOS DATOS DE TIPO DEPARTAMENTO DADO QUE SE ENCUENTRAN EN MAYOR PROPORCION")

df2=df2[df2["Tipo"]=="departamento"]

print("ELIMINIANDO LAS COLUMNAS URL DEL PROYECTO, CATEGORIA Y TIPO")

df3=df2.drop(columns=["Tipo","URL Proyecto","Categoria"])

# Extraer solo el nombre del barrio (texto antes de la primera coma)
print("CREAMOS UNA NUEVA COLUMNA LLAMADA BARRIO")
df3['barrio'] = df3['Ubicación'].str.split(',').str[0]

# Mostrar los datos resultantes

df3[['barrio', 'Ubicación']].head()

##Contar la cantidad de repeticiones por ubicación
counts = df3['barrio'].value_counts()

print("ELIMINANDO LAS FILAS CUYO BARRIO APARECE MENOS DE 10 VECES EN EL DATASET")

# Filtrar solo las ubicaciones con 10 o más repeticiones
df4 = df3[df3['barrio'].isin(counts[counts >= 10].index)]
print("CANTIDAD DE DATOS LUEGO DEL FILTRO")
df4.shape


print("CONVIRTIENDO LOS DATOS A MAYÚSCULA PREVIO AL JOIN")
df5["barrio"]=df5["barrio"].str.upper()print("LEYENDO EL ARCHIVO BARRIO LOCALIDADES PARA HCER EL JOIN CON LA TABLA PRINCIPAL")
localidades=pd.read_excel("barrios_localidades.xlsx")[["MAYUSCULAS BARRIO","LOCALIDAD"]]
localidades=localidades.rename(columns={'MAYUSCULAS BARRIO': 'barrio'})


# Realizar el merge para agregar la localidad
print("REALIZANDO EL MERGE PARA OBTENER LA LOCALIDAD DE CADA BARRIO")
df6=df5.merge(localidades, on='barrio', how='left').drop_duplicates()

print("ELIMINANDO LAS FILAS DONDE LA LOCALIDAD ES UN NULL")
df7=df6[~df6["LOCALIDAD"].isnull()]

print("ELIMINANDO LAS COLUMNAS UBICACION Y BARRIO")
df8=df7.drop(columns=["Ubicación","barrio"])

## SEGMENTACION DEL DATASET LUEGO DEL ANALISIS DE GRAFICOS
### NOS QUEDAMOS CON LAS MUESTRAS QUE TENGAN ENTRE 1 Y 5 HABITACIONES
df8["Habitaciones"]=df8["Habitaciones"].astype(float)
df8=df8[(df8["Habitaciones"]>=1) & (df8["Habitaciones"]<=5)]


### NOS QUEDAMOS CON LAS MUESTRAS QUE TENGAN ENTRE 1 Y 5 BAÑOS
df8["Baños"]=df8["Baños"].astype(float)
df8=df8[(df8["Baños"]>=1) & (df8["Baños"]<=5)]

## DEJAMOS EL DATASET CON DATOS QUE MUESTREN ESTRATOS ENTRE 2 Y 6
df8["Estrato"]=df8["Estrato"].astype(float)
df8=df8[(df8["Estrato"]>=2) & (df8["Estrato"]<=6)]


## DEJAMOS EL DATASET CON DATOS QUE MUESTREN INFORMACIÓN DE MÁXIMO 5 PARQUEADEROS
df8["Parqueaderos"]=df8["Parqueaderos"].astype(float)
df8=df8[(df8["Parqueaderos"]>=0) & (df8["Parqueaderos"]<=5)]


## REDUCIMOS EL DATASET A DEPARTAMENTOS QUE TENGAN ENTRE 20 Y 300 M2
df8["Área (m²)"]=df8["Área (m²)"].astype(float)
df8=df8[(df8["Área (m²)"]>=20) & (df8["Área (m²)"]<=300)]

df10=df8[ (df8["Precio"]>=50000000)  & (df8["Precio"]<10000000000)]

# CREANDO NUEVAS COLUMNAS CON LA AYUDA DE LA FUNCION GET DUMMIES
new_features=pd.get_dummies(df10[categorical]).astype(int)

#Concating the new features with the first dataframe
df11=pd.concat([df10,new_features],axis=1)

#Dropping the categorical columns due to they were transformed in new columns
df11=df11.drop(columns=categorical)

print("DATASET FINAL")

df11.head()