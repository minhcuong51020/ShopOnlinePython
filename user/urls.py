from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.IndexClass.as_view(), name='index'),
    path('login/', views.LoginClass.as_view(), name='login'),
    path('register/', views.RegisterClass.as_view(), name='register'),
    path('logout/', views.LogoutClass.as_view(), name='logout'),
    path('product/<str:type>', views.ProductClass.as_view(), name='product'),
    path('add_item_to_cart/<str:type>/<int:id>', views.addItemToCart, name='add_item_to_cart'),
    path('cart/', views.CartClass.as_view(), name='cart'),
    path('delete_item_from_cart/<str:type>/<int:id>', views.deleteItemFromCart, name='delete_item_from_cart'),
    path('create_order/', views.Create_Order_class.as_view(), name='create_order'),
    path('discount/', views.DiscountClass.as_view(), name='discount'),
]