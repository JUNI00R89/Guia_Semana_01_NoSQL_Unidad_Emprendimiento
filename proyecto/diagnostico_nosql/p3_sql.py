"""P3 - Consultar relaciones con SQL (diagnóstico Semana 1)."""

import sqlite3

conexion = sqlite3.connect(":memory:")
conexion.executescript(
    """
CREATE TABLE emprendedores(id INTEGER PRIMARY KEY, alias TEXT);
CREATE TABLE iniciativas(
  id INTEGER PRIMARY KEY, emprendedor_id INTEGER, estado TEXT
);
INSERT INTO emprendedores VALUES
  (1, 'Emprendedor A'), (2, 'Emprendedor B'), (3, 'Emprendedor C');
INSERT INTO iniciativas VALUES
  (101, 1, 'activa'), (102, 2, 'archivada'), (103, 1, 'activa');
"""
)

consulta = """
SELECT i.id AS iniciativa_id, e.alias AS emprendedor
FROM iniciativas AS i
JOIN emprendedores AS e
  ON i.emprendedor_id = e.id
WHERE i.estado = 'activa'
ORDER BY i.id;
"""

print("Resultado de la consulta:")
for fila in conexion.execute(consulta).fetchall():
    print("  ", fila)

print("\nExplicación:")
print("  - Se unen 'iniciativas' con 'emprendedores' mediante la clave")
print("    foránea emprendedor_id = emprendedores.id (JOIN).")
print("  - Se filtran solo las iniciativas con estado 'activa'.")
print("  - Se ordenan por el identificador de la iniciativa.")
print("  - La consulta devuelve (iniciativa_id, alias del emprendedor).")

conexion.close()
