import matplotlib.pyplot as plt
from main import matches,color_codes

def number_of_matches_played_per_year_by_team():
    no_of_matches = {}
    for match in matches:
        season = match['season']
        team1 = match['team1']
        team2 = match['team2']
    
       if season in no_of_matches:
            if team1 in no_of_matches[season]:
                no_of_matches[season][team1] +=1
            else:
                no_of_matches[season][team1] = 1
            
            if team2 in no_of_matches[season]:
                no_of_matches[season][team2] +=1
            else:
                no_of_matches[season][team2] = 1
        else:
            no_of_matches[season] = {team1 : 1 , team2: 1}
    

    sorted_no_of_matches = dict(sorted(no_of_matches.items(),key=lambda x : x[0]))
    
    teams = []
    for season_data in sorted_no_of_matches.values():
        for team in season_data.keys():
            if team not in teams:
                teams.append(team)
    def plot():
                
        no_of_wins = {team: [year_data.get(team, 0) for year_data in sorted_no_of_matches.values()] for team in teams}
        values = list(no_of_wins.values())
        points = [season for season in range(2008,2018)]
        
        plt.figure(figsize=(10, 5))
        bottom = [0]*len(points)
        for i in range(len(teams)):
            plt.bar(points,values[i],color = color_codes[i],label=teams[i],bottom=bottom)
            bottom = [bottom[j] + values[i][j] for j in range(len(points))]
        
        
        plt.legend()
        plt.show()
    plot()
    
number_of_matches_played_per_year_by_team()
    