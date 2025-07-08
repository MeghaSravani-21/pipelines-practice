import configparser
import urllib.parse
from sqlalchemy import create_engine, text
 
def load(data):
    config = configparser.ConfigParser()
    config.read(r'C:\Users\Sravani\Documents\mongoDB_task_2\config.ini')
    
    username = config['SqlDB']['username']
    password = config['SqlDB']['password']
    server   = config['SqlDB']['server']
    database = config['SqlDB']['database']
    driver   = config['SqlDB']['driver']
    
    params = urllib.parse.quote_plus(
        f"DRIVER={{{driver}}};SERVER={server};DATABASE={database};UID={username};PWD={password}"
    )
    
    engine = create_engine(f"mssql+pyodbc:///?odbc_connect={params}", fast_executemany=True)
    
    
    query = """
    INSERT INTO Resumes (full_name, email, phone, skills, projects)
    VALUES (:full_name, :email, :phone, :skills, :projects)
    """
    with engine.begin() as conn:
        conn.execute(text(query), {
            "full_name": data.get("name"),
            "email": data.get("email"),
            "phone": data.get("phone"),
            "skills": data.get("skills"),
            "projects": data.get("projects")
        })
    