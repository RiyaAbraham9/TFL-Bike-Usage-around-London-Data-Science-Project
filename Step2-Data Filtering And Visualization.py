# importing neccessary packages and libraries
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

my_data = pd.read_excel('CycleData.xlsx', index_col=0)
df = pd.DataFrame(my_data)

#Collecting user input
station = input("Enter desired station: ").strip().title()
direction = input("Enter desired direction: ").strip().title()
private_only = input("Do you want to restrict to private cycles only (Y/N)?: ").strip().upper()
period_type = input("Do you want to display the date by time (T) or by date and time (D)?: ").strip().upper()
shade = input("Do you want to colour code by Weather, Direction, or Mode?: ").strip().title()

# Generates a scatterplot based on user input
def plot_scatter(station2, shade2, period_type2):
    df["Station"] = df["Station"].str.strip().str.title()
    if period_type2 == 'T':
        x = 'Time'
    else:
        x = 'Full_time'
        
    
    filtered_data = df[df['Station'] == station2]
    plt.figure(figsize=(20, 5))
    sns.scatterplot(data=filtered_data, x=x, y='Count', hue=shade2)
    plt.xticks(rotation=45)
    plt.show()

# First variant which filters to private cycles only
def plot_private_cycles(station2, shade2, period_type2):
    df["Station"] = df["Station"].str.strip().str.title()
    if period_type2 == 'T':
        x = 'Time'
    else:
        x = 'Full_time'
    
    filtered_data = df[(df['Station'] == station2) & (df['Mode'] == 'Private cycles')]
    plt.figure(figsize=(20, 5))
    sns.scatterplot(data=filtered_data, x=x, y='Count', hue=shade2)
    plt.xticks(rotation=45)
    plt.show()

# second variant which filters by station and direction
def plot_by_direction(station2, direction2, shade2, period_type2):
    df["Station"] = df["Station"].str.strip().str.title()
    if period_type2 == 'T':
        x = 'Time'
    else:
        x = 'Full_time'
    
    filtered_data = df[(df['Station'] == station2) & (df['Direction'] == direction2)]
    plt.figure(figsize=(20, 5))
    sns.scatterplot(data=filtered_data, x=x, y='Count', hue=shade2)
    plt.xticks(rotation=45)
    plt.show()

# Third variant which filters by station,direction and private cycles only
def plot_private_by_direction(station2, direction2, shade2, period_type2):
    df["Station"] = df["Station"].str.strip().str.title()
    if period_type2 == 'T':
        x = 'Time'
    else:
        x = 'Full_time'
    
    filtered_data = df[(df['Station'] == station2) & (df['Direction'] == direction2) & (df['Mode'] == 'Private cycles')]
    plt.figure(figsize=(20, 5))
    sns.scatterplot(data=filtered_data, x=x, y='Count', hue=shade2)
    plt.xticks(rotation=45)
    plt.show()

# code to call the relevant function without restriction on direction
if direction == "Any" or "ANY":
    if private_only == "Y":
        plot_private_cycles(station, shade, period_type)
    else:
        plot_scatter(station, shade, period_type)
else:
    if private_only == "Y":
        plot_private_by_direction(station, direction, shade, period_type)
        
    else:
       plot_by_direction(station, direction, shade, period_type)
       