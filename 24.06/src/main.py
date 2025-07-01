from transform import transfrom
from extract import extract_mss 
from perform import load_to_ssm 
from extraction import extract
from load import load_mysql


data=extract()
data2=extract_mss()
data1,data2=transfrom(data)
load_to_ssm(data1,data2)
load_mysql(data1,data2)
