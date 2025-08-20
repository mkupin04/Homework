import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("movies_dataset.csv")

grop_df = df.groupby("Year")["budget"].mean()

plt.figure(figsize=(12, 6))
plt.plot(grop_df.index, grop_df.values, color="b") 

plt.xlabel("Рік")
plt.ylabel("Бюджет в млн $")
plt.title("Середній бюджет фільмів кожного року")

plt.show()

