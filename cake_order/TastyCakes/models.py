from django.db import models
class Birthday_cake(models.Model):
    image=models.ImageField(upload_to='birthday_cake_img/')
    name=models.CharField(max_length=100)
    price=models.DecimalField(max_digits=5, decimal_places=2)

class Anniversary_cake(models.Model):
    image=models.ImageField(upload_to='anniversary_cake_img/')
    name=models.CharField(max_length=100)
    price=models.DecimalField(max_digits=5, decimal_places=2)

class Designer_cake(models.Model):
    image=models.ImageField(upload_to='designer_cake_img/')
    name=models.CharField(max_length=100)
    price=models.DecimalField(max_digits=5, decimal_places=2)

class Normal_cake(models.Model):
    image=models.ImageField(upload_to='normal_cake_img/')
    name=models.CharField(max_length=100)
    price=models.DecimalField(max_digits=5, decimal_places=2)

class Eggless_cake(models.Model):
    image=models.ImageField(upload_to='eggless_cake_img/')
    name=models.CharField(max_length=100)
    price=models.DecimalField(max_digits=5, decimal_places=2)

class Trend_cake(models.Model):
    image=models.ImageField(upload_to='trend_cake_img/')
    name=models.CharField(max_length=100)
    price=models.DecimalField(max_digits=5, decimal_places=2)

class Photo_cake(models.Model):
    image=models.ImageField(upload_to='photo_cake_img/')
    name=models.CharField(max_length=100)
    price=models.DecimalField(max_digits=5, decimal_places=2)

class Passion_cake(models.Model):
    image=models.ImageField(upload_to='passion_cake_img/')
    name=models.CharField(max_length=100)
    price=models.DecimalField(max_digits=6, decimal_places=2)

class Cartoon_cake(models.Model):
    image=models.ImageField(upload_to='cartoon_cake_img/')
    name=models.CharField(max_length=100)
    price=models.DecimalField(max_digits=6, decimal_places=2)

class Filmy_cake(models.Model):
    image=models.ImageField(upload_to='filmy_cake_img/')
    name=models.CharField(max_length=100)
    price=models.DecimalField(max_digits=6, decimal_places=2)

class Chocolate_cake(models.Model):
    image=models.ImageField(upload_to='chocolate_cake_img/')
    name=models.CharField(max_length=100)
    price=models.DecimalField(max_digits=6, decimal_places=2)

class Venilla_cake(models.Model):
    image=models.ImageField(upload_to='venilla_cake_img/')
    name=models.CharField(max_length=100)
    price=models.DecimalField(max_digits=6, decimal_places=2)

class Black_cur_cake(models.Model):
    image=models.ImageField(upload_to='Black_cur_cake_img/')
    name=models.CharField(max_length=100)
    price=models.DecimalField(max_digits=6, decimal_places=2)

class Pine_cake(models.Model):
    image=models.ImageField(upload_to='Pine_cake_img/')
    name=models.CharField(max_length=100)
    price=models.DecimalField(max_digits=6, decimal_places=2)

class Red_cake(models.Model):
    image=models.ImageField(upload_to='Red_cake_img/')
    name=models.CharField(max_length=100)
    price=models.DecimalField(max_digits=6, decimal_places=2)

class Blue_cake(models.Model):
    image=models.ImageField(upload_to='blue_cake_img/')
    name=models.CharField(max_length=100)
    price=models.DecimalField(max_digits=6, decimal_places=2)

class Account_Details(models.Model):
    name=models.CharField(max_length=255)
    Email = models.CharField(max_length=50)
    Contact_no=models.IntegerField(12)
    Password=models.TextField()

class Order(models.Model):
    cake_name = models.CharField(max_length=255)
    cake_price = models.DecimalField(max_digits=10, decimal_places=2)
    name=models.CharField(max_length=255)
    contact = models.CharField(max_length=15)
    address = models.TextField()

    def __str__(self):
        return f"Order for {self.cake_name}"

class Brownie(models.Model):
    image=models.ImageField(upload_to='brownie_img/')
    name=models.CharField(max_length=100)
    price=models.DecimalField(max_digits=6, decimal_places=2)

class Bread(models.Model):
    image=models.ImageField(upload_to='bread_img/')
    name=models.CharField(max_length=100)
    price=models.DecimalField(max_digits=6, decimal_places=2)

class Cookie(models.Model):
    image=models.ImageField(upload_to='cookie_img/')
    name=models.CharField(max_length=100)
    price=models.DecimalField(max_digits=6, decimal_places=2)

class Cup(models.Model):
    image=models.ImageField(upload_to='cup_img/')
    name=models.CharField(max_length=100)
    price=models.DecimalField(max_digits=6, decimal_places=2)

class Donut(models.Model):
    image=models.ImageField(upload_to='donut_img/')
    name=models.CharField(max_length=100)
    price=models.DecimalField(max_digits=6, decimal_places=2)

class Pastry(models.Model):
    image=models.ImageField(upload_to='pastry_img/')
    name=models.CharField(max_length=100)
    price=models.DecimalField(max_digits=6, decimal_places=2)





    
