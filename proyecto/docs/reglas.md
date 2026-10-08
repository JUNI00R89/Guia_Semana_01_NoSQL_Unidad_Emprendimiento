# Reglas del caso — Unidad de Emprendimiento SENA

## Reglas funcionales

1. **Códigos únicos.** Cada emprendedor, iniciativa y asesoría tiene un código único (p. ej. `EMP-…`, `INI-…`, `ASE-…`).
2. **Responsable existente.** Cada iniciativa tiene un emprendedor responsable existente; una persona puede representar varias iniciativas.
3. **Vínculo de asesorías.** Cada asesoría pertenece a una iniciativa existente y registra el código ficticio del asesor que la atiende.
4. **Dominios controlados.**
   - Sectores: `tecnologia`, `alimentos`, `economia_circular`.
   - Etapas: `idea`, `validacion`, `puesta_en_marcha`.
   - Estado de iniciativa: `activa`, `archivada`.
   - Estado de asesoría: `programada`, `realizada`, `cancelada`.
5. **Fechas explícitas.** Registrar `fecha_programada` siempre; registrar `fecha_realizacion` cuando la asesoría se realice. La fecha real puede diferir de la programada y **no se altera para ocultar una reprogramación**.
6. **Sin doble agenda.** No programar dos asesorías para el mismo asesor en la misma franja definida para el laboratorio. (Se documenta la franja; la garantía de concurrencia se estudiará después.)
7. **Historial preservado.** Archivar una iniciativa no elimina automáticamente su historial de asesorías.

## Preguntas para la persona responsable de la Unidad

1. ¿Cuál es la franja horaria "definida para el laboratorio" que se usa en la regla de no doble programación (hora de inicio, hora de fin, días)?
2. Para Q06, ¿debe usarse el sector actual de la iniciativa o el sector que tenía en el momento de cada asesoría?

## Riesgo

- **Riesgo:** que las asesorías reprogramadas pierdan trazabilidad si se sobrescribe `fecha_programada` con la nueva fecha.
- **Mitigación (regla 5):** conservar siempre la fecha original/programada y registrar la real en `fecha_realizacion`; si hay reprogramación, conservar ambas fechas o un historial de cambios en el futuro diseño.

## Reglas funcionales vs mecanismos técnicos

- Funcionales: unicidad de códigos, pertenencia de asesorías a iniciativas, dominios de estados/sectores, trazabilidad de fechas, no doble agenda, preservación del historial.
- Mecanismos técnicos (se aprenderán más adelante): validación formal de esquemas en MongoDB, índices únicos, garantías concurrentes para la regla de agenda.
- La validación formal y el manejo de solicitudes simultáneas **no** forman parte de esta semana.
