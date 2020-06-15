import sqlite3
from sqlite3 import Error

def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        c = conn.cursor()
        c.execute('pragma encoding')
    except Error as e:
        print(e)

    return conn

def insert_team(team, conn):
    sql = f'INSERT INTO team(fgm2, fga2,fgm3,fga3,ftm,fta,points,blocks,steals,assists,minutes,\
                            offensive_rebounds, defensive_rebounds,fouls,tf,turnovers,disq,teamname)\
                            VALUES(\'{str(team.fgm2)}\', \'{str(team.fga2)}\',\'{str(team.fgm3)}\',\'{str(team.fga3)}\',\
                            \'{str(team.ftm)}\',\'{str(team.fta)}\',\'{str(team.points)}\',\'{str(team.blocks)}\',\'{str(team.steals)}\',\
                            \'{str(team.assists)}\',\'{str(team.minutes)}\',\'{str(team.offensive_rebounds)}\',\'{str(team.defensive_rebounds)}\',\
                            \'{str(team.fouls)}\', \'{str(team.tf)}\',\'{str(team.turnovers)}\',\'{str(team.disq)}\',\'{str(team.teamname)}\')'
    cur = conn.cursor()
    cur.execute(sql)
    conn.commit()
    return cur.lastrowid

def update_team(team, conn):
    sql = f'UPDATE team SET\
                            fgm2 = \'{str(team.fgm2)}\',\
                            fga2 = \'{str(team.fga2)}\',\
                            fgm3 = \'{str(team.fgm3)}\',\
                            fga3 = \'{str(team.fga3)}\',\
                            ftm = \'{str(team.ftm)}\',\
                            fta = \'{str(team.fta)}\',\
                            points = \'{str(team.points)}\',\
                            blocks = \'{str(team.blocks)}\',\
                            steals = \'{str(team.steals)}\',\
                            assists = \'{str(team.assists)}\',\
                            offensive_rebounds = \'{str(team.offensive_rebounds)}\',\
                            minutes = \'{str(team.minutes)}\',\
                            defensive_rebounds = \'{str(team.defensive_rebounds)}\',\
                            fouls = \'{str(team.fouls)}\',\
                            tf = \'{str(team.tf)}\',\
                            turnovers = \'{str(team.turnovers)}\',\
                            disq = \'{str(team.disq)}\',\
                            teamname = \'{str(team.teamname)}\'\
                            WHERE teamname = \'{str(team.teamname)}\''
    cur = conn.cursor()
    cur.execute(sql)
    conn.commit()
    return cur.lastrowid

def update_player(player, conn):
    sql = f'UPDATE player SET\
                            fgm2 = \'{str(player.fgm2)}\',\
                            fga2 = \'{str(player.fga2)}\',\
                            fgm3 = \'{str(player.fgm3)}\',\
                            fga3 = \'{str(player.fga3)}\',\
                            ftm = \'{str(player.ftm)}\',\
                            fta = \'{str(player.fta)}\',\
                            points = \'{str(player.points)}\',\
                            blocks = \'{str(player.blocks)}\',\
                            steals = \'{str(player.steals)}\',\
                            assists = \'{str(player.assists)}\',\
                            offensive_rebounds = \'{str(player.offensive_rebounds)}\',\
                            minutes = \'{str(player.minutes)}\',\
                            defensive_rebounds = \'{str(player.defensive_rebounds)}\',\
                            fouls = \'{str(player.fouls)}\',\
                            tf = \'{str(player.tf)}\',\
                            turnovers = \'{str(player.turnovers)}\',\
                            gp = \'{str(player.gp)}\',\
                            gs = \'{str(player.gs)}\',\
                            disq = \'{str(player.disq)}\',\
                            teamname = \'{str(player.teamname)}\'\
                            WHERE teamname = \'{str(player.teamname)}\' and number = \'{str(player.number)}\''
    cur = conn.cursor()
    cur.execute(sql)
    conn.commit()
    return cur.lastrowid


def insert_player(player, conn):
    sql = f'INSERT INTO player(name,surname,number,fgm2, fga2,fgm3,fga3,ftm,fta,points,blocks,steals,assists,minutes,\
                            offensive_rebounds, defensive_rebounds,fouls,tf,turnovers,disq,gp,gs,teamname)\
                            VALUES(\'{str(player.name)}\',\'{str(player.surname)}\',\'{str(player.number)}\',\
                            \'{str(player.fgm2)}\', \'{str(player.fga2)}\',\'{str(player.fgm3)}\',\'{str(player.fga3)}\',\
                            \'{str(player.ftm)}\',\'{str(player.fta)}\',\'{str(player.points)}\',\'{str(player.blocks)}\',\'{str(player.steals)}\',\
                            \'{str(player.assists)}\',\'{str(player.minutes)}\',\'{str(player.offensive_rebounds)}\',\'{str(player.defensive_rebounds)}\',\'{str(player.fouls)}\',\
                            \'{str(player.tf)}\',\'{str(player.turnovers)}\',\'{str(player.disq)}\',\'{str(player.gp)}\',\'{str(player.gs)}\',\'{str(player.teamname)}\')'
    cur = conn.cursor()
    cur.execute(sql)
    conn.commit()
    return cur.lastrowid

def create_table(conn):

    create_table_sql = """ CREATE TABLE IF NOT EXISTS team (
                                        fgm2 integer,
                                        fga2 integer,
                                        fgm3 integer,
                                        fga3 integer,
                                        ftm integer,
                                        fta integer,
                                        points integer,
                                        blocks integer,
                                        steals integer,
                                        assists integer,
                                        minutes integer,
                                        offensive_rebounds integer,
                                        defensive_rebounds integer,
                                        fouls integer,
                                        tf integer,
                                        turnovers integer,
                                        disq integer,
                                        teamname TEXT NOT NULL
                                    ); """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)

    create_table_sql = """ CREATE TABLE IF NOT EXISTS player (
                                        name TEXT NOT NULL,
                                        surname TEXT NOT NULL,
                                        number integer,
                                        fgm2 integer,
                                        fga2 integer,
                                        fgm3 integer,
                                        fga3 integer,
                                        ftm integer,
                                        fta integer,
                                        points integer,
                                        blocks integer,
                                        steals integer,
                                        assists integer,
                                        minutes integer,
                                        offensive_rebounds integer,
                                        defensive_rebounds integer,
                                        fouls integer,
                                        tf integer,
                                        turnovers integer,
                                        disq integer,
                                        gp integer,
                                        gs integer,
                                        teamname TEXT NOT NULL
                                    ); """

    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)   

def get_connection():
    database = r"C:\Users\Radek\Desktop\match_stats.db"

    # create a database connection
    conn = create_connection(database)

    if conn is not None:
        create_table(conn)
        return conn
