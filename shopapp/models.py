from django.db import models

# Create your models here.

class Category(models.Model):
     name = models.CharField(max_length=200, db_index=True)
     slug = models.SlugField(max_length=200, db_index=True, unique=True)

     def __str__(self):
        return self.name

class Brand(models.Model):
     name = models.CharField(max_length=200, db_index=True)

     def __str__(self):
        return self.name
