from django.contrib.auth.views import LoginView
from django.views.generic import ListView, DetailView
from app.models import Product


class ProductList(ListView):
    queryset = Product.objects.all()
    template_name = 'apps/product/product_list.html'
    context_object_name = 'products'


class ProductDetail(DetailView):
    queryset = Product.objects.all()
    template_name = 'apps/product/product_detail.html'
    context_object_name = 'product'


class Login(LoginView):
    template_name = 'apps/auth/login.html'
