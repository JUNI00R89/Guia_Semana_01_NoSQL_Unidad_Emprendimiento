# NoSQL Unidad de Emprendimiento SENA — Semana 1

Proyecto de la Semana 1 de Bases de Datos NoSQL (ADSO — SENA CTMA, instructor Wilson Castro Gil).

## Objetivo de la Semana 1

Comparar modelos de datos, interpretar documentos y demostrar una conexión autenticada con evidencias reproducibles, siguiendo la guía "Guía de aprendizaje de Bases de Datos NoSQL - Semana 1 - Unidad de Emprendimiento del SENA".

## Situación problema

Una Unidad de Emprendimiento del SENA ficticia acompaña iniciativas de sectores como tecnología, alimentos y economía circular. Los registros de emprendedores, iniciativas y asesorías están dispersos en hojas de cálculo y documentos separados, lo que dificulta consultar avances, historiales y asesorías pendientes. El reto es diseñar una base de datos (a explorar con MongoDB) que registre emprendedores, sus iniciativas y las asesorías asociadas.

## Actividades realizadas

- **A1 — Diagnóstico:** teoría (10 preguntas), JSON (P1), Python (P2), SQL (P3) y autoevaluación.
- **A2 — Comparación de modelos:** matriz de selección (MongoDB, Redis, Neo4j, Cassandra y caso SQL).
- **A3 — Reglas y consultas:** reglas del caso y Q01–Q06 en lenguaje natural.
- **A4 — Entorno MongoDB:** conexión autenticada y exploración del documento demo `ASE-DEMO-001`.
- **A5 — Socialización:** presentación de E01 y nivelación.

## Estructura de carpetas

```
proyecto/
├── docs/
│   ├── matriz_modelos.md
│   ├── consultas.md
│   ├── reglas.md
│   ├── entorno.md
│   ├── lista_chequeo_E01.md
│   └── socializacion_A5.md
├── scripts/
│   └── 01_explorar.js
├── diagnostico_nosql/
│   ├── teoria.md
│   ├── p1_json.py
│   ├── p2_python.py
│   └── p3_sql.py
├── evidencias/
├── .gitignore
└── README.md
```

## Cómo ejecutar el diagnóstico

Requiere Python 3 (solo biblioteca estándar):

```bash
cd diagnostico_nosql
python p1_json.py
python p2_python.py
python p3_sql.py
```

## Cómo ejecutar 01_explorar.js

Desde la carpeta `scripts/`, con el servidor MongoDB autenticado disponible:

```bash
mongosh "mongodb://127.0.0.1:27017/emprendimiento_sena_lab" \
  --username aprendiz_nosql \
  --authenticationDatabase emprendimiento_sena_lab \
  --file 01_explorar.js
```

En Windows, si `mongosh` no está en el PATH, usa la ruta completa:
PowerShell: `& "C:\Users\Sena\mongosh\mongosh-2.5.0-win32-x64\bin\mongosh.exe" "mongodb://127.0.0.1:27017/emprendimiento_sena_lab" --username aprendiz_nosql --authenticationDatabase emprendimiento_sena_lab --file scripts\01_explorar.js`

Alternativamente, copia y pega el contenido del archivo dentro de una sesión de mongosh.

## Cómo conectarse a MongoDB

1. Verificar el cliente: `mongosh --version`
2. Conectar con la cuenta de práctica (sin escribir la contraseña en el comando):
   `mongosh "mongodb://127.0.0.1:27017/emprendimiento_sena_lab" --username aprendiz_nosql --authenticationDatabase emprendimiento_sena_lab`
3. Introducir la contraseña en el prompt.
4. Dentro de mongosh: `db.runCommand({ping: 1})`

Compass: configura la misma cuenta y base de autenticación; localiza `emprendimiento_sena_lab.asesorias_demo`.

## Evidencias

- `docs/entorno.md`: SO, versiones, base de datos, usuario (sin contraseña), comandos, resultados y errores.
- `evidencias/`: capturas y salidas reales de las ejecuciones. No se incluyen capturas inventadas.

### Evidencia: salida de `01_explorar.js` (ejecución real)

```text
{
  _id: 'ASE-DEMO-001',
  emprendedor_alias: 'Emprendedor ficticio 01',
  iniciativa: {
    codigo: 'INI-DEMO-001',
    nombre: 'EcoEmpaque',
    sector: 'economia_circular'
  },
  temas: [ 'propuesta de valor', 'validacion de clientes' ],
  modalidad: 'virtual',
  estado: 'programada',
  requiere_seguimiento: true,
  fecha_programada: ISODate('2026-10-08T13:00:00.000Z'),
  fecha_realizacion: null
}
Conteo ASE-DEMO-001: 1
fecha_programada es Date: true
typeof emprendedor_alias: string
typeof requiere_seguimiento: boolean
temas es arreglo: true
iniciativa es subdocumento: true
Conteo ASE-DEMO-002: 1
ASE-DEMO-002 fecha_programada es Date: true
ASE-DEMO-002 sector: alimentos
```

### Evidencia: salida del diagnóstico (ejecución real)

```text
# p1_json.py
1) Intento de carga del JSON original:
   Error inicial: Expecting value: line 1 column 31 (char 30)
2) Resultado correcto al cargar el JSON corregido:
   {'codigo': 'INI-001', 'activa': True, 'intereses': ['Validar mercado']}
3) Campos y tipos:
   codigo = INI-001 -> tipo: str
   activa = True -> tipo: bool

# p2_python.py
Prueba 1 (con resultados), sector 'tecnologia':
   ['INI-001']
Prueba 2 (sin resultados), sector inexistente:
   []

# p3_sql.py
Resultado de la consulta:
   (101, 'Emprendedor A')
   (103, 'Emprendedor A')
```

Versiones registradas en esta máquina: Windows 10 Pro 10.0.19045, Python 3.14.8, Git 2.55.0, mongosh 2.5.0, MongoDB Server 7.0.43.

## Seguridad

- No se guardan contraseñas en archivos ni comandos.
- `.gitignore` incluye `.env`, `secrets/`, `.venv/`, `__pycache__/`, `*.log`.
- Una contraseña ya subida a Git no queda protegida agregándola luego al `.gitignore`: se debe rotar y corregir el incidente.

## Continuidad hacia Semana 2

En la Semana 2 se decidirá el modelo definitivo: colecciones `emprendedores`, `iniciativas` y `asesorias`, referencias vs documentos embebidos, y la construcción completa del modelo con datos de ejemplo.
