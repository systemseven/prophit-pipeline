import os
import nflreadpy as nfl
from util.s3 import store
from dotenv import load_dotenv
from util.season import seasons

load_dotenv()

def fantasy_ids():
    print('[Fantasy] - Getting Fantasy Player IDs')
    team_df = nfl.load_ff_playerids()
    json = team_df.write_json()
    store(json, 'fantasy_ids.json')
    print('[Fantasy] - Wrote Fantasy Player IDs')

def rankings():
    print('[Fantasy] - Getting Fantasy Player Rankings')
    for rank_type in ['draft', 'week']:
        print(f'--- {rank_type} rankings')
        filename = f'fantasy_{rank_type}_rankings.json'
        team_df = nfl.load_ff_rankings(rank_type)
        json = team_df.write_json()
        store(json, filename)

def opps():
    print('[Fantasy] - Getting Fantasy Opportunities')
    for season in seasons:
        for stat_type in ['weekly', 'pbp_pass', 'pbp_rush']:
            print(f'--- {season} {stat_type} opps')
            filename = f'{season}/fantasy_{stat_type}_opps.json'
            team_df = nfl.load_ff_opportunity(season, stat_type)
            json = team_df.write_json()
            store(json, filename)

if __name__ == '__main__':
   fantasy_ids()
    print('------')
    rankings()
    print('------')
    opps()