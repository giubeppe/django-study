from django.db import models

# Create your models here.
class NameUrl(models.Model):
    name = models.CharField(max_length=32)
    url = models.CharField(max_length=1024)
    
    def populate(self):
        NameUrl.objects.all().delete()
        url = NameUrl(name="apple", url="http://www.apple.com")
        url.save()
        url = NameUrl(name="google", url="http://www.google.com")
        url.save()
        url = NameUrl(name="microsoft", url="http://www.microsoft.com")
        url.save()
        url = NameUrl(name="microgame", url="http://www.microgame.com")
        url.save()
        url = NameUrl(name="facebook", url="http://www.facebook.com")
        url.save()
        url = NameUrl(name="twitter", url="http://www.twitter.com")
        url.save()
        url = NameUrl(name="twister", url="http://www.twister.com")
        url.save()
