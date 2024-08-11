from src.player import Player

class Team:
    def __init__(self, name: str, size: int):
        self.name = name
        self.size = size
        self.players = []

    def is_full(self) -> bool:
        return self.size == len(self.players)

    def open_slots(self) -> int:
        return self.size - len(self.players)
    
    def average_rating(self) -> int:
        totalRating = 0
        for p in self.players:
            totalRating += p.rating
        return totalRating // len(self.players)

    def add_player(self, p: Player) -> None:
        if p in self.players:
            print(f'Player {p.name} already on team {self.name}')
            return
        if len(self.players) >= self.size:
            print(f'Team {self.name} is full, cannot add player {p.name}')
            return
        self.players.append(p)

    def list_players(self) -> str:
        if len(self.players) < 1:
            return f'{self.name} has no players :('
        output = f'------------------\nTeam "{self.name}" Roster (Average Rating {self.average_rating()}):\n'
        index = 1
        for p in self.players:
            output += f'{index}. {p.name} - Rating {p.rating}\n'
            index += 1
        output += '------------------'
        return output
