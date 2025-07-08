
from fetch import download_data
from extract import extract_text_from_pdf
from load import load
from parse import parse_details
from archive import move_to_archive

bucket_name = 'resume-bucket1-s3'
resume_keys = download_data()

load
for key in resume_keys:
    text = extract_text_from_pdf(bucket_name,key)
    details = parse_details(text)
    load(details)
    move_to_archive(bucket_name,key)