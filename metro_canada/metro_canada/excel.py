import pandas
import pymysql
import metro_canada.db_config as db

con = pymysql.connect(user=db.db_user, host=db.db_host, password=db.db_password, database=db.db_name)
cur = con.cursor()

df = pandas.read_sql(f"select * from {db.db_data_table}", con)
df["id"] = range(1, len(df) + 1)
df = df[['id'] + [col for col in df.columns if col != 'id']]
df.to_excel("metro_canada.xlsx", index=False, engine="openpyxl")
print("file generated successfully")