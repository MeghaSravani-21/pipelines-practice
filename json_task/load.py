import configparser,pandas as pd,urllib
import urllib.parse
from sqlalchemy import create_engine,text

def load_to_ssms(tables:dict):
    config = configparser.ConfigParser()
    config.read(r'C:\Users\Sravani\Documents\mongoDB_task_2\config.ini')

    driver = config['SqlDB']['driver']
    server = config['SqlDB']['server']
    username = config['SqlDB']['username']
    password = config['SqlDB']['password']
    database = config['SqlDB']['database']

    params = urllib.parse.quote_plus(
        f'''
            DRIVER={{{driver}}};
            SERVER={server};
            DATABASE={database};
            UID={username};
            PWD={password}'''
            )
    engine = create_engine(f'mssql+pyodbc:///?odbc_connect={params}')
    
    with engine.begin() as conn:
        for name,df in tables.items():
            df.to_sql(name,conn,if_exists='replace',index=False,chunksize=1000)

        

    

