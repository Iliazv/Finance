from email.policy import default
from django.db import models


class ServiceMessage(models.Model):
    FIO = models.CharField(max_length=120)
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=100)

    def __str__(self):
        return self.FIO


class VebinarMessage(models.Model):
    FIO = models.CharField(max_length=120)
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=100)

    def __str__(self):
        return self.FIO


class Ip(models.Model):
    ip = models.CharField(max_length=100)

    def __str__(self):
        return self.ip


class Case(models.Model):
    name = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    role = models.CharField(max_length=80)
    progress = models.CharField(max_length=250)
    sector = models.CharField(max_length=50)
    long = models.CharField(max_length=30, default='5 мин. чтения')
    date = models.DateField('Опубликовано:')
    #views = models.IntegerField()
    author_image = models.ImageField(upload_to='author_images/', blank=True)
    views = models.ManyToManyField(Ip, related_name='case_views', blank=True)

    def __str__(self):
        return self.name[:40]

    def total_views(self):
        return self.views.count()


class Paragraph(models.Model):
    case = models.ForeignKey(Case, on_delete=models.CASCADE, related_name='paragraphs')
    title = models.CharField(max_length=350)
    information = models.TextField(max_length=10000)
    image = models.ImageField(upload_to='paragraph_images/', blank=True)

    def __str__(self):
        return self.title[:40]


class Image(models.Model):
    paragraph = models.ForeignKey(Paragraph, on_delete=models.CASCADE, related_name='images', default='')
    image = models.ImageField(upload_to='case_images/', blank=True)
