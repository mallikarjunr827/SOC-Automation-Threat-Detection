import smtplib
from email.message import EmailMessage

def send_alert(email_to, alerts_df):
    if alerts_df.empty:
        return  # No alerts, skip email
    
    msg = EmailMessage()
    msg['Subject'] = "Mini-SIEM Alert: Suspicious Activity Detected"
    msg['From'] = "youremail@gmail.com"           # Replace with your Gmail
    msg['To'] = email_to
    msg.set_content(f"Suspicious IPs detected:\n{alerts_df.to_string(index=False)}")
    
    # Connect and send
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login("youremail@gmail.com", "your_app_password")  # Use App Password
        smtp.send_message(msg)
    print(f"Email alert sent to {email_to}")
