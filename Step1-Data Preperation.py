# importing neccessary packages and libraries
import csv
import pandas as pd

# List of station names to filter for group 33
StationNames = ["ML0012", "ML0036", "ML0040"]
RowCounter = 0

# Open the output CSV file in append mode
with open("project_data.csv", "a", newline="") as f:
    writer = csv.writer(f)
    
    
    for i in range(2014, 2020): #Loop through years 2014 to 2019 
        for j in range(1, 5):   # Loop through quarters 1 to 4
            dataName = str(i) + '-Q' + str(j) + '-Central.csv'  # Concatenate the strings together so that the right file can be retrieved          
    
            with open(dataName, "r", newline="") as file: # Open and read the appropriate dataset defined above
                reader = csv.reader(file)
                

                for row in reader:
                    if row[1] in StationNames: # Check if the station name matches one of the target stations
                        row[0] = str(i) + "Q" + str(j)
                        
                        # Create a new row with an index column and write it to output
                        out_row = [RowCounter] + row
                        RowCounter += 1  
                        writer.writerow(out_row)
                        
# Define column names for the DataFrame
col_names = ["Quarter", "Station", "Date", "Weather", "Time", "Day", "Drop1", "Direction", "Drop2", "Mode", "Count"]                
# Read the filtered data into a Pandas DataFrame
df = pd.read_csv('project_data.csv', names=col_names)
# Drop unnecessary columns
df2 = df.drop(['Drop1', 'Drop2'], axis=1)
# Create a new column that combines Date and Time
df2["Full_time"] = df2["Date"] + " " + df2["Time"]
# Export the processed data to an Excel file
df2.to_excel("CycleData.xlsx", sheet_name="Sheet1")