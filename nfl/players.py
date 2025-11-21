import os
import nflreadpy as nfl
from util.s3 import store
from dotenv import load_dotenv
from util.season import seasons

load_dotenv()

def players():
    print('[Players] - Getting Player List')
    team_df = nfl.load_players()
    json = team_df.write_json()
    store(json, 'players.json')
    print('[Players] - Wrote Player List')

def contracts():
    print('[Players] - Getting Contracts')
    team_df = nfl.load_contracts()
    json = team_df.write_json()
    store(json, 'contracts.json')
    print('[Players] - Wrote Contracts')

def draft_picks():
    for season in seasons:
        print(f'[Players] - Getting {season} Draft Picks')
        filename = f'{season}/draft_picks.json'
        stat_df = nfl.load_draft_picks(season)
        json = stat_df.write_json()
        store(json, filename)
        print(f'[Players] - Wrote {season} Draft Picks')

def combine():
    for season in seasons:
        print(f'[Players] - Getting {season} Combine')
        filename = f'{season}/combine.json'
        stat_df = nfl.load_combine(season)
        json = stat_df.write_json()
        store(json, filename)
        print(f'[Players] - Wrote {season} Combine')

def injuries():
    for season in seasons:
        print(f'[Players] - Getting {season} Injuries')
        filename = f'{season}/injuries.json'
        stat_df = nfl.load_injuries(season)
        json = stat_df.write_json()
        store(json, filename)
        print(f'[Players] - Wrote {season} Injuries')

if __name__ == '__main__':
    players()
    print('------')
    draft_picks()
    print('------')
    contracts()
    print('------')
    combine()
    #injuries()