from xml.dom import minidom
from xml.parsers.expat import ExpatError
import time
import sys
from datetime import datetime
import xml.etree.ElementTree as ET
import connection as database_handler


class TeamStatisticLine:
    """Klasa reprezentujaca linijke statystyczna druzyny"""
    def __init__(self, fgm, fga,fgm3,fga3,ftm,fta,tp,blk,stl,ast,min,oreb,dreb,treb,pf,tf,to,dq,sec,fgpct,fg3pct,ftpct,teamname):
        self.fgm2 = int(fgm) - int(fgm3)
        self.fga2 = int(fga) - int(fga3)
        self.fgm3 = int(fgm3)
        self.fga3 = int(fga3)
        self.ftm = int(ftm)
        self.fta = int(fta)
        self.points = int(tp)
        self.blocks = int(blk)
        self.steals = int(stl)
        self.assists = int(ast)
        self.minutes = int(min)
        self.offensive_rebounds = int(oreb)
        self.defensive_rebounds = int(dreb)
        self.fouls = int(pf)
        self.tf = int(tf)
        self.turnovers = int(to)
        self.disq = int(dq)
        self.teamname = teamname

    def __repr__(self):
        return f'\nPoints - {self.points}, Team - {self.teamname}\n'


class PlayerStatisticLine:
    """Klasa reprezentujaca linijke statystyczna zawodnika"""
    def __init__(self, name, surname, code, fgm, fga,fgm3,fga3,ftm,fta,tp,blk,stl,ast,min,oreb,dreb,treb,pf,tf,to,dq,sec,fgpct,fg3pct,ftpct,gp,gs,teamname):
        self.name = name
        self.surname = surname
        self.number = code
        self.fgm2 = int(fgm) - int(fgm3)
        self.fga2 = int(fga) - int(fga3)
        self.fgm3 = int(fgm3)
        self.fga3 = int(fga3)
        self.ftm = int(ftm)
        self.fta = int(fta)
        self.points = int(tp)
        self.blocks = int(blk)
        self.steals = int(stl)
        self.assists = int(ast)
        self.minutes = int(min)
        self.offensive_rebounds = int(oreb)
        self.defensive_rebounds = int(dreb)
        self.fouls = int(pf)
        self.tf = int(tf)
        self.turnovers = int(to)
        self.disq = int(dq)
        self.gp=gp
        self.gs=gs
        self.teamname = teamname

    def __repr__(self):
        return f'\nName - {self.name}, Surname - {self.surname}, Shirt number - {self.number}, Points - {self.points}, Team - {self.teamname}\n'


def make_player_statistic_line(player_stat, player_detail, team_detail):
    info = {}
    try:
        for key, value in player_stat.items():
            info[key]=value
        for key, value in team_detail.items():
            if(key=='name'):
                info['teamname']=value
        for key, value in player_detail.items():
            if(key=='code'):
                info[key]=value
            if(key=='name'):
                data = str(value).split(", ")
                info['name']=data[1]
                info['surname']=data[0]
            if(key=='gp'):
                info[key]=value
            if(key=='gs'):
                info[key]=value
        info['sec']=0
        player = PlayerStatisticLine(**info)
    except IndexError:
        return
    return player

def make_team_statistic_line(team_stat, team_detail):
    info = {}
    try:
        for key, value in team_stat.items():
            info[key]=value
        for key, value in team_detail.items():
            if(key=='name'):
                info['teamname']=value
        info['sec']=0
        team = TeamStatisticLine(**info)
    except IndexError:
        return
    return team


def make_log(text):
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    return f'{dt_string}\t{text}'


def get_stats_from_root(root):
    players,teams = [],[]
    for child in root:
        team_infos = child.findall("totals")
        for team_info in team_infos:
            for stat in team_info:
                if(stat.tag=='stats'):
                    team = make_team_statistic_line(stat,child)
                    teams.append(team)

        player_infos = child.findall("player")
        for player_info in player_infos:
                for stat in player_info:
                    if(stat.tag=='stats'):
                        player = make_player_statistic_line(stat,player_info,child)
                        players.append(player)
    return players,teams

def save_to_database(players,teams):
    conn = database_handler.get_connection()
    for team in teams:
        if(team is not None):
            database_handler.insert_team(team,conn)
    for player in players:
        if(player is not None):
            database_handler.insert_player(player,conn)

def update_database(players,teams):
    conn = database_handler.get_connection()
    for team in teams:
        if(team is not None):
            database_handler.update_team(team,conn)
    for player in players:
        if(player is not None):
            database_handler.update_player(player,conn)


def scan(scan_time, file_path):
    tree = ET.parse(file_path)
    players,teams = get_stats_from_root(tree.getroot())
    save_to_database(players,teams)
    print(players)
    print(teams)
    while(True):
        time.sleep(5)
        players,teams = get_stats_from_root(tree.getroot())
        update_database(players,teams)
        print(make_log("Uaktualniono"))

    


if __name__ == "__main__":
    if(len(sys.argv)!=3):
        print("Podaj okres odświeżania i lokalizację pliku XML!")
        sys.exit(1)
    try:
        scan(int(sys.argv[1]), sys.argv[2]) 
    except ValueError:
        print("Niepoprawny okres odświeżania!")
        sys.exit(1)