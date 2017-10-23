from django.db import models
from django.template.defaultfilters import slugify

# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Item, self).save(*args, **kwargs)
        
    def __str__(self):
        return self.name
