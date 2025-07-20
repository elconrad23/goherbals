from django.urls import path
from . import views

app_name = 'goherbalseller'

urlpatterns = [
    # Seller registration
    path('auth/becomeseller/', views.SellerRegisterView.as_view(), name='becomeseller'),
    
    # Seller dashboard URLs
    path('dashboard/', views.SellerDashboardView.as_view(), name='dashboard'),
    path('products/', views.SellerProductListView.as_view(), name='productlist'),
    path('products/add/', views.SellerProductCreateView.as_view(), name='product_create'),
    path('products/<uuid:pk>/edit/', views.SellerProductUpdateView.as_view(), name='product_update'),
    path('products/<uuid:pk>/delete/', views.SellerProductDeleteView.as_view(), name='product_delete'),
    path('orders/', views.SellerOrderListView.as_view(), name='orders'),
    path('order/<uuid:pk>/', views.SellerOrderDetailView.as_view(), name='order_detail'),
    path('payouts/', views.SellerPayoutListView.as_view(), name='payouts'),
    path('payout/request/', views.SellerPayoutRequestView.as_view(), name='payout_request'),
    path('analytics/', views.SellerAnalyticsView.as_view(), name='analytics'),
    path('profile/', views.SellerProfileView.as_view(), name='profile'),
    path('profile/edit/', views.SellerProfileEditView.as_view(), name='profile_edit'),
]