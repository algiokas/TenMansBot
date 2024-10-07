import sqlite3
import src.db.tables

DB_SOURCE="./data/TenMans.db"

class Database:
    def __init__(this):
        print(f"Initializing database at {DB_SOURCE}")
        this.con = sqlite3.connect(DB_SOURCE)
        this.cur = this.con.cursor()

        this.cur.execute(src.db.tables.CREATE_PLAYERS_TABLE)
        this.cur.execute(src.db.tables.CREATE_MAPS_TABLE)
        this.cur.execute(src.db.tables.CREATE_MATCHES_TABLE)
        this.cur.execute(src.db.tables.CREATE_PLAYER_MATCHES_TABLE)
    
