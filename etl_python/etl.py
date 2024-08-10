import pandas as pd
from dabatabase import *

def etl():
  # Realizar la extracción de datos
  df = pd.read_sql('SELECT * FROM clientes_transaccional', conexion)

  # Limpieza: Remover duplicados y normalizar nombres
  df.drop_duplicates(inplace=True)
  df['nombre_cliente'] = df['nombre_cliente'].str.upper()

  # Agregación: Resumir datos por región
  df_resumen = df.groupby('nombre_cliente').agg({'id_cliente': 'count', 'region': 'max'}).reset_index()
  df_resumen['duplicados'] = df_resumen['id_cliente']
  del df_resumen['id_cliente']

  crea_tabla_resumen()
  # Insertar los datos transformados en la tabla resumen
  df_resumen.to_sql('resumen', conexion, if_exists='replace', index=False)


if __name__ == "__main__":

  try:
    # Crear la tabla clientes_transaccional
    crear_tabla_transaccional()
    etl()
    # Verificar los resultados de la carga
    df_cargado = pd.read_sql('SELECT * FROM resumen', conexion)
    print(df_cargado)

    # Cerrar la conexión a la base de datos
    conexion.close()
    pass
  except Exception as err :
    print(f'{err}: Por favor elimine el archivo almacen_datos.db y vuelva a ejecutar')
    pass
  