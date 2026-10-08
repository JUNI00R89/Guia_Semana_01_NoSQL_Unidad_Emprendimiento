"""API de la Unidad de Emprendimiento SENA (Semana 1).

Dos tablas relacionadas con SQLite:
- emprendedores (1) ──< iniciativas (N)

Ejecutar:
    uvicorn main:app --reload
Documentación interactiva: http://127.0.0.1:8000/docs
"""

from typing import List, Optional

from fastapi import Depends, FastAPI, HTTPException, status
from pydantic import BaseModel, Field
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, relationship, sessionmaker, declarative_base

# ---------------------------------------------------------------- base de datos
DATABASE_URL = "sqlite:///./emprendimiento.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)
Base = declarative_base()


class Emprendedor(Base):
    __tablename__ = "emprendedores"
    id = Column(Integer, primary_key=True, index=True)
    alias = Column(String, unique=True, index=True)
    ciudad = Column(String)
    iniciativas = relationship("Iniciativa", back_populates="emprendedor")


class Iniciativa(Base):
    __tablename__ = "iniciativas"
    id = Column(Integer, primary_key=True, index=True)
    codigo = Column(String, unique=True, index=True)
    nombre = Column(String)
    sector = Column(String)  # tecnologia | alimentos | economia_circular
    etapa = Column(String)   # idea | validacion | puesta_en_marcha
    estado = Column(String)  # activa | archivada
    emprendedor_id = Column(Integer, ForeignKey("emprendedores.id"))
    emprendedor = relationship("Emprendedor", back_populates="iniciativas")


Base.metadata.create_all(bind=engine)

# ------------------------------------------------------------------ esquemas
class EmprendedorIn(BaseModel):
    alias: str = Field(example="Emprendedor ficticio 01")
    ciudad: str = Field(example="Bogotá")


class EmprendedorOut(EmprendedorIn):
    id: int

    class Config:
        from_attributes = True


class IniciativaIn(BaseModel):
    codigo: str = Field(example="INI-001")
    nombre: str = Field(example="EcoEmpaque")
    sector: str = Field(example="economia_circular")
    etapa: str = Field(example="validacion")
    estado: str = Field(example="activa")
    emprendedor_id: int = Field(example=1)


class IniciativaOut(IniciativaIn):
    id: int

    class Config:
        from_attributes = True


# ------------------------------------------------------------------- dependencia
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


app = FastAPI(title="API Unidad de Emprendimiento SENA", version="1.0")

# ------------------------------------------------------- endpoints emprendedores
@app.post("/emprendedores", response_model=EmprendedorOut, status_code=status.HTTP_201_CREATED)
def crear_emprendedor(datos: EmprendedorIn, db: Session = Depends(get_db)):
    if db.query(Emprendedor).filter(Emprendedor.alias == datos.alias).first():
        raise HTTPException(400, "El alias ya existe")
    nuevo = Emprendedor(**datos.model_dump())
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    return nuevo


@app.get("/emprendedores", response_model=List[EmprendedorOut])
def listar_emprendedores(db: Session = Depends(get_db)):
    return db.query(Emprendedor).all()


@app.get("/emprendedores/{id}", response_model=EmprendedorOut)
def obtener_emprendedor(id: int, db: Session = Depends(get_db)):
    emp = db.get(Emprendedor, id)
    if not emp:
        raise HTTPException(404, "Emprendedor no encontrado")
    return emp


@app.put("/emprendedores/{id}", response_model=EmprendedorOut)
def actualizar_emprendedor(id: int, datos: EmprendedorIn, db: Session = Depends(get_db)):
    emp = db.get(Emprendedor, id)
    if not emp:
        raise HTTPException(404, "Emprendedor no encontrado")
    for campo, valor in datos.model_dump().items():
        setattr(emp, campo, valor)
    db.commit()
    db.refresh(emp)
    return emp


@app.delete("/emprendedores/{id}", status_code=status.HTTP_204_NO_CONTENT)
def eliminar_emprendedor(id: int, db: Session = Depends(get_db)):
    emp = db.get(Emprendedor, id)
    if not emp:
        raise HTTPException(404, "Emprendedor no encontrado")
    if emp.iniciativas:
        raise HTTPException(400, "No se puede eliminar: tiene iniciativas asociadas")
    db.delete(emp)
    db.commit()


@app.get("/emprendedores/{id}/iniciativas", response_model=List[IniciativaOut])
def iniciativas_de_emprendedor(id: int, db: Session = Depends(get_db)):
    emp = db.get(Emprendedor, id)
    if not emp:
        raise HTTPException(404, "Emprendedor no encontrado")
    return emp.iniciativas

# -------------------------------------------------------- endpoints iniciativas
@app.post("/iniciativas", response_model=IniciativaOut, status_code=status.HTTP_201_CREATED)
def crear_iniciativa(datos: IniciativaIn, db: Session = Depends(get_db)):
    if not db.get(Emprendedor, datos.emprendedor_id):
        raise HTTPException(400, "El emprendedor_id no existe")
    if db.query(Iniciativa).filter(Iniciativa.codigo == datos.codigo).first():
        raise HTTPException(400, "El código de iniciativa ya existe")
    nueva = Iniciativa(**datos.model_dump())
    db.add(nueva)
    db.commit()
    db.refresh(nueva)
    return nueva


@app.get("/iniciativas", response_model=List[IniciativaOut])
def listar_iniciativas(estado: Optional[str] = None, db: Session = Depends(get_db)):
    q = db.query(Iniciativa)
    if estado:
        q = q.filter(Iniciativa.estado == estado)
    return q.all()


@app.get("/iniciativas/{id}", response_model=IniciativaOut)
def obtener_iniciativa(id: int, db: Session = Depends(get_db)):
    ini = db.get(Iniciativa, id)
    if not ini:
        raise HTTPException(404, "Iniciativa no encontrada")
    return ini


@app.put("/iniciativas/{id}", response_model=IniciativaOut)
def actualizar_iniciativa(id: int, datos: IniciativaIn, db: Session = Depends(get_db)):
    ini = db.get(Iniciativa, id)
    if not ini:
        raise HTTPException(404, "Iniciativa no encontrada")
    if not db.get(Emprendedor, datos.emprendedor_id):
        raise HTTPException(400, "El emprendedor_id no existe")
    for campo, valor in datos.model_dump().items():
        setattr(ini, campo, valor)
    db.commit()
    db.refresh(ini)
    return ini


@app.delete("/iniciativas/{id}", status_code=status.HTTP_204_NO_CONTENT)
def eliminar_iniciativa(id: int, db: Session = Depends(get_db)):
    ini = db.get(Iniciativa, id)
    if not ini:
        raise HTTPException(404, "Iniciativa no encontrada")
    db.delete(ini)
    db.commit()
