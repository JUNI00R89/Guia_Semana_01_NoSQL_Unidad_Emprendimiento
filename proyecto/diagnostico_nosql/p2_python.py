"""P2 - Filtrar registros con Python (diagnóstico Semana 1)."""


def seleccionar_pendientes(registros, sector):
    """Retorna los códigos del sector indicado con pendiente exactamente True.

    - No modifica la lista recibida.
    - Si el campo 'pendiente' falta, el registro no se considera pendiente
      (equivale a "sin información confirmada", no a True).
    - Solo acepta el booleano True; la cadena "True" no es válida.
    """
    resultado = []
    for registro in registros:
        if registro.get("sector") == sector and registro.get("pendiente") is True:
            resultado.append(registro["codigo"])
    return resultado


if __name__ == "__main__":
    iniciativas = [
        {"codigo": "INI-001", "sector": "tecnologia", "pendiente": True},
        {"codigo": "INI-002", "sector": "alimentos", "pendiente": True},
        {"codigo": "INI-003", "sector": "tecnologia", "pendiente": False},
        {"codigo": "INI-004", "sector": "tecnologia"},
    ]

    print("Prueba 1 (con resultados), sector 'tecnologia':")
    print("  ", seleccionar_pendientes(iniciativas, "tecnologia"))

    print("Prueba 2 (sin resultados), sector inexistente:")
    print("  ", seleccionar_pendientes(iniciativas, "turismo"))

    print("\nExplicación:")
    print("  - INI-004 no aparece porque le falta el campo 'pendiente'.")
    print("  - No se debe confundir True (booleano) con \"True\" (cadena):")
    print("    bool(\"True\") y bool(\"False\") serían ambos True, lo cual es incorrecto.")
    print("  - 'registros' no se modifica; se construye una lista nueva.")
