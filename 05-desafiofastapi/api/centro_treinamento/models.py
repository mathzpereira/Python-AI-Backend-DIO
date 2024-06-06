from sqlalchemy import Integer, String
from sqlalchemy.orm import mapped_column, Mapped, relationship
from api.contrib.models import BaseModel

class CategoriaModel(BaseModel):
    __tablename__ = "centros_treinamento"
    
    pk_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    nome: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)
    endereco: Mapped[str] = mapped_column(String(60), nullable=False)
    proprietario: Mapped[str] = mapped_column(String(30), nullable=False)