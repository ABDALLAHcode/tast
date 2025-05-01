from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from taggit.managers import TaggableManager
from django.utils.translation import gettext as _
from django.utils.text import slugify
# Create your models here.

FLAG_TYPES = (
    ('new' , 'new'),
    ('feature' , 'feature'),
    ('sale' , 'sale'),
)

class Product(models.Model):
    name = models.CharField(_('Title'),max_length=120)
    image = models.ImageField(_('Image'),upload_to='products')
    price = models.FloatField(_('Price'),)
    sku = models.IntegerField(_('Sku'),)
    subtitle = models.CharField(_('Subtitle'),max_length=300)
    description = models.TextField(_('Description'),max_length=20000)
    flag = models.SlugField(_('Flag'),max_length=10,choices=FLAG_TYPES)
    brand = models.ForeignKey('Brand',verbose_name=_('Brand'),related_name='product_brand',on_delete=models.SET_NULL,null=True,blank=True)
    tags = TaggableManager()
    slug = models.SlugField(null=True,blank=True)
    
    def __str__(self):
        return self.name
    
    def save(self , *args , **kwargs):
        self.slug = slugify(self.name)
        super(Product , self).save(*args , **kwargs)
        


class ProductImages(models.Model):
    product = models.ForeignKey(Product,related_name='product_images',on_delete=models.CASCADE)
    image = models.ImageField(upload_to='productimages')
    
    def __str__(self):
        return str(self.product)



class Brand(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='brand')
    slug = models.SlugField(null=True,blank=True)
    
    def __str__(self):
        return self.name
    
    def save(self , *args , **kwargs):
        self.slug = slugify(self.name)
        super(Brand , self).save(*args , **kwargs)


class ProductReview(models.Model):
    user = models.ForeignKey(User,related_name='review_auhtor',on_delete=models.SET_NULL,null=True,blank=True)
    product = models.ForeignKey(Product,related_name='product_review',on_delete=models.CASCADE)
    rate = models.IntegerField()
    review = models.TextField(max_length=400)
    date = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return str(self.user)