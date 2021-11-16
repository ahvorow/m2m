from typing import Text
from django.db import models
from m2m.features import custom_send_mail, convert_mail_text


class Mail(models.Model):
    recipient = models.CharField(max_length=100)
    text = models.TextField()

    def send(self, convert_mail_text):
        custom_send_mail(self.recipient, convert_mail_text(self.text))
