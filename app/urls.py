from django.urls import path

from app.views import ProductList, ProductDetail, Login

urlpatterns = [
    path('', ProductList.as_view(), name='product_list'),
    path('product-detail/<int:pk>', ProductDetail.as_view(), name='product_detail'),
    path('login', Login.as_view(), name='login')
]
