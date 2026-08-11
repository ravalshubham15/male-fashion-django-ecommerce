from .models import AddToCart

def cart_count(request):
    count = 0

    if request.user.is_authenticated:
        count = AddToCart.objects.filter(user=request.user).count()

    return {
        'cart_count': count
    }