from dataclasses import dataclass

from django.conf import settings
from django.core.mail import send_mail
from django.utils.functional import cached_property

from mailing.models import EmailEntry


@dataclass
class Pigeon:
    to: str
    message: str
    subject: str


    def __call__(self) -> None:
        """Send email when initialize"""

        if self.is_sent_already:
            return

        self.__msg()
        self.__write_email_log()


    def __msg(self) -> None:
        """Sending email"""

        send_mail(
            subject= self.subject,
            message=self.message,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[self.to],
        )

    def __write_email_log(self) -> None:
        """Logging sent email"""

        EmailEntry.objects.update_or_create(
            email=self.to,
            message=self.message
        )

    @property
    def is_sent_already(self) -> bool:
        """Check if mail is already sent"""
        
        return EmailEntry.objects.filter(email=self.to, message=self.message).exists()
    
