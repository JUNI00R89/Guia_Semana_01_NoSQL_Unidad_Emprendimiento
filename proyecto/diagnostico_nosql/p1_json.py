"""P1 - Corregir y leer JSON (diagnóstico Semana 1).

Se conserva la primera versión fallida como evidencia.
"""

import json

# Primera versión (fallida): True y None son de Python, no de JSON;
# la coma al final del arreglo es inválida en JSON.
texto_original = '{"codigo":"INI-001", "activa":True, "intereses":["Validar mercado",]}'

print("1) Intento de carga del JSON original:")
try:
    json.loads(texto_original)
except json.JSONDecodeError as error:
    print("   Error inicial:", error)

# Corrección sin cambiar la intención del documento.
texto_corregido = '{"codigo":"INI-001", "activa":true, "intereses":["Validar mercado"]}'

print("\n2) Resultado correcto al cargar el JSON corregido:")
datos = json.loads(texto_corregido)
print("  ", datos)

print("\n3) Campos y tipos:")
print("   codigo =", datos["codigo"], "-> tipo:", type(datos["codigo"]).__name__)
print("   activa =", datos["activa"], "-> tipo:", type(datos["activa"]).__name__)

print("\n4) Explicación de las correcciones:")
print("   - 'True' (Python) se cambió por 'true' (JSON).")
print("   - Se eliminó la coma final dentro del arreglo de 'intereses'.")
print("   - Se mantuvo la intención: mismo código, mismo estado activo,")
print("     misma lista de intereses.")
