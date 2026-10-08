// 01_explorar.js — Semana 1: exploración inicial de mongosh
// Ejecutar con la cuenta de práctica (no administrativa):
//   mongosh "mongodb://127.0.0.1:27017/emprendimiento_sena_lab" \
//     --username aprendiz_nosql \
//     --authenticationDatabase emprendimiento_sena_lab \
//     --file 01_explorar.js

db = db.getSiblingDB("emprendimiento_sena_lab");

if (db.asesorias_demo.countDocuments({ _id: "ASE-DEMO-001" }) === 0) {
  db.asesorias_demo.insertOne({
    _id: "ASE-DEMO-001",
    emprendedor_alias: "Emprendedor ficticio 01",
    iniciativa: {
      codigo: "INI-DEMO-001",
      nombre: "EcoEmpaque",
      sector: "economia_circular"
    },
    temas: ["propuesta de valor", "validacion de clientes"],
    modalidad: "virtual",
    estado: "programada",
    requiere_seguimiento: true,
    fecha_programada: new Date("2026-10-08T13:00:00Z"),
    fecha_realizacion: null
  });
}

printjson(db.asesorias_demo.findOne({ _id: "ASE-DEMO-001" }));
print("Conteo ASE-DEMO-001: " + db.asesorias_demo.countDocuments({ _id: "ASE-DEMO-001" }));

const asesoria = db.asesorias_demo.findOne({ _id: "ASE-DEMO-001" });
print("fecha_programada es Date: " + (asesoria.fecha_programada instanceof Date));

// Identificación de tipos:
print("typeof emprendedor_alias: " + typeof asesoria.emprendedor_alias); // string
print("typeof requiere_seguimiento: " + typeof asesoria.requiere_seguimiento); // boolean
print("temas es arreglo: " + Array.isArray(asesoria.temas)); // true
print("iniciativa es subdocumento: " + (typeof asesoria.iniciativa === "object" && !Array.isArray(asesoria.iniciativa))); // true

// ---- Transferencia: ASE-DEMO-002 ----
if (db.asesorias_demo.countDocuments({ _id: "ASE-DEMO-002" }) === 0) {
  db.asesorias_demo.insertOne({
    _id: "ASE-DEMO-002",
    emprendedor_alias: "Emprendedor ficticio 02",
    iniciativa: {
      codigo: "INI-DEMO-002",
      nombre: "Sabores Locales",
      sector: "alimentos"
    },
    temas: ["canales de venta", "propuesta de valor"],
    modalidad: "presencial",
    estado: "programada",
    requiere_seguimiento: true,
    fecha_programada: new Date("2026-10-09T14:00:00Z"),
    fecha_realizacion: null
  });
}

print("Conteo ASE-DEMO-002: " + db.asesorias_demo.countDocuments({ _id: "ASE-DEMO-002" }));
const asesoria2 = db.asesorias_demo.findOne({ _id: "ASE-DEMO-002" });
print("ASE-DEMO-002 fecha_programada es Date: " + (asesoria2.fecha_programada instanceof Date));
print("ASE-DEMO-002 sector: " + asesoria2.iniciativa.sector);

// Qué cambió y qué se conserva:
// Cambió: _id, nombre ("Sabores Locales"), sector ("alimentos"), temas, modalidad,
//         emprendedor_alias y fecha_programada.
// Se conservó el mismo tipo: fecha_programada sigue siendo Date, temas arreglo,
//         iniciativa subdocumento, requiere_seguimiento booleano, estado cadena.
