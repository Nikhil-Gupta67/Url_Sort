from django.db import models
from hashlib import md5

class Url(models.Model):
    full_url = models.CharField(unique=True, max_length=200)
    short_url = models.CharField(unique=True, max_length=10)

    def __str__(self):
        return self.full_url
    
    @classmethod
    def create(cls, full_url):
        if not full_url:
            return None
        temp_url = md5(full_url.encode()).hexdigest()[:5]
        try:
            obj = cls.objects.create(full_url=full_url, short_url=temp_url)
        except cls.DoesNotExist:
            obj = cls.objects.get(full_url=full_url)
        except Exception:
            obj = cls.objects.get(full_url=full_url)
        return obj  