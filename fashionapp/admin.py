from django.contrib import admin
from .models import userregister, brand, category, product, AddToCart,Order,OrderItem,Wishlist,Review,Payment

admin.site.register(userregister)
admin.site.register(brand)
admin.site.register(category)
admin.site.register(product)
admin.site.register(AddToCart)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Wishlist)
admin.site.register(Review)
admin.site.register(Payment)