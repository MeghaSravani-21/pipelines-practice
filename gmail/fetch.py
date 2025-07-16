import imaplib
import email
import os
from email.header import decode_header
from datetime import datetime, timedelta
from bs4 import BeautifulSoup

def clean_html_to_text(html):
    """Clean HTML to plain readable text."""
    soup = BeautifulSoup(html, "html.parser")

    # Remove non-visible elements
    for tag in soup(["script", "style", "noscript"]):
        tag.decompose()

    # Insert newlines for readable tags
    for tag in soup.find_all(["br", "p", "li", "div"]):
        tag.insert_after("\n")

    text = soup.get_text(separator=" ", strip=True)
    lines = [line.strip() for line in text.splitlines() if line.strip()]
    return "\n".join(lines)

def fetch_emails():
    EMAIL = "meghasravani21@gmail.com"
    APP_PASSWORD = "mmjretgtvzajemjh"  # Gmail App Password

    since_date = (datetime.now() - timedelta(days=20)).strftime("%d-%b-%Y")
    imap = imaplib.IMAP4_SSL("imap.gmail.com")
    imap.login(EMAIL, APP_PASSWORD)
    imap.select("inbox")

    status, messages = imap.search(None, f'(UNSEEN SINCE {since_date})')
    email_ids = messages[0].split()

    email_data = []

    for eid in email_ids[-10:]:  # Limit to 10 latest
        _, msg_data = imap.fetch(eid, "(RFC822)")
        msg = email.message_from_bytes(msg_data[0][1])

        subject, encoding = decode_header(msg["Subject"])[0]
        subject = subject.decode(encoding or "utf-8") if isinstance(subject, bytes) else subject
        sender = msg.get("From").split()[-1].strip("<>")

        body = None
        attachments = []

        if msg.is_multipart():
            for part in msg.walk():
                content_type = part.get_content_type()
                disposition = str(part.get("Content-Disposition"))

                if "attachment" in disposition:
                    filename = part.get_filename()
                    if filename:
                        os.makedirs("temp_attachments", exist_ok=True)
                        filepath = os.path.join("temp_attachments", filename)
                        with open(filepath, "wb") as f:
                            f.write(part.get_payload(decode=True))
                        attachments.append(filepath)

                elif content_type == "text/plain" and not body:
                    body = part.get_payload(decode=True).decode(errors="ignore").strip()
                elif content_type == "text/html" and not body:
                    html = part.get_payload(decode=True).decode(errors="ignore")
                    body = clean_html_to_text(html)
        else:
            payload = msg.get_payload(decode=True).decode(errors="ignore")
            body = clean_html_to_text(payload) if "<html" in payload.lower() else payload.strip()

        email_data.append({
            "sender": sender,
            "subject": subject,
            "body": body,
            "attachments": attachments
        })

    imap.logout()
    return email_data