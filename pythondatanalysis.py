import pandas as pd
data = pd.read_csv("C://Users/aksl8/Downloads/matches.csv")
#print(data)
#print(data.head(100))
#print(data.tail())
#print(data.tail(19))
#print(data[100:200])
#print(data[:200])
#print(data[200:])
#print(data.columns)
#print(data[data['Season']==2008])
#print(data[data['Winner']=='Kolkata Knight Riders'])
#print(data[data['City']=='Bangalore'])
print(data[data['Player_of_Match']=='MS Dhoni'])