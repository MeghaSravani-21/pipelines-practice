from io import BytesIO
from office365.sharepoint.client_context import ClientContext
from office365.runtime.auth.user_credential import UserCredential
import configparser,pandas as pd
 
 
config = configparser.ConfigParser()
config.read(r'C:\Users\Sravani\Documents\mongoDB_task_2\config.ini')
username = config['SharePoint']['username']
password = config['SharePoint']['password']
site_url = config['SharePoint']['site_url']
folder_path = config['SharePoint']['folder_path']
file_name = config['SharePoint']['file_name']
 
ctx = ClientContext(site_url).with_credentials(UserCredential(username,password))
 
 
folder = ctx.web.get_folder_by_server_relative_url(folder_path)
response = BytesIO()
folder.files.get_by_url(file_name).download(response).execute_query()
 
file_content = response
 
response.seek(0)
df = pd.read_csv(file_content)
 
print(df.head(5))