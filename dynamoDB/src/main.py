from json_read import read_json
from load_dynamodb import load_data_to_dynamoDB
from data_dynamodb import fetch_data_from_dynamo
from load_ssms import load_to_ssms
from data_mongodb import read_data

from unstruct_monogodb import fetch_from_mongo
from transform import transform_data
from load_ssms_unstruct import load_unstructured_to_ssms

# #read data from mongodb,
# mongo_data = read_data()

# #loading mongo_data to dynamodb
# load_data_to_dynamoDB('Projects',mongo_data)

# #fetch data from dynamodb
# fetched_data = fetch_data_from_dynamo('Projects')

# #load dynamodb data to sqlserver
# load_to_ssms(fetched_data)


#fetch unstructured data from mongo
data = fetch_from_mongo()

#load mongo data to dynamo
load_data_to_dynamoDB('Project_customer_data',data)

# fetch data from dynamo
fetched_data = fetch_data_from_dynamo('Project_customer_data')

# transform dynamo data
df_projects, df_clients, df_technologies, df_team_members, df_milestones = transform_data(fetched_data)

# load to ssms
load_unstructured_to_ssms(df_projects,'projectTable')
load_unstructured_to_ssms(df_clients,'ClientTable')
load_unstructured_to_ssms(df_technologies,'TechnologiesTable')
load_unstructured_to_ssms(df_team_members,'TeamMembersTable')
load_unstructured_to_ssms(df_milestones,'MilestonesTable')