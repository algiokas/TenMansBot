from game.player import Player
from game.team import Team

class TeamGenerator:
    def __init__(self, playerList: list[Player]):
        self.players = playerList
        self.matchups_generated = ()

    def generate_even_teams(self) -> tuple[Team]:
        if self.matchups_generated is None or len(self.matchups_generated) < 1:
            return self.naive_generate_even_teams()
            

    def naive_generate_even_teams(self) -> tuple[Team]:
        if len(self.players) % 2 > 0:
            print(f'Even Number of players required')
            return
        teamSize = len(self.players) // 2

        print(f'Team  Size: {teamSize}')
        
        team1 = Team('Team1', teamSize)
        team2 = Team('Team2', teamSize)

        # naive implementation
        byRating = sorted(self.players, key=lambda player: player.rating)
        for x in byRating:
            print(f'Player ID: {x.id} - Rating: {x.rating}')
        currentTeam = 1
        for i in range(teamSize):
            print(f'index {i}')
            if (currentTeam == 1):
                team1.add_player(byRating[i])
                if not team1.is_full():
                    team1.add_player(byRating[-1 - i])
                else:
                    team2.add_player(byRating[-1 - i])
                currentTeam = 2
            elif (currentTeam == 2):
                team2.add_player(byRating[i])
                if not team2.is_full():
                    team2.add_player(byRating[-1 - i])
                else:
                    team1.add_player(byRating[-1 - i])
                currentTeam = 1

        return (team1, team2)
        
    def 





