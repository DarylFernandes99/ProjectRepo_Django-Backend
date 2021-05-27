from django.db import models
from django.conf import settings
from django.core.mail import send_mail

# Create your models here.
class Feedback(models.Model):
    email = models.EmailField(blank=True)
    subject = models.CharField(max_length=50)
    message = models.TextField()

    def __str__(self):
        return str(self.id)
    
    def save(self, *args, **kwargs):
        email_from = settings.EMAIL_HOST_USER
        if self.email:
            subject = 'Feedback Acknowledgement'
            message = f'Hello {self.email}, thank you for your valuable feedback. We will get back to you shortly if any queries mentioned.\nMessage\n{self.message}'
            recipient_list = [self.email]
            send_mail( subject, message, email_from, recipient_list )
        else:
            subject = self.subject
            message = self.message
            recipient_list = [settings.EMAIL_HOST_USER]
            send_mail( subject, message, email_from, recipient_list )
        return super().save(*args, **kwargs)