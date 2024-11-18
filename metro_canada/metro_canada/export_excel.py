import pandas
import pymysql
import metro_canada.db_config as db

con = pymysql.connect(user=db.db_user, host=db.db_host, password=db.db_password, database=db.db_name)

def clean_price_per_unit(unit):
    # if "xa" in unit:
    #     return '$' + unit.split('$')[-1]
    if unit.count('$') == 2:
        return '$' + unit.split('$')[-1]
    else:
        return unit


def remove_doller(mrp):
    if mrp:
        if "$" in mrp:
            return mrp.replace('$','').strip()
        else:
            return mrp
    else:
        return "NA"
df = pandas.read_sql(f'SELECT * FROM {db.db_data_table};', con)
df["price_per_unit"] = df["price_per_unit"].apply(clean_price_per_unit)
df["mrp"] = df["mrp"].apply(remove_doller)
df.fillna("NA", inplace=True)
df.insert(0, 'id', range(1, len(df) + 1))
df.to_excel("metro_canada_full_2024_11_15.xlsx", engine='openpyxl', index=False)
print("file generated successfully...")
