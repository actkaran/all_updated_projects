import os.path

import tiffany.db_config as db
import pandas as pd


loc = "C:\\FILE\\TIFFANY\\"
if not os.path.exists(loc):
    os.makedirs(loc)

df = pd.read_sql(f"SELECT * FROM {db.db_data_table} WHERE country='United States'", db.con)
df.fillna("NA", inplace=True)
df.to_excel(f"{loc}{db.store_name}.xlsx", index=False)
print("file generated...", loc)