# API — Unidad de Emprendimiento SENA

API REST con **FastAPI + SQLite**. Dos tablas relacionadas (1 a N):

```
emprendedores (1) ──< iniciativas (N)
```

- `emprendedores`: id, alias (único), ciudad
- `iniciativas`: id, codigo (único), nombre, sector, etapa, estado, emprendedor_id (FK → emprendedores.id)

## Instalar

```bash
pip install -r requirements.txt
```

## Ejecutar

```bash
cd api
uvicorn main:app --reload
```

Documentación interactiva: <http://127.0.0.1:8000/docs>

## Endpoints

| Método | Ruta | Descripción |
|---|---|---|
| POST | `/emprendedores` | Crear emprendedor |
| GET | `/emprendedores` | Listar emprendedores |
| GET | `/emprendedores/{id}` | Obtener uno |
| PUT | `/emprendedores/{id}` | Actualizar |
| DELETE | `/emprendedores/{id}` | Eliminar (bloquea si tiene iniciativas) |
| GET | `/emprendedores/{id}/iniciativas` | Iniciativas de un emprendedor (relación) |
| POST | `/iniciativas` | Crear iniciativa (valida que exista el emprendedor) |
| GET | `/iniciativas?estado=activa` | Listar/filtrar por estado |
| GET | `/iniciativas/{id}` | Obtener una |
| PUT | `/iniciativas/{id}` | Actualizar |
| DELETE | `/iniciativas/{id}` | Eliminar |

## Ejemplo con curl

```bash
curl -X POST http://127.0.0.1:8000/emprendedores \
  -H "Content-Type: application/json" \
  -d '{"alias":"Emprendedor ficticio 01","ciudad":"Bogota"}'

curl -X POST http://127.0.0.1:8000/iniciativas \
  -H "Content-Type: application/json" \
  -d '{"codigo":"INI-001","nombre":"EcoEmpaque","sector":"economia_circular","etapa":"validacion","estado":"activa","emprendedor_id":1}'

curl http://127.0.0.1:8000/emprendedores/1/iniciativas
```
