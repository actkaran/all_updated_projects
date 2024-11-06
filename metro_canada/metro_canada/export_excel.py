import pandas
import pymysql
import metro_canada.db_config as db

con = pymysql.connect(user=db.db_user, host=db.db_host, password=db.db_password, database=db.db_name)

def clean_price_per_unit(unit):
    if "xa" in unit:
        return '$' + unit.split('$')[-1]
    elif unit.count('$') == 2:
        return '$' + unit.split('$')[-1]
    else:
        return unit
df = pandas.read_sql(f'SELECT * FROM {db.db_data_table};', con)
df["price_per_unit"] = df["price_per_unit"].apply(clean_price_per_unit)
df.fillna("NA", inplace=True)
df.to_excel("metro_canada_full.xlsx", engine='openpyxl', index=False)
print("file generated successfully...")
