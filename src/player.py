import numpy
from src.database import Base
from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

class Player(Base):
    __tablename__ = "players"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    rating: Mapped[int]
    

    def __repr__(self) -> str:
        return super().__repr__()


    def __init__(self, name: str, id: int):
        self.name = name
        self.id = id

        gen = numpy.random.default_rng()
        self.rating = int((gen.normal(1, 0.2) * 500) + 500)

    def __eq__(self, other: object) -> bool:
        return self.id == other.id
    
    def __ne__(self, other: object) -> bool:
        return self.id != other.id
    

