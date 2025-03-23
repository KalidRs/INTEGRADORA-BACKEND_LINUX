from config.db import Base
from sqlalchemy import Column, String, Enum, DateTime, ForeignKey, Integer
from sqlalchemy.orm import relationship
import enum
import uuid
import datetime

# 🔹 Enumeración de tipos de espacios disponibles en el hospital
class TipoEspacioEnum(str, enum.Enum):
    Consultorio = 'Consultorio'
    Laboratorio = 'Laboratorio'
    Quirófano = 'Quirófano'
    Sala_de_Espera = 'Sala de Espera'
    Edificio = 'Edificio'
    Estacionamiento = 'Estacionamiento'
    Habitación = 'Habitación'
    Cama = 'Cama'
    Sala_Maternidad = 'Sala Maternidad'
    Cunero = 'Cunero'
    Anfiteatro = 'Anfiteatro'
    Oficina = 'Oficina'
    Sala_de_Juntas = 'Sala de Juntas'
    Auditorio = 'Auditorio'
    Cafeteria = 'Cafeteria'
    Capilla = 'Capilla'
    Farmacia = 'Farmacia'
    Ventanilla = 'Ventanilla'
    Recepción = 'Recepción'
    Piso = 'Piso'

# 🔹 Enumeración para el estatus del espacio
class EstatusEnum(str, enum.Enum):
    Activo = 'Activo'
    Inactivo = 'Inactivo'

# 🔹 Modelo que representa un espacio físico dentro del hospital
class Espacio(Base):
    __tablename__ = 'tbc_espacios'  # Nombre de la tabla en la base de datos

    # ID único del espacio (UUID como string)
    id = Column(String(36), primary_key=True, index=True, default=lambda: str(uuid.uuid4()))

    # Tipo de espacio según la enumeración definida
    tipo = Column(Enum(TipoEspacioEnum), nullable=False)

    # Nombre identificador del espacio (ej: "Consultorio 3B")
    nombre = Column(String(100), nullable=False)

    # ID del departamento al que pertenece (FK, UUID como string)
    departamento_id = Column(
        String(36),
        ForeignKey("tbc_departamentos.id", ondelete="SET NULL"),
        nullable=True,
        index=True
    )

    # Estado del espacio (Activo o Inactivo)
    estatus = Column(Enum(EstatusEnum), nullable=False, default=EstatusEnum.Activo)

    # Fecha de creación del registro
    fecha_registro = Column(DateTime, default=datetime.datetime.utcnow)

    # Fecha de última actualización del registro
    fecha_actualizacion = Column(DateTime, nullable=True, onupdate=datetime.datetime.utcnow)

    # Capacidad máxima del espacio (opcional)
    capacidad = Column(Integer, nullable=True)

    # ID del espacio superior (jerarquía)
    espacio_superior_id = Column(
        String(36),
        ForeignKey("tbc_espacios.id", ondelete="SET NULL"),
        nullable=True
    )

    # 🔗 Relación con tabla intermedia Servicios Médicos Espacios (1:N)
    servicios_medicos_espacios = relationship(
        "ServiciosMedicosEspacios",
        back_populates="espacio"
    )
