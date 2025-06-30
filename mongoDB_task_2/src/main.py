from  extract import extract_from_mongo
from load import load_to_ssms
from insert import extract_from_text, load_to_mongoDB
from transform import transform_dynamic
import pandas as pd

records = extract_from_text(r'C:\Users\Sravani\Documents\mongoDB_task_2\src\Doc_unstructured_1.txt')
load_to_mongoDB(records)
data = extract_from_mongo()

tdata = transform_dynamic(data)
load_to_ssms(tdata)