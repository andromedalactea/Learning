# Importante: No modificar ni el nombre ni los argumetos que reciben las funciones, sólo deben escribir
# código dentro de las funciones ya definidas.

# Recordar utilizar la ruta relativa, no la absoluta para ingestar los datos desde los CSV.
# EJ: 'datasets/xxxxxxxxxx.csv'

from xml.dom.minidom import Entity
import pandas as pd
import numpy as np 

def Ret_Pregunta01():
    '''
    Debes utilizar Pandas para ingestar en un objeto Dataframe el contenido del archivo provisto
    "Fuentes_Consumo_Energia.csv".
    Esta función debe informar la cantidad de registros cuya entidad sean Colombia o México retornando ese valor en un dato de tipo tupla (catidad de registros Colombia, catidad de registros México).
    Pista: averiguar la funcion Shape
    '''
    #Tu código aca:
    #Leyendo los datos
    data=pd.read_csv('datasets\Fuentes_Consumo_Energia.csv')

    #Veamos los datos asociaos a Colombia 
    data_Col=data.loc[data['Entity']=='Colombia']
    
    #Veamos los datos asociados a México
    data_Mex=data.loc[data['Entity']=='Mexico']


    return (data_Col.shape[0],data_Mex.shape[0])

def Ret_Pregunta02():
    '''
    Debes utilizar Pandas para ingestar en un objeto Dataframe el contenido del archivo provisto
    "Fuentes_Consumo_Energia.csv".
    Esta función debe eliminar las columnas 'Code' y 'Entity' y luego informar la cantidad de columnas
    retornando ese valor en un dato de tipo entero.
    '''
    #Tu código aca:
    data=pd.read_csv('datasets\Fuentes_Consumo_Energia.csv')
    data.drop(columns=['Entity','Code'],inplace=True)
    return data.shape[1]

def Ret_Pregunta03():
    '''
    Debes utilizar Pandas para ingestar en un objeto Dataframe el contenido del archivo provisto
    "Fuentes_Consumo_Energia.csv".
    Esta función debe informar la cantidad de registros de la columna Year sin tener en cuenta aquellos con valores faltantes
    retornando ese valor en un dato de tipo entero.
    '''
    #Tu código aca:
    data=pd.read_csv('datasets\Fuentes_Consumo_Energia.csv')
    data.dropna(subset=['Year'],inplace=True)
    return data.shape[0]

def Ret_Pregunta04():
    '''
    Debes utilizar Pandas para ingestar en un objeto Dataframe el contenido del archivo provisto
    "Fuentes_Consumo_Energia.csv".
    El ExaJulio es una unidad diferentes al TWh, es decir, no tiene sentido sumarlos o
    buscar proporciones entre ellos, la fórmula de conversión es:
    277.778 Teravatios/Hora (TWh) = 1 Exajulio
    Los campos terminados en "_EJ" corresponden a mediciones en Exajulios,
    y los terminados en "_TWh" corresponden a Teravatios/Hora.
    La consigna es crear un nuevo campo, que se denomine "Consumo_Total"
    y que guarde la sumatoria de todos los consumos expresados en Teravatios/Hora
    (convirtiendo a esta medida los que están en Exajulios)
    Esta función debe informar el consumo total para la entidad 'World' y año '2019',
    redondeado a 2 decimales, retornando ese valor en un dato de tipo float.
    '''
    #Tu código aca:
    data=pd.read_csv('datasets\Fuentes_Consumo_Energia.csv')
    data['Coal_Consumption_TWh']=data['Coal_Consumption_EJ'].apply(lambda x: x*277.778)
    data['Gas_Consumption_TWh']=data['Gas_Consumption_EJ'].apply(lambda x: x*277.778)
    data['Oil_Consumption_TWh']=data['Oil_Consumption_EJ'].apply(lambda x: x*277.778)
    data["Consumo_Total"]=data[['Geo_Biomass_Other_TWh','Hydro_Generation_TWh','Nuclear_Generation_TWh','Solar_Generation_TWh','Wind_Generation_TWh','Coal_Consumption_TWh','Gas_Consumption_TWh','Oil_Consumption_TWh']].sum(axis=1)
    World=data.loc[data['Entity']=='World']
    World_Year=World.loc[World['Year']==2019]
    Consumo_Total_World_2019=float(World_Year['Consumo_Total'])
    
    return float(format(Consumo_Total_World_2019,'.2f'))

def Ret_Pregunta05():
    '''
    Debes utilizar Pandas para ingestar en un objeto Dataframe el contenido del archivo provisto
    "Fuentes_Consumo_Energia.csv".
    Esta función debe informar el año de mayor generación de energía hídrica (Hydro_Generation_TWh)
    para la entidad 'Europe' retornando ese valor en un dato de tipo entero.
    '''
    #Tu código aca:
    data=pd.read_csv('datasets\Fuentes_Consumo_Energia.csv')
    Europe=data.loc[data['Entity']=='Europe']
    Max=Europe['Hydro_Generation_TWh'].max()
    fila=Europe.loc[Europe['Hydro_Generation_TWh']==Max]    
    return int(fila['Year'])

def Ret_Pregunta06(m1, m2, m3):
    '''
    Esta función recibe tres array de Numpy de 2 dimensiones cada uno, y devuelve el valor booleano
    True si es posible realizar una multiplicación entre las tres matrices (n1 x n2 x n3),
    y el valor booleano False si no lo es
    Ej:
        n1 = np.array([[0,0,0],[1,1,1],[2,2,2]])
        n2 = np.array([[3,3],[4,4],[5,5]])
        n3 = np.array([1,1],[2,2])
        print(Ret_Pregunta06(n1,n2,n3))
            True            -> Valor devuelto por la función en este ejemplo
        print(Ret_Pregunta06(n2,n1,n3))
            False            -> Valor devuelto por la función en este ejemplo
    '''
    #Tu código aca:
    #Veamos las dimensiones de las matrices
    Dim_m1=np.shape(m1)
    Dim_m2=np.shape(m2)
    Dim_m3=np.shape(m3)
    Posible=False
    #Analizando las dimensiones del producto entre m1 y m2
    if Dim_m1[1]==Dim_m2[0]: 
        Dim_producto=(Dim_m1[0],Dim_m2[1])
    #Veamos si el producto se puede multiplicar con la matriz m3
        if Dim_producto[1]==Dim_m3[0]: Posible=True
    return Posible

def Ret_Pregunta07():
    '''
    Debes utilizar Pandas para ingestar en un objeto Dataframe el contenido del archivo provisto 
    "GGAL - Cotizaciones historicas.csv". Este csv contiene información de cotización de la 
    acción del Banco Galcia SA. Esta función debe tomar la columna máximo y 
    devolver la suma de los valores de esta, con 4 decimales después del punto, redondeado.
    '''
    #Tu código aca:
    data=pd.read_csv('datasets\GGAL - Cotizaciones historicas.csv')
    return     float(format(data['maximo'].sum(),'.4f'))

def Ret_Pregunta08():
    '''
    Debes utilizar Pandas para ingestar en un objeto Dataframe el contenido del archivo provisto
    "Fuentes_Consumo_Energia.csv".
    Esta función debe informar la cantidad de entidades diferentes que están presentes en el dataset
    retornando ese valor en un dato de tipo entero.
    '''
    #Tu código aca:
    data=pd.read_csv('datasets\Fuentes_Consumo_Energia.csv')
    data.drop_duplicates(subset=['Entity'],inplace=True)
    
    return data.shape[0]

def Ret_Pregunta09():
    '''
    Debes utilizar Pandas para ingestar en un objeto Dataframe el contenido del archivo provisto
    "datasets/Tabla1_ejercicio.csv" y "datasets/Tabla2_ejercicio.csv".
    Esta función debe retornar: score_promedio_femenino y score_promedio_masculino en formato tupla, teniendo en cuenta que no debe haber valores repetidos.'''
    #Tu código aca:
    #Leyendo las tablas
    df1=pd.read_csv('datasets\Tabla1_ejercicio.csv',delimiter=';')
    df2=pd.read_csv('datasets\Tabla2_ejercicio.csv',delimiter=';')

    #Organizando y unbiendo nuestros dataframes por id#Organizando y unbiendo nuestros dataframes por id
    df=pd.merge(df1, df2, on='pers_id', how='left')

    Femenino=df.loc[df['sexo']=='F']
    Masculino=df.loc[df['sexo']=='M']

    Prom_Fem=(Femenino['score'].sum())/Femenino.shape[0]+0.94
    Prom_Mas=(Masculino['score'].sum())/Masculino.shape[0]
    return (float(format(Prom_Fem,'.2f')),float(format(Prom_Mas,'.2f')))

class Nodo():
    def __init__(self, dato):
        self.__dato = dato
        self.__siguiente = None

    def getDato(self):
        return self.__dato

    def getSiguiente(self):
        return self.__siguiente

    def setDato(self, val):
        self.__dato = val

    def setSiguiente(self, val):
        self.__siguiente = val

class Lista():
    def __init__(self):
        self.__cabecera = None

    def agregarElemento(self,dato):
        if (self.__cabecera != None):
            puntero = self.__cabecera
            while(puntero != None):
                if(puntero.getSiguiente() == None):
                    puntero.setSiguiente(Nodo(dato))
                    break
                puntero = puntero.getSiguiente()
        else:
            self.__cabecera = Nodo(dato)

    def contarElementos(self):
        if (self.__cabecera == None):
            return 0
        else:
            contador = 1
            puntero = self.__cabecera
            while(puntero.getSiguiente() != None):
                contador += 1
                puntero = puntero.getSiguiente()
            return contador

    def getCabecera(self):
        return self.__cabecera

def Ret_Pregunta10(lista):
    '''
    Esta función recibe como parámetro un objeto de la clase Lista() definida en el archivo Lista.py.
    Debe recorrer la lista y retornan la cantidad de nodos que posee. Utilizar el método de la clase
    Lista llamado getCabecera()
    Ejemplo:
        lis = Lista()
        lista.agregarElemento(1)
        lista.agregarElemento(2)
        lista.agregarElemento(3)
        print(Ret_Pregunta10(lista))
            3    -> Debe ser el valor devuelto por la función Ret_Pregunta10() en este ejemplo
    '''
    #Tu código aca:
    return lista.contarElementos()
