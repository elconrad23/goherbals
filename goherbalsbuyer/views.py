from django.shortcuts import render
from django.views.generic import TemplateView

class HomeView(TemplateView):
    template_name = 'goherbalsbuyer/home.html'

class CategoryListView(TemplateView):
    template_name = 'goherbalsbuyer/products/categories.html'

class CategoryDetailView(TemplateView):
    template_name = 'goherbalsbuyer/products/categorydetail.html'

class ProductListView(TemplateView):
    template_name = 'goherbalsbuyer/products/products.html'

class ProductDetailView(TemplateView):
    template_name = 'goherbalsbuyer/products/productdetail.html'

class ProductReviewsView(TemplateView):
    template_name = 'goherbalsbuyer/products/reviews.html'

class ProductSearchView(TemplateView):
    template_name = 'goherbalsbuyer/products/search.html'

class RegisterView(TemplateView):
    template_name = 'goherbalsbuyer/auth/register.html'

class LoginView(TemplateView):
    template_name = 'goherbalsbuyer/auth/login.html'

class ProfileView(TemplateView):
    template_name = 'goherbalsbuyer/profile/profile.html'

class ProfileEditView(TemplateView):
    template_name = 'goherbalsbuyer/profile/edit.html'

class CartView(TemplateView):
    template_name = 'goherbalsbuyer/cart/cart.html'

class AddToCartView(TemplateView):
    template_name = 'goherbalsbuyer/cart/add.html'

class UpdateCartItemView(TemplateView):
    template_name = 'goherbalsbuyer/cart/update.html'

class RemoveFromCartView(TemplateView):
    template_name = 'goherbalsbuyer/cart/remove.html'

class CheckoutView(TemplateView):
    template_name = 'goherbalsbuyer/checkout/checkout.html'

class OrderListView(TemplateView):
    template_name = 'goherbalsbuyer/orders/list.html'

class OrderDetailView(TemplateView):
    template_name = 'goherbalsbuyer/orders/detail.html'

class OrderTrackingView(TemplateView):
    template_name = 'goherbalsbuyer/orders/tracking.html'

class AddReviewView(TemplateView):
    template_name = 'goherbalsbuyer/reviews/add.html'

class EditReviewView(TemplateView):
    template_name = 'goherbalsbuyer/reviews/edit.html'

class AjaxAddToCartView(TemplateView):
    template_name = 'goherbalsbuyer/ajax/add_to_cart.html'

class AjaxUpdateCartView(TemplateView):
    template_name = 'goherbalsbuyer/ajax/update_cart.html'

class AjaxGetCartCountView(TemplateView):
    template_name = 'goherbalsbuyer/ajax/cart_count.html'

class AjaxProductSearchView(TemplateView):
    template_name = 'goherbalsbuyer/ajax/product_search.html'