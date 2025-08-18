import pandas as pd

df = pd.read_csv("movies_dataset.csv")

filter_df = df[df["Year"] == 2010]

sorted_df = filter_df.sort_values("Rating")
print(sorted_df.head(10))
