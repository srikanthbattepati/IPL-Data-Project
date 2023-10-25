import matplotlib.pyplot as plt
from main import deliveries, matches

def extra_runs_conceded_by_team():
    season = []
    for match in matches:
        if match['season'] == '2016' and match['id'] not in season:
            season.append(match['id'])
      
    extras_dict = {}
    for over in deliveries:
        if over['match_id'] in season:
            bowling_team = over['bowling_team']
            extras = int(over['extra_runs'])
            if(bowling_team in extras_dict):
                extras_dict[bowling_team] += extras
            else:
                extras_dict[bowling_team] = extras
    
    teams = list(extras_dict.keys())
    extras = list(extras_dict.values())
    
    plt.bar(teams,extras)
    plt.xlabel("Team")
    plt.ylabel("Extras")
    plt.title("Extras conceded by each team ")
    for index,value in enumerate(extras):
        plt.text(teams[index],value,str(value),ha='center',va='bottom')
    plt.show()

extra_runs_conceded_by_team()
