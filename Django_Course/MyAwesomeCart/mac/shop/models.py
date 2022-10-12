from django.db import models

# Create your models here.
class Product(models.Model):
    product_id  = models.AutoField(primary_key = True)
    product_name = models.CharField(max_length = 100)
    category = models.CharField(max_length = 80, default="")
    subcategory = models.CharField(max_length = 80, default="")
    price = models.IntegerField(default = 0 )
    desc = models.CharField(max_length = 700, default="")
    pub_date = models.DateField(auto_now_add = True)
    image = models.ImageField(upload_to='shop/images', default = "")

    def __str__(self):
        return self.product_name


class Contact(models.Model):
    contact_id  = models.AutoField(primary_key = True)
    fname = models.CharField(max_length=30)
    lname = models.CharField(max_length=30)
    email = models.CharField(max_length=40)
    phone = models.CharField(max_length=10)
    desc = models.CharField(max_length=200)

    def __str__(self):
        full_name = self.fname + " " + self.lname
        return full_name
        #"Returns the person's full name."
        #return '%s %s' % (self.first_name, self.last_name)


class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    items_json = models.CharField(max_length=3000)
    name = models.CharField(max_length=50)
    amount=models.IntegerField(default=0)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=13)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=30)
    state = models.CharField(max_length=30)
    zip_code = models.CharField(max_length=20)

class OrderUpdate(models.Model):
    update_id = models.AutoField(primary_key = True)
    order_id = models.IntegerField(default="")
    update_desc = models.CharField(max_length=300, default="")
    timeStamp = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.update_desc[:15] + "..."