from django.db import models

# Create your models here.
class Email(models.Model):
    recipient = models.EmailField()
    originator = models.EmailField()
    subject = models.CharField(max_length=256)
    text = models.TextField()
    sent_on = models.DateField(null=True, blank=True)