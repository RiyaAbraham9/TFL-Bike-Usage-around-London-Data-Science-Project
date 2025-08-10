# importing neccessary packages and libraries
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor, plot_tree

# load the CycleData excel file and set first column as the index
data = pd.read_excel("CycleData.xlsx", index_col=0)

def train_decision_tree(station):
    #Get data for the station input and only for private cycles
    df = data[(data["Station"] == station) & (data["Mode"] == "Private cycles")].copy() 
    #Convert the time variable from a string into hours
    df["RealTime"] = pd.to_datetime(df["Time"], format="%H:%M:%S").dt.hour 
    #Setting up our input, X, as the hour of the day, and output, y, as the count
    X = df[["RealTime"]]
    y = df["Count"]
    #Split the data into training sets and test sets 
    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=1)
    #Use the training data to train a decision tree to predict cycle usage patterns
    model = DecisionTreeRegressor(max_depth=3)
    model.fit(X_train, y_train)
    
    df["Predicted"] = model.predict(X)
    
    #Create a scatterplot to compare the model's predictions and the actual count
    plt.figure(figsize=(10, 5))
    sns.scatterplot(data=df, x="RealTime", y="Count", label="Actual")
    sns.scatterplot(data=df, x="RealTime", y="Predicted", label="Predicted")
    plt.xlabel("Time of Day (Hours)")
    plt.ylabel("Cycle Count")
    plt.title(f"Decision Tree Prediction for {station}")
    plt.legend()
    plt.show()
    
    #Plot the decision tree to see how predictions are made
    plt.figure(figsize=(10, 5))
    plot_tree(model, feature_names=["RealTime"], filled=True)
    plt.title(f"Decision Tree for {station}")
    plt.show()

#Ask the user which station they want to observe (the station will be converted to uppercase to ensure correct format)    
station_choice = input("Enter a station: ").strip().upper()
train_decision_tree(station_choice) 
    
