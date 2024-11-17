from django.urls import path
from . import views

urlpatterns = [
    path('events', views.event_list, name='event_list'),
    path('', views.root, name='root'),
    path('event_detail/<int:event_id>/', views.event_detail, name='event_detail'),
    path('get_ticket_price/<int:ticket_type_id>/', views.get_ticket_price, name='get_ticket_price'),
]

