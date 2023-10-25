import matplotlib.pyplot as plt
from main import matches

def number_of_matches_per_year():
    matches_dict = {}
    for match in matches:
        if(match['season'] in matches_dict):
            matches_dict[match['season']] += 1
        else:
            matches_dict[match['season']] = 1
            
    sorted_matches_dict = dict(sorted(matches_dict.items(),key=lambda x: x[0]))
    
    year = list(sorted_matches_dict.keys())
    number_of_matches_played = list(sorted_matches_dict.values())
    def plot():
        plt.bar(year,number_of_matches_played)
        plt.xlabel("Year")
        plt.ylabel("Number of matches")
        plt.title("Number of matches played in each year")
        for index,value in enumerate(number_of_matches_played):
            plt.text(year[index],value,str(value),ha='center',va='bottom')
        plt.show()
    plot()

number_of_matches_per_year()
