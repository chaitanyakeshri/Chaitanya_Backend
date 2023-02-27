from django.db import models
import static

# Create your models here.


class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)

    def _str_(self):
        return self.name


class Event(models.Model):
    Event_title = models.CharField(max_length=200, primary_key=True)
    Event_time = models.DateTimeField(auto_now_add=True)
    Event_venue = models.CharField(max_length=100)
    Conducting_Body = models.CharField(max_length=200)
    Description = models.TextField()
    img = models.ImageField(upload_to='static/', height_field=None,
                            width_field=None, max_length=1000, default='static/default.jpg')
    fav = models.BooleanField()

    def __str__(self) -> str:
        return self.Event_title
