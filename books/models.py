from django.db import models

# Create your models here.

class Books(models.Model):
    title = models.CharField(max_length=350)
    author = models.CharField(max_length=350)
    publisher = models.URLField(max_length=200)
    stock = models.IntegerField()

    def __str__(self):
        return self.title

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'author': self.author,
            'publisher': self.publisher,
            'stock': self.stock,
        }
    
