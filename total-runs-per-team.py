# import csv
# from main import deliveries
# # import matlplotlib.pylplot as plt
# # total_runs_per_team=0
# # with open('/home/srikanth/Desktop/MB/IPL-Data-project/deliveries.csv') as csv_file:
# #     csv_reader = csv.reader(csv_file, delimiter=',')
# def calculate_total_runs_per_team():
#     total_runs_per_team={}
#     for over in deliveries:
#         batting_team = over['batting_team']
#         runs = int(over['total_runs'])
#         if(batting_team in total_runs_per_team):
#             total_runs_per_team[batting_team] += runs
#         else:
#             total_runs_per_team[batting_team] = runs
            
#     # print(total_runs_per_team)

# # print(total_runs)
# def plot():
#     x_values = list(total_runs_per_team.keys())
#     y_values = list(total_runs_per_team.values())
#     plt.bar(x_values,y_values,color = color_codes,label = x_values,width=0.5)
#     plt.xlabel("Team")
#     plt.ylabel("Runs scored by team")
#     plt.title("Runs scored by each team")
#     plt.legend()
#     plt.xticks(rotation = 90)
#     plt.show()


# def execute():
#     calculate_total_runs_per_team()
#     # plot()
# execute()



import matplotlib.pyplot as plt
from main import deliveries

def total_runs_scored_by_team():
    
    total_runs_per_team = {}
    
    for over in deliveries:
        batting_team = over['batting_team']
        runs = int(over['total_runs'])
        if batting_team in total_runs_per_team:
            total_runs_per_team[batting_team] += runs
        else:
            total_runs_per_team[batting_team] = runs
    
    def plot():
        team = list(total_runs_per_team.keys())
        runs = list(total_runs_per_team.values())
        plt.bar(team,runs,width=0.5)
        plt.xlabel("Team")
        plt.ylabel("Runs scored by team")
        plt.title("Runs scored by each team")
        plt.xticks(rotation = 90)
        for index,value in enumerate(runs):
            plt.text(team[index],value,str(value),ha='center',va='bottom')
        plt.show()
    plot()

total_runs_scored_by_team()