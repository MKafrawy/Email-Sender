import smtplib
from email.message import EmailMessage
from credentials import *  # Assuming this contains sender_email, sender_password, smtp_server, smtp_port

def send_email(subject, message, sender_email, sender_password, recipient_email, smtp_server, smtp_port):
    try:
        # Create an EmailMessage object
        msg = EmailMessage()
        msg.set_content(message)
        msg['Subject'] = subject
        msg['From'] = sender_email
        msg['To'] = recipient_email

        # Connect to the SMTP server
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()  # Secure the connection
            server.login(sender_email, sender_password)  # Log in to the server
            server.send_message(msg)  # Send the email
        print('Email sent successfully!')

    except smtplib.SMTPException as e:
        print(f"Error: Email could not be sent. {e}")

if __name__ == '__main__':
    recipient_email = input("Please enter the recipient's email address: ")
    subject = input("Please enter the subject of the email: ")
    message = input("Please enter the message: ")
    send_email(subject, message, sender_email, sender_password, recipient_email, smtp_server, smtp_port)
