import pandas as pd
data=pd.read_csv("Day 25/2018-Central-Park-Squirrel-Census-Squirrel-Data.csv")
gre_squi_count=len(data[data["Primary Fur Color"]=="Gray"])
cinnamon_sui_count=len(data[data["Primary Fur Color"]=="Cinnamon"])
black_squi_count=len(data[data["Primary Fur Color"]=="Black"])
print(gre_squi_count)
print(black_squi_count)
print(cinnamon_sui_count)

dataframe={
    "Fur color":["Gray","Cinnamon","Black"],
    "counts": [gre_squi_count,cinnamon_sui_count,black_squi_count]
}

df=pd.DataFrame(dataframe)
df.to_csv("squirell_count.csv")