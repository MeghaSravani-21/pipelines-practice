from fetch import fetch_emails
from upload_s3 import upload_attachments_to_s3
from upload_sqlserver import get_sql_engine
import pandas as pd
import os

bucket_name = "email-reading"

def main():
    emails = fetch_emails()
    all_records = []

    for email_obj in emails:
        sender = email_obj['sender']
        subject = email_obj['subject']
        body = email_obj['body']
        attachments = email_obj['attachments']

        print(f"\nEmail from {sender} with subject: {subject}")
        print(f"Found attachments: {attachments}")

        if attachments:
            s3_folder_url = upload_attachments_to_s3(attachments, sender, bucket_name)
        else:
            s3_folder_url = None
            print("No attachments found. Skipping S3 upload.")

        all_records.append({
            "sender": sender,
            "subject": subject,
            "body": body,
            "s3_folder_url": s3_folder_url or ""
        })

        # Clean up
        for f in attachments:
            if os.path.exists(f):
                os.remove(f)
        print("Cleaned up local attachment files.")

    if all_records:
        df = pd.DataFrame(all_records)
        engine = get_sql_engine()
        df.to_sql("Email_Communications", con=engine, if_exists="append", index=False)
        print(" Loaded data into SQL Server.")
    else:
        print(" No unseen emails to process.")

if __name__ == "__main__":
    main()