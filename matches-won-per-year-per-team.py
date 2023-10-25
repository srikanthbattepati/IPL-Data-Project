import matplotlib.pyplot as plt
from main import matches, color_codes

def number_of_wins_by_team_in_each_season():
    wins_in_each_season_dict = {}
    
    for match in matches:
        season = match['season']
        winner = match['winner']
        if season in wins_in_each_season_dict:
            if winner in wins_in_each_season_dict[season]:
                wins_in_each_season_dict[season][winner] += 1
            else:
                wins_in_each_season_dict[season][winner] = 1
        else:
            wins_in_each_season_dict[season] = {winner : 1}
            
    sorted_wins_in_each_season_dict = dict(sorted(wins_in_each_season_dict.items(),key=lambda x : x[0]))
    
    
    teams = []
    for wins_data in sorted_wins_in_each_season_dict.values():
        for team in wins_data.keys():
            if team not in teams:
                teams.append(team)
        
    def plot():
        wins = {team: [year_data.get(team, 0) for year_data in sorted_wins_in_each_season_dict.values()] for team in teams}
        values = list(wins.values())
        positions = [season for season in range(2008,2018)]

        plt.figure(figsize=(10, 5))
        bottom = [0]*len(positions)
        for i in range(len(teams)):
            plt.bar(positions,values[i],color = color_codes[i],label=teams[i],bottom=bottom)
            bottom = [bottom[j] + values[i][j] for j in range(len(positions))]
    
        
        plt.legend()
        plt.show()
    plot()

    number_of_wins_by_team_in_each_season()
    