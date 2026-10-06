# "Toronto Blue Jays" is being stored in "team".
team = "Toronto Blue Jays"
# "July 18, 2021" is being stored in "current_date".
current_date = "July 18, 2021"
# "Vladimir Guerrero Jr." is being stored in "player".
player = "Vladimir Guerrero Jr."
# 31 is being stored in home_runs_to_date".
home_runs_to_date = 31
# 88 is being stored in "games_played".
games_played = 88
# 162 is being stored in "total_season_games".
total_season_games = 162
# 73 is being stored in "home_run_record".
home_run_record = 73

# games_remaining = 162 - 88 = 74
games_remaining = total_season_games - games_played
# home_runs_per_game = 31 / 88 = 0.35
home_runs_per_game = round(home_runs_to_date / games_played, 2)
# projected_home_runs = 0.35 * 162 = 56.7
projected_home_runs = home_runs_per_game * total_season_games
# Because projected_home_runs = 56.7, and home_run_record = 73, thus projected_home_runs < home_run_record therefore can_break_record = False
can_break_record = projected_home_runs > home_run_record

print(f"{player} of the {team}")
print(f"currently has {home_runs_to_date} home runs as of {current_date}.")
print(f"The current MLB record for most home runs in a season is {home_run_record}.")
print(f"With {games_remaining} games remaining and an average of {home_runs_per_game} home runs per game,")
print(f"it is {can_break_record} that he is on pace to break the record.")
print(f"{player} is projected to hit {projected_home_runs} home runs this season.")
