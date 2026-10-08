# Parte A — Diagnóstico teórico (10 preguntas)

1. **¿Qué representan una tabla, una fila y una clave primaria?**
   - Una tabla es una colección organizada de registros sobre una misma entidad; una fila (registro) es una instancia concreta de esa entidad; la clave primaria es el campo o conjunto de campos que identifica de forma única cada fila. Ejemplo: en una tabla de iniciativas del emprendimiento, cada fila es una iniciativa (p. ej. "EcoEmpaque") y su clave primaria sería `codigo` (INI-001), que no se repite.

2. **¿Para qué sirve una clave foránea? ¿Qué problema genera una iniciativa que referencia a un emprendedor inexistente?**
   - La clave foránea vincula una fila de una tabla con la clave primaria de otra, garantizando integridad referencial. Si una iniciativa referencia a un emprendedor inexistente, se rompe esa integridad: no se sabe quién está a cargo, las consultas con JOIN fallarían al perder la fila y el historial queda huérfano.

3. **¿Qué devuelve `SELECT codigo FROM iniciativas WHERE sector = 'tecnologia';`? ¿Modifica registros?**
   - Devuelve únicamente la columna `codigo` de las iniciativas cuyo `sector` es `'tecnologia'` (un conjunto de lectura). No modifica registros: es una consulta de solo lectura; para modificar datos se usan `UPDATE`, `INSERT` o `DELETE`.

4. **Diferencia una lista y un diccionario en Python. ¿Qué estructura usarías para una iniciativa y para varias?**
   - Una lista es una secuencia ordenada accesible por índice; un diccionario es una colección de pares clave–valor. Para una iniciativa usaría un diccionario (campos con nombre: `codigo`, `sector`, `etapa`); para varias iniciativas usaría una lista de diccionarios.

5. **¿Son equivalentes `false` y `"false"` en JSON?**
   - No. `false` es un booleano (valor lógico verdadero/falso). `"false"` es una cadena de texto con cinco caracteres. El tipo de cada valor es distinto: `bool` frente a `string`.

6. **Diferencia campo ausente, campo con `null` y campo con cadena vacía. Propón un ejemplo.**
   - Campo ausente: la clave no existe en el documento (`"fecha_realizacion"` no aparece). Campo con `null`: la clave existe pero su valor es nulo explícito (`"fecha_realizacion": null` → la asesoría aún no se ha realizado). Cadena vacía: la clave existe con texto de longitud cero (`"nombre": ""` → dato pendiente o inválido). Ejemplo: en una asesoría, `fecha_realizacion` ausente indica que el sistema nunca registró el campo; `null` indica que se esperaba pero no ocurrió; `""` indica que alguien escribió un texto vacío.

7. **¿Qué ventaja tiene una función que retorna datos frente a otra que solo los imprime?**
   - Una función que retorna datos permite reutilizar el resultado: guardarlo en una variable, pasarlo a otra función, filtrarlo o probarlo con pruebas automáticas. Una que solo imprime muestra en pantalla pero el dato se pierde para el programa.

8. **Si falla la lectura de un archivo JSON, ¿qué revisarías antes de cambiar el programa?**
   - Revisaría: que la ruta del archivo sea correcta y exista; que la codificación sea válida (UTF-8); que el contenido sea JSON bien formado (comillas dobles, comas, sin espacios de más tras el último elemento); que el archivo no esté vacío o corrupto; y el mensaje de error exacto (`json.JSONDecodeError`) para localizar la línea. Primero corregiría los datos, no el programa.

9. **¿Qué información reconoces en `2026-10-06T13:00:00Z`? ¿Qué ambigüedades evita frente a `06/10/26 8:00`?**
   - Es una fecha y hora en formato ISO 8601: año 2026, mes 10, día 06, 13:00:00 UTC (la `Z` indica UTC; en Colombia serían las 08:00). Evita ambigüedades de formato regional: en `06/10/26 8:00` no queda claro si es 6 de octubre o 10 de junio, ni la zona horaria, ni el siglo completo del año.

10. **Se publicó por error una contraseña en Git. ¿Qué acciones propondrías? ¿Es suficiente borrarla del archivo actual?**
    - No es suficiente borrarla del archivo actual: la contraseña queda en el historial de commits y cualquiera con acceso al repositorio puede recuperarla. Acciones: rotar/cambiar la contraseña de inmediato, notificar al responsable del sistema, eliminar el secreto del historial (por ejemplo con git filter-repo o BFG) si el repositorio es público, revisar accesos no autorizados y documentar el incidente. Agregar el archivo al `.gitignore` después no protege una contraseña ya expuesta.

## Autoevaluación

- **Puedo realizar:** analizar consultas SQL básicas, manipular listas y diccionarios en Python, interpretar documentos JSON y reconocer tipos de datos.
- **Necesito reforzar:** manejo preciso de fechas con zona horaria, tipos de datos en JSON vs Python y buenas prácticas de seguridad con credenciales.
- **Mi primera acción de mejora será:** practicar la conversión JSON ↔ Python y registrar correctamente errores como `JSONDecodeError` antes de corregir código.
