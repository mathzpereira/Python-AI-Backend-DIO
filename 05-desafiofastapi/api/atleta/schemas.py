from typing import Annotated
from pydantic import Field, PositiveFloat
from api.contrib.schemas import BaseSchema

class Atleta(BaseSchema):
    nome: Annotated[str, Field(description="Nome do atleta", examples=["João", "Maria"], max_length=50)]
    cpf: Annotated[str, Field(description="CPF do atleta", examples=["12345678900"], max_length=11)]
    idade: Annotated[int, Field(description="Idade do atleta", examples=[20, 30])]
    peso: Annotated[PositiveFloat, Field(description="Peso do atleta", examples=[70.5, 80.0])]
    altura: Annotated[PositiveFloat, Field(description="Altura do atleta", examples=[1.70, 1.80])]
    sexo: Annotated[str, Field(description="Sexo do atleta", examples=["M", "F"], max_length=1)]