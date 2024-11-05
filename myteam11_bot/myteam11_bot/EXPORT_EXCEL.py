# import pandas as pd
# import pymysql
# import datetime
#
# MATCHES = 'matches'
# CONTESTS = 'contests'
# database = 'myteam11'
#
# time_frame = ''
# description = ''
# # file_path = fr'C:\Users\DELL\Desktop\KARAN\files\ORIGINAL\sample_deliveroo_2.xlsx'
# zip_file_path = fr'''G:\My Drive\Esport\karan\Excel_files\myteam11\{time_frame}'''
# file_path = fr'''G:\My Drive\Esport\karan\Excel_files\myteam11\{time_frame}\myteam11_{description}.xlsx'''
# client = pymysql.connect(user='root', host='localhost', password='actowiz', database=database)
# cursor = client.cursor()
#
# df = pd.read_sql(f"SELECT * FROM {CONTESTS}", client)
# del df["Id"]
# a_id = range(1, len(df) + 1)
# df.insert(0, column="Id", value=a_id)
# df.fillna("NA", inplace=True)
# df.to_excel(file_path,
#             index=False,
#             engine='openpyxl'
#             )
# print("Exported: ", file_path)
