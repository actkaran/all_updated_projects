import pandas as pd
import string

letter_list = list(string.ascii_lowercase)
df = pd.Series([i for i in range(1, len(letter_list)+1)],  index=[x for x in letter_list])
print(df)
print("-------------------------------------")

# loc
print(df.loc["m"])
print(df.loc[["m", "p"]])
print("--------------------------------------")

# iloc
print(df.iloc[0])
print(df.iloc[[5, 10]])
print("--------------------------------------")

# to know which are the index of current series
print(df.index)

