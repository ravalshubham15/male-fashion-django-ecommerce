from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

class userregister(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    name = models.CharField(max_length=40)
    contact = models.CharField(max_length=10)
    city = models.CharField(max_length=30)
    gender = models.CharField(max_length=15)

    # Profile Picture
    profile_image = models.ImageField(
        upload_to='profile/',
        default='profile/default-user.png',
        blank=True,
        null=True
    )

    register_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username
    
class brand(models.Model):
        name = models.CharField(max_length=50,unique=True)
        description = models.TextField(blank=True)
        image = models.ImageField(upload_to='brand_photo/')
        created_at = models.DateTimeField(auto_now_add=True)
        
        def __str__(self):
         return self.name
     
class category(models.Model):
    brand=models.ForeignKey(brand,on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    description=models.TextField(blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
     return self.name
 
class product(models.Model):
     name=models.CharField(max_length=150)
     brand=models.ForeignKey(brand,on_delete=models.CASCADE)
     category=models.ForeignKey(category,on_delete=models.CASCADE)
     price=models.DecimalField(max_digits=10,decimal_places=2)
     description=models.TextField()
     stock=models.PositiveIntegerField()
     image=models.ImageField(upload_to="product_img/")
     created_at=models.DateTimeField(auto_now_add=True)

     status = models.BooleanField(default=True)
     
     def __str__(self):
      return self.name
     
class AddToCart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    added_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.product.name}"
    
class Order(models.Model):

    ORDER_STATUS = (
        ("Pending", "Pending"),
        ("Confirmed", "Confirmed"),
        ("Shipped", "Shipped"),
        ("Delivered", "Delivered"),
        ("Cancelled", "Cancelled"),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    order_date = models.DateTimeField(default=timezone.now)

    status = models.CharField(
        max_length=20,
        choices=ORDER_STATUS,
        default="Pending"
    )

    def __str__(self):
        return f"Order {self.id} - {self.user.username}"

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.product.name} ({self.quantity})"
    
class Wishlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(product, on_delete=models.CASCADE)
    added_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.product.name}"
    
class Review(models.Model):
    product = models.ForeignKey(product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    rating = models.IntegerField(default=5)

    review = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.product.name}"
    
class Payment(models.Model):

    PAYMENT_STATUS = (
        ('Pending', 'Pending'),
        ('Success', 'Success'),
        ('Failed', 'Failed'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)

    payment_id = models.CharField(max_length=100, blank=True, null=True)

    amount = models.DecimalField(max_digits=10, decimal_places=2)

    payment_method = models.CharField(max_length=50)

    status = models.CharField(
        max_length=20,
        choices=PAYMENT_STATUS,
        default='Pending'
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.status}"
