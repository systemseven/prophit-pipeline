import os
import nflreadpy as nfl
from util.s3 import store
from dotenv import load_dotenv
from util.season import seasons

load_dotenv()

def teams():
    print('[Teams] - Getting Team List')
    team_df = nfl.load_teams()
    json = team_df.write_json()
    store(json, 'teams.json')
    print('[Teams] - Wrote Team List')

def trades():
    print('[Teams] - Getting Trade List')
    team_df = nfl.load_trades()
    json = team_df.write_json()
    store(json, 'trades.json')
    print('[Teams] - Wrote Trade List')

def team_stats():
    for season in seasons:
        print(f'[Teams] - Getting {season} Team Stats')
        filename = f'{season}/team_stats.json'
        stat_df = nfl.load_team_stats(season)
        json = stat_df.write_json()
        store(json, filename)
        print(f'[Teams] - Wrote {season} Team Stats')

def schedule():
    for season in seasons:
        print(f'[Teams] - Getting {season} Schedule')
        filename = f'{season}/schedule.json'
        stat_df = nfl.load_schedules(season)
        json = stat_df.write_json()
        store(json, filename)
        print(f'[Teams] - Wrote {season} Schedule')

def rosters():
    for season in seasons:
        print(f'[Teams] - Getting {season} Rosters (Weekly + Season)')
        roster_filename = f'{season}/roster.json'
        weekly_roster_filename = f'{season}/weekly_roster.json'
        roster_df = nfl.load_rosters(season)
        weekly_df = nfl.load_rosters_weekly(season)
        roster_json = roster_df.write_json()
        weekly_roster_json = weekly_df.write_json()
        store(roster_json, roster_filename)
        store(weekly_roster_json, weekly_roster_filename)
        print(f'[Teams] - Wrote {season} Rosters')

def depth_charts():
    for season in seasons:
        print(f'[Teams] - Getting {season} Depth Charts')
        filename = f'{season}/depth_charts.json'
        stat_df = nfl.load_depth_charts(season)
        json = stat_df.write_json()
        store(json, filename)
        print(f'[Teams] - Wrote {season} Depth Charts')

if __name__ == '__main__':
    teams()
    print('------')
    team_stats()
    print('------')
    schedule()
    print('------')
    rosters()
    print('------')
    depth_charts()
    print('------')
    trades()
