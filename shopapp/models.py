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

#def image_folder(instance, filename):
#    filename = instance.slug + '.' + os.path.splitext(filename)[1]
#    return "{0}/{1}".format[instance.slug, filename]

class Product(models.Model):
    category = models.ForeignKey(Category, models.SET_NULL, blank=True, null=True)
    brand = models.ForeignKey(Brand, models.SET_NULL, blank=True, null=True)
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, db_index=True)
    description = models.TextField(blank=True)
    image = models.ImageField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField(null=True, blank=True)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
