import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv("C://Users/aksl8/Downloads/matches.csv")
matches_per_season =data.groupby('Season').size().reset_index(name = 'Match_count')
print(matches_per_season)
plt.bar(matches_per_season['Season'],matches_per_season['Match_count'])
plt.xlabel('Season')
plt.ylabel('Number of Maches')
plt.title('Number of Matches in Each Season')
plt.show()

