from django.db import models
from django.conf import settings
from django.utils  import timezone


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    title = models.CharField(max_length=240)
    text = models.TextField()
    imagen = models.ImageField(upload_to='Imagenes/',blank=True)
    created_date = models.DateTimeField(default=timezone.now)
    publish_date = models.DateTimeField(blank=True,null=True)
    url = models.URLField(blank=True, null=True)
    
    def publicar(self):
        self.publish_date = timezone.now()
        self.save()
    
    def __str__(self):
        return self.title