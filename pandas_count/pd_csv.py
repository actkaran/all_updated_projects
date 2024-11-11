import pandas as pd

df = pd.read_excel("swiggy.xlsx")
print("excel file loaded...")
date_greoup_data = df.groupby(["dateOfScrape"])
temp_df = []
for x, i in date_greoup_data:
    item = {}
    item["count"] = len(i)
    item["Date"] = x
    item["Total_delivery"] = len(set(i["scraped_time"]))
    temp_df.append(item)
df2 = pd.DataFrame(temp_df)
df2.to_excel("swiigy_count_datewise.xlsx", index=False, engine='openpyxl')
print("File generated")