# A4 — Registro del entorno MongoDB

> Completa este archivo con los datos reales de tu computador al ejecutar los comandos. No incluyas contraseñas ni capturas inventadas.

## Sistema y versiones

| Elemento | Valor |
|----------|-------|
| Sistema operativo | Microsoft Windows 10 Pro 10.0.19045 |
| Versión de Python | Python 3.14.8 |
| Versión de Git | git version 2.55.0.windows.5 |
| Versión de mongosh | 2.5.0 |
| Versión del servidor MongoDB | 7.0.43 |
| Base de datos | `emprendimiento_sena_lab` |
| Usuario utilizado | `aprendiz_nosql` (sin contraseña) |

## Comandos ejecutados

```bash
python --version
git --version
mongosh --version

mongosh "mongodb://127.0.0.1:27017/emprendimiento_sena_lab" \
  --username aprendiz_nosql \
  --authenticationDatabase emprendimiento_sena_lab
```

Dentro de mongosh:

```javascript
db = db.getSiblingDB("emprendimiento_sena_lab");
db.runCommand({ping: 1});
db.getName();
```

## Resultados esperados

- Conexión autenticada correcta con usuario de práctica (no administrativa).
- `ping: 1` con ok: 1.
- `db.getName()` → `emprendimiento_sena_lab`.
- Al ejecutar `scripts/01_explorar.js`:
  - existe el documento `ASE-DEMO-001` en `emprendimiento_sena_lab.asesorias_demo`;
  - conteo por ID igual a 1;
  - `fecha_programada` es Date (true con `instanceof Date`);
  - tipos identificados: cadena (`emprendedor_alias`), booleano (`requiere_seguimiento`), arreglo (`temas`), subdocumento (`iniciativa`), Date (`fecha_programada`).

## Por qué la demo no es el modelo definitivo

`ASE-DEMO-001` es un documento único de exploración con campos fijos y datos mínimos. Todavía no representa colecciones `emprendedores`, `iniciativas` y `asesorias`, ni reglas de unicidad, referencias entre entidades ni validación de tipos. Se usará para experimentar sin confundirlo con el diseño final, que se definirá en la Semana 2.

## Cómo comprobarlo en MongoDB Compass

1. Abrir Compass y crear una conexión local con la misma URI.
2. Usar la cuenta de práctica (`aprendiz_nosql`) y base de autenticación `emprendimiento_sena_lab`.
3. Localizar la base `emprendimiento_sena_lab` y dentro la colección `asesorias_demo`.
4. Verificar el documento `ASE-DEMO-001` y sus tipos (`fecha_programada` tipo Date, no String).
5. Si no está disponible, hacer la verificación desde mongosh con los comandos anteriores.

## Errores encontrados y cómo se solucionaron

| Error | Qué se revisó | Solución |
|-------|---------------|----------|
| (completar) p. ej. `Authentication failed` | Usuario, contraseña, base de autenticación | Confirmar los tres datos con el instructor; no usar la cuenta administrativa |
| (completar) p. ej. `MongoNetworkError: connection refused` | Servicio, dirección y puerto | Verificar que el servidor esté iniciado; no desactivar autenticación |
| (completar) p. ej. fecha almacenada como texto | Construcción del valor | Usar `new Date("...")` en el documento |

## Transferencia a 01_explorar.js (ASE-DEMO-002)

Se creó una copia del script cambiando:

- `_id`: `ASE-DEMO-001` → `ASE-DEMO-002`
- `iniciativa.codigo`: `INI-DEMO-001` → `INI-DEMO-002`
- `iniciativa.nombre`: "EcoEmpaque" → "Sabores Locales"
- `iniciativa.sector`: `economia_circular` → `alimentos`

Debe cambiar: el `_id`, los datos del nombre y sector, y los valores mostrados. Debe conservar el mismo tipo: `fecha_programada` sigue siendo Date, `temas` sigue siendo arreglo, `iniciativa` sigue siendo subdocumento, `requiere_seguimiento` sigue siendo booleano. El conteo por cada ID debe seguir siendo 1.
