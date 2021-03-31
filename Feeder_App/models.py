from django.db import models

# Create your models here.
class image(models.Model):
    image_date      =   models.DateTimeField('image date')
    image           =   models.ImageField(upload_to='pictures')
    species         =   models.IntegerField()

class food(models.Model):
    notice_date     =   models.DateTimeField('notice date')
    check_view      =   models.BooleanField(default=False)