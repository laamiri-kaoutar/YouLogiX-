import uuid
from email.message import EmailMessage
import smtplib

class EmailNotification() : 
    def send_notification(self , model , ) :
        email_address="kamalyouness277@gmail.com"
        email_password="jdwhwvrmkkfcratl"
        msg = EmailMessage()
        msg['subject'] = "colis validation"
        msg['from'] =  email_address
        msg['to'] = email_address
        token = str(uuid.uuid4())
        link = f"http://localhost:8000/api/v1/users/emailverification?token={email_address}"
        msg.set_content(
            f"""
            full name  : {model.destinataire_nom } 
            link : to validate your colis  {link}
            This is your validation key confirming that your package has arrived successfully : {token}
            """
        )
        with smtplib.SMTP("smtp.gmail.com", 587) as stp:
            stp.starttls()
            stp.login(email_address, email_password)
            stp.send_message(msg)
        return "done"
