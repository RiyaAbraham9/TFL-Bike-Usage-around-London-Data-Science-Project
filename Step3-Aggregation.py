#The relevant libaries are imported
import matplotlib.pyplot as plt
import pandas as pd 
import seaborn as sns

#The program is reading the data from the relevant libaries listed above
my_data = pd.read_excel("CycleData.xlsx", index_col=0)
df = pd.DataFrame(my_data)

#The user will input station and direction, ML0040 and Northbound
station = input("Enter desired station: ").strip().title()
direction = input("Enter desired direction: ").strip().title()

#This function takes into account the two parameters above
def averageNumberOfCycles(stationChoice, directionChoice):

    #The data is then filtered, grouped and the average number of cycles by time is calculated 
    df_filtered = df[(df["Station"].str.title() == stationChoice) & (df["Direction"].str.title() == directionChoice)]
    df_grouped = df_filtered.groupby(['Date', 'Time'])['Count'].sum().reset_index()
    df_avg = df_grouped.groupby('Time')['Count'].mean().reset_index()

    #The data is plotted    
    sns.set_style("whitegrid")
    plt.figure(figsize=(20, 5))
    sns.scatterplot(data=df_avg, x='Time', y='Count')
    plt.xticks(rotation=45)

    plt.show()

#The function is called 
averageNumberOfCycles(station, direction)
