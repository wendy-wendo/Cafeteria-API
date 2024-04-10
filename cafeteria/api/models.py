from django.db import models

# Create your models here.
class Item(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    price = models.IntegerField(default=0)

    def __str__(self) -> str:
        return self.name

