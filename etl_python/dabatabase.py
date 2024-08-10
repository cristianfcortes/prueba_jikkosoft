import sqlite3

# Conexión a la base de datos SQLite (se creará si no existe)
conexion = sqlite3.connect('almacen_datos.db')
cursor = conexion.cursor()

def crear_tabla_transaccional():
  cursor.execute('''
    CREATE TABLE clientes_transaccional (
        id_cliente INTEGER PRIMARY KEY,
        nombre_cliente TEXT NOT NULL,
        region TEXT NOT NULL
    )
    ''')

  # Insertar 10 registros de ejemplo
  clientes = [
      (1, 'Juan Perez', 'Norte'),
      (2, 'Maria Lopez', 'Sur'),
      (3, 'Carlos Gomez', 'Este'),
      (4, 'Ana Ramirez', 'Oeste'),
      (5, 'Luis Fernandez', 'Norte'),
      (6, 'Elena Martinez', 'Sur'),
      (7, 'Ricardo Diaz', 'Este'),
      (8, 'Ana Ramirez', 'Oeste'),
      (9, 'Juan Perez', 'Norte'),
      (10, 'Carmen Alvarez', 'Sur')
  ]

  cursor.executemany('''
  INSERT INTO clientes_transaccional (id_cliente, nombre_cliente, region)
  VALUES (?, ?, ?)
  ''', clientes)

  # Guardar los cambios
  conexion.commit()
  

def crea_tabla_resumen():
  # Crear la tabla resumen en la base de datos del almacén de datos
  cursor.execute('''
  CREATE TABLE IF NOT EXISTS resumen (
      nombre_cliente TEXT NOT NULL,
      region TEXT NOT NULL,
      duplicados INTEGER NOT NULL
  )
  ''')
