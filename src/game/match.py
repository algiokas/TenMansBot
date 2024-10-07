from datetime import datetime, timedelta
from enum import Enum

from game.player import Player


class Map(Enum):
    ANCIENT = 0
    ANUBIS = 1
    DUST2 = 2
    INFERNO = 3
    MIRAGE = 4
    NUKE = 5
    VERTIGO = 6
    MILLS = 7
    THERA = 8

class MatchStats:
    def __init__(self, 
                 kills = 0, 
                 assists = 0, 
                 deaths = 0, 
                 mvps = 0, 
                 hsp = 0, 
                 score = 0,
                 rating = 0,
                 rating_delta = 0):
        self.kills = kills
        self.assists = assists
        self.deaths = deaths
        self.mvps = mvps
        self.hsp = hsp
        self.score = score
        self.rating = rating
        self.rating_delta = rating_delta

class Match:
    def __init__(self, map: Map, dt: datetime, duration: timedelta):
        self.map = map
        self.dt = dt
        self.duration = duration
        self.team1_individual_stats = {}
        self.team2_individual_stats = {}

    def add_player_stats(self, team: int, player_id: int, m_stats: MatchStats):
        id_string = str(player_id)
        if team == 1:
            if id_string in self.team1_individual_stats:
                print (f"Stats for player {player_id} already added")
                return
            if id_string in self.team2_individual_stats:
                print(f"player {player_id} stats already on team 2")
                return
            self.team1_individual_stats[str(player_id)] = m_stats
        else:
            if id_string in self.team2_individual_stats:
                print (f"Stats for player {player_id} already added")
                return
            if id_string in self.team1_individual_stats:
                print(f"player {player_id} stats already on team 2")
                return
            self.team2_stats[str(player_id)] = m_stats

    def get_stats_for_player(self, player_id: int) -> MatchStats | None:
        id_string = str(player_id)
        if id_string in self.team1_individual_stats:
            return self.team1_individual_stats[id_string]
        if id_string in self.team2_individual_stats:
            return self.team2_individual_stats[id_string]
        print(f"Player {id_string} not found in match stats")
        return 
        
    def get_stats_for_team(self, team: int) -> MatchStats | None:
        if team == 1:
            return self.get_team_stats(self.team1_individual_stats)
        elif team == 2:
            return self.get_team_stats(self.team2_individual_stats)
        else:
            print("invalid team number")

    def get_team_stats(self, individualStats: dict) -> MatchStats:
        total_kills = 0
        total_assists = 0
        total_deaths = 0
        total_mvps = 0
        total_hsp = 0
        for key, value in individualStats:
            total_kills += value.kills
            total_assists += value.assists
            total_deaths += value.deaths
            total_mvps += value.mvps
            total_hsp += value.hsp
        return MatchStats(total_kills, total_assists, total_deaths, total_mvps, total_hsp / 5, 0)


    

    

