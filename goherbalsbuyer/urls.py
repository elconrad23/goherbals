from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'goherbalsbuyer'

urlpatterns = [
    # Home and category pages
    path('', views.HomeView.as_view(), name='home'),
    path('categories/', views.CategoryListView.as_view(), name='category_list'),
    path('category/<slug:slug>/', views.CategoryDetailView.as_view(), name='category_detail'),
    
    # Product pages
    path('products/', views.ProductListView.as_view(), name='products'),
    path('product/<uuid:pk>/', views.ProductDetailView.as_view(), name='product_detail'),
    path('product/<uuid:pk>/reviews/', views.ProductReviewsView.as_view(), name='product_reviews'),
    path('search/', views.ProductSearchView.as_view(), name='product_search'),
    
    # Authentication URLs
    path('auth/login/', auth_views.LoginView.as_view(template_name='goherbalsbuyer/auth/login.html'), name='login'),
    path('auth/logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('auth/register/', views.RegisterView.as_view(), name='register'),
    path('auth/profile/', views.ProfileView.as_view(), name='profile'),
    path('auth/profile/edit/', views.ProfileEditView.as_view(), name='profile_edit'),
    
    # Shopping cart URLs
    path('cart/', views.CartView.as_view(), name='cart'),
    path('cart/add/<uuid:product_id>/', views.AddToCartView.as_view(), name='add_to_cart'),
    path('cart/update/<int:item_id>/', views.UpdateCartItemView.as_view(), name='update_cart_item'),
    path('cart/remove/<int:item_id>/', views.RemoveFromCartView.as_view(), name='remove_from_cart'),
    
    # Checkout and order URLs
    path('checkout/', views.CheckoutView.as_view(), name='checkout'),
    path('orders/', views.OrderListView.as_view(), name='order_list'),
    path('order/<uuid:pk>/', views.OrderDetailView.as_view(), name='order_detail'),
    path('order/<uuid:pk>/track/', views.OrderTrackingView.as_view(), name='order_tracking'),
    
    # Review URLs
    path('product/<uuid:product_id>/review/add/', views.AddReviewView.as_view(), name='add_review'),
    path('review/<int:pk>/edit/', views.EditReviewView.as_view(), name='edit_review'),
    
    # AJAX endpoints
    path('ajax/add-to-cart/', views.AjaxAddToCartView.as_view(), name='ajax_add_to_cart'),
    path('ajax/update-cart/', views.AjaxUpdateCartView.as_view(), name='ajax_update_cart'),
    path('ajax/get-cart-count/', views.AjaxGetCartCountView.as_view(), name='ajax_cart_count'),
    path('ajax/product-search/', views.AjaxProductSearchView.as_view(), name='ajax_product_search'),
]