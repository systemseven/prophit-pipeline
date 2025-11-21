import os
from dotenv import load_dotenv

load_dotenv()

def season_list():
    start_season = int(os.getenv('START_SEASON'))
    end_season = int(os.getenv('END_SEASON'))
    return list(range(start_season, end_season + 1))

seasons = season_list()
