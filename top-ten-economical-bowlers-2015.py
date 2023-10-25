# import matplotlib.pyplot as plt
# from main import deliveries, matches

# def calculate_top_economical_bowlers():
#     bowler_dict = {}
#     for match in matches:
#         if match['season'] == '2015' and match['id'] not in bowler_dict:
#             bowler_dict[match['id']] = 1
    
     
    
#     for over in deliveries:
#         if over['match_id'] in bowler_dict:
#             if over['wide_runs'] == '0' and over['noball_runs'] == '0':
#                 bowler  = over['bowler'] 
#                 runs = int(over['total_runs'])
#                 if bowler in bowler_dict:
#                     bowler_dict[bowler][0] += runs
#                     bowler_dict[bowler][1] += 1
#                 else:
#                     bowler_dict[bowler] = [runs,0]
#             else:
#                 if bowler in bowler_dict:
#                     bowler_dict[bowler][0] += runs
#                 else:
#                     bowler_dict[bowler] = [runs,0]
                
   
#     for bowler in bowler_dict:
#         bowler_dict[bowler] = round((bowler_dict[bowler][0] / bowler_dict[bowler][1]) * 6,2)
    
#     top_ten_bowlers = dict(sorted(bowler_dict.items(),key=lambda x: x[1])[:10])

#     print(top_ten_bowlers)
    
#     def plot():
#         bowler = list(top_ten_bowlers.keys())
#         economy = list(top_ten_bowlers.values())
        
#         plt.bar(bowler,economy)
#         plt.xlabel("Bowler")
#         plt.ylabel("Economy")
#         plt.title("Top 10 economical bowlers of 2015")
#         plt.show()

#     plot()

# def execute():
#     calculate_top_economical_bowlers()

# execute()





import matplotlib.pyplot as plt
from main import deliveries, matches

def top_economical_bowlers():
    
    season= []
    for match in matches:
        if match['season'] == '2015' and match['id'] not in season:
            season.append(match['id'])

    bowler_runs_dict ={}
    for over in deliveries:
        if over['match_id'] in season:
            bowler = over['bowler']
            runs = int(over['total_runs'])
            if over['wide_runs'] == '0' or over['noball_runs'] == '0':
                if bowler in bowler_runs_dict:
                    bowler_runs_dict[bowler][0] += runs
                    bowler_runs_dict[bowler][1] += 1
                else:
                    bowler_runs_dict[bowler] = [runs,1]
            else:
                if bowler in bowler_runs_dict:
                    bowler_runs_dict[bowler][0] += runs
                else:
                    bowler_runs_dict[bowler] = [runs,0]

    for bowler in bowler_runs_dict:
        bowler_runs_dict[bowler] = round(bowler_runs_dict[bowler][0] / bowler_runs_dict[bowler][1]*6,2)
    top_ten_bowlers = dict(sorted(bowler_runs_dict.items(),key=lambda x: x[1])[:10])
    
    def plot():
        bowler = list(top_ten_bowlers.keys())
        economy = list(top_ten_bowlers.values())
        plt.bar(bowler,economy)
        plt.xlabel("Bowler")
        plt.ylabel("Economy")
        plt.title("Top 10 economical bowlers of 2015")
        for index,economy_value in enumerate(economy):
            plt.text(bowler[index],economy_value,str(economy_value),ha='center',va='bottom')
        plt.show()
    
    plot()

top_economical_bowlers()