import os
import smtplib, ssl

from dataclasses import dataclass
from typing import List
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from django.conf import settings
from django.core.mail import send_mail

from orders.models import Order
from mailing.models import EmailEntry


from dotenv import load_dotenv
load_dotenv()


@dataclass
class Pigeon:
    to: List[str]
    text: str
    subject: str
    template_name: str = None
    order_id: int = None


    def __call__(self) -> None:
        """Send email when initialize"""

        em = self._prepare_email()

        self._send(em)
        self._mark_mail_as_sent()

        return True

    def send_mail(self) -> None:
        """Sending email msg to list of users"""
        
        em = self._prepare_email()

        self._send(em)
        self._mark_mail_as_sent()

    def _send(self, em: str) -> None:
        """Login via gmain and sending email"""

        context = ssl.create_default_context()

        with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as server:
            server.login(
                os.environ.get('EMAIL_HOST_USER'), 
                os.environ.get('EMAIL_HOST_PASSWORD'),
            )
            server.sendmail(os.environ.get('EMAIL_HOST_USER'), self.to, em)

    def _prepare_email(self) -> str:
        """Create email message"""

        em = MIMEMultipart()
        em['From'] = os.environ.get('EMAIL_HOST_USER')
        em['To'] = ', '.join(self.to)
        em['Subject'] = self.subject

        if self.template_name:
            tmpl = self._read_html_file()
            em.attach(MIMEText(tmpl, 'html'))

        if self.text:
            em.attach(MIMEText(self.text, 'plain'))

        return em.as_string()

    def _read_html_file(self) -> str:
        """Return text from html"""

        try:
            with open('/Users/kkk_kkkkkkk/Documents/email_sender/email_sender/mailing/templates/h.html') as f:
                tmpl = f.read()

            return tmpl
        
        except IOError as _ex:
            print(f'Ur fucked with {_ex}')

    def _mark_mail_as_sent(self) -> None:
        """Mark as sent"""
    
        EmailEntry.objects.create(
            email=self.to,
            from_email=os.environ.get('EMAIL_HOST_USER'),
            subject= self.subject,
            text=self.text,
            template_name=self.template_name,
            is_sent=True,
            order=Order.objects.get(id=self.order_id)
        )
    

@dataclass
class PigeonAutomaticly:
    to: str
    message: str
    subject: str


    def __call__(self) -> None:
        """Sending email"""

        send_mail(
            subject= self.subject,
            message=self.message,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[self.to],
        )