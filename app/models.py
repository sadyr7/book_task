from django.db import models



class Book(models.Model):
    title = models.CharField(max_length=30)
    author = models.CharField(max_length=100)
    year_publishing = models.DateField(auto_now=False)
    isbn = models.PositiveIntegerField()

    def __str__(self):
        return self.title
