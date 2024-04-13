from django.urls import path
from . import views

urlpatterns = [
    path('sell/', views.sell, name='sell'),
    path('sell/list/', views.properties_list, name='properties_list'),
    path('sell/<int:property_id>/', views.property_detail, name='property_detail'),
    path('user-properties/', views.user_properties, name='user_properties'),
    path('buy/<int:property_id>/', views.buy_property, name='buy_property'),
    path('delete/<int:property_id>/', views.delete, name='delete'),

]
