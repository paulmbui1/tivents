from django.urls import path
from . import views

urlpatterns = [
    path('events', views.event_list, name='event_list'),
    path('', views.root, name='root'),
    path('event_detail/<int:event_id>/', views.event_detail, name='event_detail'),

]

