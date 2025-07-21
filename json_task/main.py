from extract import extract_data
from transform import transform
from load import load_to_ssms
data = extract_data()
tdata = transform(data)
load_to_ssms(tdata)
