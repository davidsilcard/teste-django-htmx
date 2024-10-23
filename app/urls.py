from django.urls import path
from . import views, views_htmx

urlpatterns = [
    path('list_products/', views.list_products, name='list_products'),
]

htmx_urlpatterns = [
    path('check_product/', views_htmx.check_products, name='check_products'),
    #path('save_product/', views.save_products, name='save_products'),
]

urlpatterns += htmx_urlpatterns