
import matplotlib.pyplot as plt
from main import matches,umpires

def foreign_umpire_analysis():
    
    foreign_umpire = set()
    country = {}
    country_data = {}
    for match in matches:
        foreign_umpire.add(match['umpire1'])
        foreign_umpire.add(match['umpire2'])
   
    for umpire in umpires:
        country[umpire['umpire']] = umpire[' country']
    
    for umpire in foreign_umpire:
        if umpire in country:
            country = country[umpire]
            if country != ' India':
                if country in country_data:
                    country_data[country] +=1
                else:
                    country_data[country] = 1

    def plot():
        countries = list(country_data.keys())
        umpires_count = list(country_data.values())
        plt.bar(countries,umpires_count)
        plt.title("Foregin umpire analysis")
        plt.xlabel("Country")
        plt.ylabel("Number of umpires")
        for index,value in enumerate(umpires_count):
            plt.text(countries[index],value,str(value))
        plt.show()

foreign_umpire_analysis()