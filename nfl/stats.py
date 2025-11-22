import os
import nflreadpy as nfl
from util.s3 import store
from dotenv import load_dotenv
from util.season import seasons

load_dotenv()

def stats():
    print('[Stats] - Getting Player Stats')
    for season in seasons:
        filename = f'{season}/player_stats.json'
        team_df = nfl.load_player_stats(season)
        json = team_df.write_json()
        store(json, filename)
    print('[Stats] - Wrote Player Stats')

def pbp():
    print('[Stats] - Getting PBP Stats')
    for season in seasons:
        filename = f'{season}/pbp.json'
        team_df = nfl.load_pbp(season)
        json = team_df.write_json()
        store(json, filename)
    print('[Stats] - Wrote PBP Stats')

def pfr():
    print('[Stats] - Getting PFR Stats')
    for season in seasons:
        for stat_type in ['pass', 'rush', 'rec', 'def']:
            filename = f'{season}/{stat_type}_pfr.json'
            print(f'--- Building {filename}')
            team_df = nfl.load_pfr_advstats(season, stat_type)
            json = team_df.write_json()
            store(json, filename)
    print('[Stats] - Wrote PFR Stats')

def nextgen():
    print('[Stats] - Getting NextGen Stats')
    for season in seasons:
        for stat_type in ['passing', 'receiving', 'rushing']:
            filename = f'{season}/{stat_type}_nextgen.json'
            print(f'--- Building {filename}')
            team_df = nfl.load_nextgen_stats(season, stat_type)
            json = team_df.write_json()
            store(json, filename)
    print('[Stats] - Wrote NextGen Stats')

def snaps():
    print('[Snaps] - Getting Player Snaps')
    for season in seasons:
        filename = f'{season}/snap_counts.json'
        team_df = nfl.load_snap_counts(season)
        json = team_df.write_json()
        store(json, filename)
    print('[Snaps] - Wrote Player Snaps')


if __name__ == '__main__':
    stats()
    print('------')
    pbp()
    print('------')
    pfr()
    print('------')
    nextgen()
    print('------')
    snaps()