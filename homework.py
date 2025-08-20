import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("movies_dataset.csv")

grop_df = df.groupby("Year")["budget"].mean()

# Побудова стовпчастої діаграми
plt.figure(figsize=(12, 6))
#plt.bar(industry_counts.index, industry_counts.values, color="gold")
plt.plot(grop_df.index, grop_df.values, color="b") 
# Оформлення графіку
plt.xlabel("Рік")
plt.ylabel("Бюджет")
plt.title("Середній бюджет фільмів кожного року")

# Показуємо графік
plt.show()