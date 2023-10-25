# import matplotlib.pyplot as plt
# from main import deliveries

# def calculate_top_ten_rcb_bastman():
#     batsman_score_dict = {}
    
  
#     for over in deliveries:
#         if over['batting_team'] == 'Royal Challengers Bangalore':
#             batsman =over['batsman']
#             runs_scored = int(over['batsman_runs_dict'])
#             if(batsman in batsman_score_dict):
#                 batsman_score_dict[batsman] += runs_scored
#             else:
#                 batsman_score_dict[batsman] = runs_scored
    
#     sorted_dict = dict(sorted(batsman_runs_dict.items(),key=lambda x: x[1],reverse=True))
    
#     batsman = list(sorted_dict.keys())[:10]
#     runs = list(sorted_dict.values())[:10]
    
#     plt.bar(batsman,runs)
#     plt.xlabel("Batsman")
#     plt.ylabel("Runs")
#     plt.title("Top 10 RCB batsman")
#     plt.show()




import matplotlib.pyplot as plt
from main import deliveries

def top_ten_rcb_bastman():
    
    batsman_runs_dict = {}
    for over in deliveries:
        batsman = over['batsman']
        runs = int(over['batsman_runs_dict'])
        if over['batting_team'] == "Royal Challengers Bangalore":
            if  batsman in batsman_runs_dict:
                batsman_runs_dict[batsman] += runs
            else:
                batsman_runs_dict[batsman] = runs
                sorted_runs_dict = dict(list(sorted(batsman_runs_dict.items(),key=lambda x:x[1],reverse=True))[:10])
    def plot():
        batsman_name = list(sorted_runs_dict.keys())
        runs_scored = list(sorted_runs_d.values())
        pltr(batsman_name,runs_scored)
        for index,value in enumerate(runs_scored):
            plt.text(batsman_name[index],value ,str(value),ha='center', va='bottom')
        plt.show()
    plot()

top_ten_rcb_bastman()