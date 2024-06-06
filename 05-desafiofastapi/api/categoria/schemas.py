from typing import Annotated

from pydantic import Field
from api.contrib.schemas import BaseSchema

class Categoria(BaseSchema):
    nome: Annotated[str, Field(description="Nome da categoria", examples=["Sub-20", "lProfissiona"], max_length=20)]