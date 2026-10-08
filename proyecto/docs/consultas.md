# A3 — Consultas Q01–Q06 (lenguaje natural)

Cada consulta se define con: ID, necesidad, actor, filtros, campos de salida, orden y frecuencia estimada. La frecuencia es una **hipótesis**, no una estadística real.

---

## Q01 — Iniciativas activas por sector y etapa didáctica

- **ID:** Q01
- **Necesidad:** saber cuántas iniciativas están activas, agrupadas por su sector y su etapa didáctica.
- **Actor:** coordinador de la Unidad de Emprendimiento.
- **Filtros:** estado de iniciativa = `activa`.
- **Campos de salida:** sector, etapa, cantidad de iniciativas.
- **Orden:** sector ascendente, etapa ascendente.
- **Frecuencia estimada:** diaria (hipótesis, para revisión del seguimiento).

## Q02 — Detalle de una iniciativa con propuesta de valor y atributos específicos

- **ID:** Q02
- **Necesidad:** consultar toda la información de una iniciativa concreta: propuesta de valor y atributos propios de su sector.
- **Actor:** asesor o tutor de la iniciativa.
- **Filtros:** código de iniciativa = un valor concreto (p. ej. `INI-DEMO-002`).
- **Campos de salida:** código, nombre, sector, etapa, estado, propuesta de valor, atributos específicos del sector.
- **Orden:** no aplica (un solo documento).
- **Frecuencia estimada:** varias veces al día (hipótesis).

## Q03 — Iniciativas de un emprendedor responsable por estado

- **ID:** Q03
- **Necesidad:** listar las iniciativas de las que es responsable un emprendedor, agrupadas o filtradas por estado.
- **Actor:** el propio emprendedor o el coordinador.
- **Filtros:** código/alias del emprendedor responsable y, opcionalmente, estado (`activa`/`archivada`).
- **Campos de salida:** código de iniciativa, nombre, sector, etapa, estado.
- **Orden:** estado y luego código de iniciativa.
- **Frecuencia estimada:** semanal (hipótesis).

## Q04 — Asesorías programadas pendientes por rango de fechas y modalidad

- **ID:** Q04
- **Necesidad:** identificar las asesorías con estado `programada` dentro de un rango de fechas y una modalidad (virtual/presencial).
- **Actor:** coordinador de agenda.
- **Filtros:** estado = `programada`; `fecha_programada` entre fecha_inicio y fecha_fin; modalidad = valor elegido.
- **Campos de salida:** código de asesoría, iniciativa, emprendedor, fecha_programada, modalidad, temas.
- **Orden:** fecha_programada ascendente.
- **Frecuencia estimada:** diaria (hipótesis).

## Q05 — Historial de asesorías de una iniciativa

- **ID:** Q05
- **Necesidad:** ver todas las asesorías (programadas, realizadas y canceladas) de una iniciativa a lo largo del tiempo.
- **Actor:** tutor de la iniciativa.
- **Filtros:** código de iniciativa concreto.
- **Campos de salida:** código de asesoría, tema, estado, fecha_programada, fecha_realizacion, modalidad, asesor asignado.
- **Orden:** fecha_programada ascendente.
- **Frecuencia estimada:** por reunión de seguimiento (hipótesis: semanal).

## Q06 — Cantidad de asesorías realizadas por sector de iniciativa y mes

- **ID:** Q06
- **Necesidad:** medir cuántas asesorías se realizaron en cada mes, agrupadas por el sector de la iniciativa.
- **Actor:** coordinación, para reportes de gestión.
- **Filtros:** estado = `realizada`; mes derivado de `fecha_realizacion`.
- **Campos de salida:** sector, mes/año, cantidad de asesorías realizadas.
- **Orden:** mes ascendente y sector ascendente.
- **Frecuencia estimada:** mensual (hipótesis para cierre de indicadores).

**Aclaración sobre Q06:** aquí el "sector" se interpreta como el **sector actual de la iniciativa** (valor vigente del campo `sector`). Esta decisión es una hipótesis de trabajo porque la guía no especifica si debe usarse el sector actual o el que tenía la iniciativa en el momento de la asesoría; si fuera el histórico, haría falta conservar el sector en cada asesoría o usar versionado. Se retomará al modelar en la Semana 2.
