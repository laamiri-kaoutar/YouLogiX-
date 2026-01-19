from app.core.config import settings

import uuid
from email.message import EmailMessage
import smtplib
import os
from app.models.colis_models import Colis


class EmailNotification() :
    def __init__(self):
        
        self.email_address = settings.email_address
        self.email_password = settings.email_password
    def send_notification(self , colis ) :
        msg = EmailMessage()
        msg['subject'] = "colis validation"
        msg['from'] =  self.email_address
        msg['to'] = colis.destinataire_email
        token = str(uuid.uuid4())
        link = f"http://localhost:8000/api/v1/users/emailverification?"
        msg.set_content(
            f"""
            full name  : {colis.destinataire_nom } 
            link : to validate your colis  {link}
            This is your validation key confirming that your package has arrived successfully : {token}
            """
        )
        with smtplib.SMTP("smtp.gmail.com", 587) as stp:
            stp.starttls()
            stp.login(self.email_address, self.email_password)
            stp.send_message(msg)
        return "sent successfuly"
    def status_colis(self , colis : Colis) :
        msg = EmailMessage()
        msg['subject'] = "Colis News"
        msg['from'] =  self.email_address
        msg['to'] = colis.destinataire_email
        msg.set_content(
            f"""
            Hi Mester  {colis.destinataire_nom }  we just wannt to let you know that ur colis status {colis.statut}
            """
        )
        with smtplib.SMTP("smtp.gmail.com", 587) as stp:
            stp.starttls()
            stp.login(self.email_address, self.email_password)
            stp.send_message(msg)
    def assign_livreur(self , colis) :
        msg = EmailMessage()
        msg['subject'] = "livreur assigned to ur colis"
        msg['from'] =  self.email_address
        msg['to'] = colis.destinataire_email
        msg.set_content(
            f"""
           Hi Mr. {colis.user.name},
Your package ({colis.description}) has been assigned to the delivery person {colis.livreur}.
            """
        )
        with smtplib.SMTP("smtp.gmail.com", 587) as stp:
            stp.starttls()
            stp.login(self.email_address, self.email_password)
            stp.send_message(msg)
        
        
