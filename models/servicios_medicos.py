from sqlalchemy import Column, Integer, String, Text, DateTime, func
from sqlalchemy.orm import relationship
from config.db import Base

# 🔹 Modelo para los servicios médicos del hospital
class ServiceM(Base):
    __tablename__ = "tbc_servicios_medicos"  # Nombre de la tabla en la base de datos

    # ID autoincremental del servicio médico (PK)
    id = Column(Integer, primary_key=True, autoincrement=True)

    # Nombre del servicio (único y obligatorio)
    nombre = Column(String(100), nullable=False, unique=True)

    # Descripción detallada del servicio (opcional)
    descripcion = Column(Text, nullable=True)

    # Observaciones adicionales (opcional)
    observaciones = Column(Text, nullable=True)

    # Fecha de creación del registro (automática)
    fecha_registro = Column(DateTime, nullable=False, server_default=func.now())

    # Fecha de última modificación (automática si se actualiza)
    fecha_actualizacion = Column(DateTime, nullable=True, onupdate=func.now())

    # 🔗 Relación con tabla Servicios Médicos Consumibles (1:N)
    consumibles = relationship("ServiciosMedicosConsumibles", back_populates="servicio")

    # 🔗 Relación con tabla Servicios Médicos Espacios (1:N)
    espacios = relationship("ServiciosMedicosEspacios", back_populates="servicio")  
