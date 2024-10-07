CREATE_PLAYERS_TABLE = ('CREATE TABLE IF NOT EXISTS players ('
                        'id INTEGER PRIMARY KEY AUTOINCREMENT,'
                        'name TEXT,'
                        'matches_played INTEGER,'
                        'rating INTEGER,' 
                        'kills INTEGER,'
                        'assists INTEGER,'
                        'deaths INTEGER,'
                        'hsp REAL,'
                        'discord_id INTEGER UNIQUE,'
                        'steam_id TEXT UNIQUE,'
                        'steam_miniprofile_id INTEGER UNIQUE)')

CREATE_MAPS_TABLE = ('CREATE TABLE IF NOT EXISTS maps ('
                     'id INTEGER PRIMARY KEY AUTOINCREMENT,'
                     'name TEXT)')

CREATE_MATCHES_TABLE = ('CREATE TABLE IF NOT EXISTS matches ('
                        'id INTEGER PRIMARY KEY AUTOINCREMENT,'
                        'map_id INTEGER,'
                        'datetime TEXT,'
                        'duration INTEGER,'
                        'team1_stats TEXT,'
                        'team2_stats TEXT,'
                        'FOREIGN KEY (map_ID) REFERENCES maps (id))')

CREATE_PLAYER_MATCHES_TABLE = ('CREATE TABLE IF NOT EXISTS player_matches ('
                               'player_id INTEGER,'
                               'match_id INTEGER,'
                               'FOREIGN KEY (player_id) REFERENCES players (id),'
                               'FOREIGN KEY (match_id) REFERENCES matches (id))')