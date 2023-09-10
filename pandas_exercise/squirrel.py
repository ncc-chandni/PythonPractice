import pandas as pd

data = pd.read_csv("pandas_exercise/2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
gray_squirrel_count = len(data[data["Primary Fur Color"] == "Gray"])
cinnamon_squirrel_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrel_count = len(data[data["Primary Fur Color"] == "Black"])

squirrel_analysis = {
    "Fur Color": ["Gray","Cinnamon","Black"], 
    "Count" : [gray_squirrel_count, cinnamon_squirrel_count, black_squirrel_count]
}

squirrel_analysis_df = pd.DataFrame(squirrel_analysis)
squirrel_analysis_df.to_csv("/Users/umakantmanore/Desktop/amu/practice/pandas_exercise/squirrel_analysis.csv")