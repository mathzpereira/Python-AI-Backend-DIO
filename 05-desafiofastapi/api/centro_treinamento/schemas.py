from typing import Annotated

from pydantic import Field
from api.contrib.schemas import BaseSchema

class CentroTreinamento(BaseSchema):
    nome: Annotated[str, Field(description="Nome do centro de treinamento", examples=["CT do Atlético", "CT do Porto"], max_length=20)]
    endereco: Annotated[str, Field(description="Endereço do centro de treinamento", examples=["Rua A", "Rua B"], max_length=60)]
    proprietario: Annotated[str, Field(description="Proprietário do centro de treinamento", examples=["João", "Maria"], max_length=30)]