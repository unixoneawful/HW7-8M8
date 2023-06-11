from django.urls import path
from . import views

app_name = 'cloth'

urlpatterns = [
    path('tag/<str:tag_name>/', views.tag_view, name='tag_view'),
    path('order/create/', views.create_order_view, name='create_order'),
    path('order/success/<int:order_id>/', views.order_success_view, name='order_success'),
]
