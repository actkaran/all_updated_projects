import os.path

import pymysql

# configs
db_name = 'tiffany'
db_data_table = 'store_data_tiffany'
db_link_table = 'store_links_tiffany'
store_name = 'Tiffany_&_co'
PAGESAVE = 'C:\\PAGESAVE\\TIFFANY\\'
if not os.path.exists(PAGESAVE):
    os.makedirs(PAGESAVE)


db_pass = 'actowiz'
db_host = 'localhost'
db_user = 'root'


# connections.....
con = pymysql.connect(user=db_user,host=db_host, password=db_pass, database=db_name)
cur = con.cursor()