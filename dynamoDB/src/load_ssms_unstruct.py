import configparser
import urllib.parse
from sqlalchemy import create_engine
import pandas as pd
import urllib

def load_unstructured_to_ssms(data,table_name):
    config = configparser.ConfigParser()
    config.read(r'C:\Users\Sravani\Documents\mongoDB_task_2\config.ini')

    username = config['SqlDB']['username']
    password = config['SqlDB']['password']
    server = config['SqlDB']['server']
    driver = config['SqlDB']['driver']
    database = config['SqlDB']['database']

    params = urllib.parse.quote_plus(
        f'DRIVER={driver};SERVER={server};DATABASE={database};UID={username};PWD={password}'
    )

    engine = create_engine(f'mssql+pyodbc:///?odbc_connect={params}')

    data.to_sql(name=table_name,con=engine,if_exists='replace',index=False)
    