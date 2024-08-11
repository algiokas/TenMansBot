import numpy

class Player:
    def __init__(self, name: str, id: int):
        self.name = name
        self.id = id

        gen = numpy.random.default_rng()
        self.rating = int((gen.normal(1, 0.2) * 500) + 500)

    def __eq__(self, other: object) -> bool:
        return self.id == other.id
    
    def __ne__(self, other: object) -> bool:
        return self.id != other.id
    

