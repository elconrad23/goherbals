from django.contrib.auth.models import AnonymousUser
from .models import CartItem

def goherbals_context(request):
    context = {}

    # Cart item count
    if request.user.is_authenticated:
        cart_items = CartItem.objects.filter(user=request.user)
        context['cart_item_count'] = cart_items.count()
    else:
        context['cart_item_count'] = 0

    # Profile info (you can customize based on your model)
    if hasattr(request.user, 'profile'):
        profile = request.user.profile
        context['user_profile'] = {
            'name': profile.full_name,
            'avatar': profile.avatar.url if profile.avatar else None,
        }
    else:
        context['user_profile'] = None

    return context
