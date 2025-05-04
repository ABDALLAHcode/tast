import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'src.settings')
import django
django.setup()
from faker import Faker
import random
from product.models import Product , Brand ,ProductImages
def seed_brand(n):
    fake = Faker()
    images = ['2.JFIF','3.JFIF','4.JFIF','5.JFIF','6.JFIF','7.JFIF','8.JFIF','9.JFIF','10.JFIF']
    for x in range(n): 
        Brand.objects.create(
            name = fake.name(),
            image = f"media/brand/{random.choice(images)}"
        )
    print(f'{n} Brand seeded')


def seed_product(n):
    fake = Faker()
    images = ['2.JFIF','3.JFIF','4.JFIF','5.JFIF','6.JFIF','7.JFIF','8.JFIF','9.JFIF','10.JFIF']
    flags = ['new','feature','sale']
    for x in range(n):
        Product.objects.create(
            name = fake.name() ,
            image = f"media/products/{random.choice(images)}" ,
            price = round(random.random()*1000,2),
            sku=  random.randint(1,100000) ,
            subtitle = fake.text(max_nb_chars=90) ,
            description = fake.text(max_nb_chars=1000) ,
            flag = random.choice(flags) ,
            brand = Brand.objects.order_by('?').first(),
        )
    print(f'{n} Products seeded')

def seed_product_images(n):
    fake = Faker()
    images = ['2.JFIF','3.JFIF','4.JFIF','5.JFIF','6.JFIF','7.JFIF','8.JFIF','9.JFIF','10.JFIF']
    for x in range(n):
        ProductImages.objects.create(
            product = Product.objects.order_by('?').first() ,
            image = f"media/productimages/{random.choice(images)}" ,
        )
    print(f'{n} Products image seeded')

seed_brand(50)
seed_product(50)
seed_product_images(200)


