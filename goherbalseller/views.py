from django.shortcuts import render
from django.views.generic import TemplateView

class SellerRegisterView(TemplateView):
    template_name = 'goherbalseller/auth/becomeseller.html'

class SellerDashboardView(TemplateView):
    template_name = 'goherbalseller/dashboard/sellerdashboard.html'

class SellerProductListView(TemplateView):
    template_name = 'goherbalseller/products/productlist.html'

class SellerProductCreateView(TemplateView):
    template_name = 'goherbalseller/products/create.html'

class SellerProductUpdateView(TemplateView):
    template_name = 'goherbalseller/products/update.html'

class SellerProductDeleteView(TemplateView):
    template_name = 'goherbalseller/products/delete.html'

class SellerOrderListView(TemplateView):
    template_name = 'goherbalseller/orders/list.html'

class SellerOrderDetailView(TemplateView):
    template_name = 'goherbalseller/orders/detail.html'

class SellerPayoutListView(TemplateView):
    template_name = 'goherbalseller/payouts/list.html'

class SellerPayoutRequestView(TemplateView):
    template_name = 'goherbalseller/payouts/request.html'

class SellerAnalyticsView(TemplateView):
    template_name = 'goherbalseller/analytics/analytics.html'

class SellerProfileView(TemplateView):
    template_name = 'goherbalseller/profile/profile.html'

class SellerProfileEditView(TemplateView):
    template_name = 'goherbalseller/profile/edit.html'
