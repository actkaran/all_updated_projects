import pandas as pd
from sqlalchemy import create_engine
import verizon.DB_config as db

# Step 1: Read Excel file into pandas DataFrame
df = pd.read_excel("states_usa.xlsx")  # Replace with your actual Excel file path

# Step 2: Create a connection to the MySQL database
engine = create_engine(f'mysql+pymysql://{db.USER}:{db.PASSWORD}@{db.HOST}/{db.DATABASE}')

# Step 3: Write the DataFrame to the MySQL table
# If the table doesn't exist, pandas will create it automatically.
df.to_sql('state_usa_names', con=engine, if_exists='replace', index=False)
