# A2 — Matriz de comparación de modelos NoSQL

Para cada necesidad del caso se propone un modelo/familia NoSQL, su razón vinculada a una consulta, su limitación o costo y una alternativa. Esta es una comparación para argumentar una elección; **NoSQL no es "mejor" en todos los casos**.

| Caso | Modelo/familia propuesta | Razón vinculada a una consulta | Limitación o costo | Alternativa |
|------|--------------------------|--------------------------------|--------------------|-------------|
| Iniciativas de varios sectores (atributos distintos: productos/canal para alimentos, plataforma/entrega para software) | Documental / MongoDB | Q02 pide el detalle completo de una iniciativa con su propuesta de valor y atributos específicos: encaja en un único documento con subdocumentos y arreglos. | Esquema flexible exige disciplina: hay que acordar campos comunes y validar tipos; consultas sobre campos anidados pueden ser más complejas. | SQL con una tabla común y tablas hijas por sector, o colección única con validación JSON Schema. |
| Sesiones temporales (acceso a un portal que expira) | Clave-valor / Redis | Una consulta típica busca "sesión por token" con acceso O(1) por clave y TTL automático. | No hay consultas por campos distintos de la clave; pensado para un patrón de acceso concreto. | Documental con índice sobre `token` y borrado programado, o sesiones en SQL con job de limpieza. |
| Recorridos de relaciones (emprendedores, mentores, habilidades) | Grafos / Neo4j | Consultas del tipo "¿qué mentores conectan a emprendedores con una habilidad?" se resuelven con recorridos de nodos y aristas. | Modelo de datos distinto (nodos/aristas); requiere cambiar el paradigma respecto al resto del sistema. | Documental referenciando IDs, o SQL con tablas intermedias y varios JOIN (menos eficiente en recorridos profundos). |
| Lecturas por dispositivo/periodo (sensores, iniciativa agroindustrial) | Familias de columnas / Cassandra | Escrituras masivas por particiones (dispositivo) y consultas previstas "lecturas del dispositivo X entre fechas". | No es adecuada para consultas ad-hoc; modelar alrededor de consultas fijas obliga a duplicar datos. | Documental con índices por dispositivo+fecha, o series de tiempo especializadas (TimescaleDB, InfluxDB). |

## Situación en la que sería preferible conservar SQL

Cuando la unidad requiera reportes financieros o de seguimiento con **integridad referencial fuerte y transacciones ACID** (por ejemplo, registrar desembolsos o estados de financiación que no deben perderse ni duplicarse), una base relacional ofrece garantías que los modelos NoSQL documentales o clave-valor no dan de forma nativa. Además, si el equipo solo conoce SQL y las consultas son relaciones bien definidas y estables, SQL puede ser la opción más mantenible.

## Dos razones para evaluar documentos (MongoDB) en este caso

1. Las iniciativas tienen atributos variables según el sector; un documento permite representar esa variabilidad sin rediseñar tablas.
2. Q01–Q06 se resuelven consultando iniciativas con su emprendedor y atributos propios: un documento único evita JOINs frecuentes y acompaña el patrón de lectura.

## Una razón para preferir SQL bajo otros requisitos

Si las consultas exigen múltiples relaciones complejas con integridad obligatoria y transacciones multi-tabla, una base relacional con constraints y transacciones es más adecuada.
