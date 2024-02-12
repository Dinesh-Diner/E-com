from django.urls import path
from . import views

urlpatterns = [
    path("",views.home,name="home"),
    path('Product',views.product,name="product"),
    path('Customer/<str:pk>/',views.customer,name="customer1"),
    path('formCreate',views.createOrder,name="FormOrder"),
    path('form_update/<str:pk>',views.Update,name='Form_update'),
    path('deleteform/<str:pk>',views.delete,name="Deleteform")
]
