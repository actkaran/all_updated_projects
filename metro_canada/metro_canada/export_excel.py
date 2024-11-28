import pandas
import pymysql
import metro_canada.db_config as db

con = pymysql.connect(user=db.db_user, host=db.db_host, password=db.db_password, database=db.db_name)

def clean_price_per_unit(unit):
    if "xa0" in unit:
        unit.replace("xa0",' ')
    if unit.count("$") == 2:
        temp = unit.split("$")
        del temp[0]
        if "kg" in temp[0]:
            unit = temp[0].split("kg")[-1].strip() + ' $' + temp[1]
        elif "g" in temp[0]:
            unit = temp[0].split("g")[-1].strip() + ' $' + temp[1]
    return unit


#
# def remove_doller(mrp):
#     if mrp:
#         if "$" in mrp:
#             return mrp.replace('$','').strip()
#         else:
#             return mrp
#     else:
#         return "NA"
df = pandas.read_sql(f'SELECT * FROM {db.db_data_table};', con)
df["price_per_unit"] = df["price_per_unit"].apply(clean_price_per_unit)
# df["mrp"] = df["mrp"].apply(remove_doller)
df.fillna("NA", inplace=True)
df.insert(0, 'id', range(1, len(df) + 1))
df.to_excel("metro_canada_full_2024_11_27.xlsx", engine='openpyxl', index=False)
print("file generated successfully...")


"u200bu200b"