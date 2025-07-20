from goherbalsbuyer.models import Cart
from goherbalseller.models import SellerProfile, SellerPayout
from django.core.exceptions import ObjectDoesNotExist

def user_context(request):
    context = {
        'cart_item_count': 0,
        'profile_image': None,
        'user_type': None,
        'seller_profile': None,
        'pending_payouts': 0,
    }

    if request.user.is_authenticated:
        user = request.user
        context['user_type'] = user.user_type
        context['profile_image'] = user.profile_image.url if user.profile_image else None

        # Cart Item Count for Buyers
        if user.user_type == 'buyer':
            try:
                cart = Cart.objects.prefetch_related('items').get(buyer=user)
                context['cart_item_count'] = sum(item.quantity for item in cart.items.all())
            except Cart.DoesNotExist:
                pass

        # Seller Profile Info & Pending Payouts
        if user.user_type == 'seller':
            try:
                seller_profile = SellerProfile.objects.get(user=user)
                context['seller_profile'] = seller_profile
                context['pending_payouts'] = SellerPayout.objects.filter(seller=user, status='pending').count()
            except SellerProfile.DoesNotExist:
                pass

    return context
