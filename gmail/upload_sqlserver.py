from sqlalchemy import create_engine
import configparser, urllib

def get_sql_engine():
    config = configparser.ConfigParser()
    config.read(r'C:\Users\Sravani\Documents\mongoDB_task_2\config.ini')

    username = config['sql']['username']
    password = config['sql']['password']
    server = config['sql']['server']
    driver = config['sql']['driver']
    database = config['sql']['database']

    params = urllib.parse.quote_plus(
        f'DRIVER={driver};SERVER={server};DATABASE={database};UID={username};PWD={password}'
    )

    return create_engine(f'mssql+pyodbc:///?odbc_connect={params}', future=True)