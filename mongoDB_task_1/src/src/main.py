from transform import extract_from_text,load_to_mongoDB
from extract import read_data,normalize_technologies
from load import load_to_ssms
records = extract_from_text(r'C:\Users\Sravani\Documents\mongoDB_task_1\src\src\project.txt')
data = load_to_mongoDB(records)
fetched_data = read_data()
fetched_data = normalize_technologies(fetched_data)
load_to_ssms(fetched_data)