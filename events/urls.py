from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('events', views.event_list, name='event_list'),
    path('', views.root, name='root'),
    path('event_detail/<int:event_id>/', views.event_detail, name='event_detail'),
    path('get_ticket_price/<int:ticket_type_id>/', views.get_ticket_price, name='get_ticket_price'),
    
    path('search/', views.search_results, name='search_results'),

    path('events/add/', views.add_event, name='add_event'),
    path('events/my-events/', views.list_user_events, name='list_user_events'),
    path('events/delete/<int:event_id>/', views.delete_event, name='delete_event'),
    path('event/<int:pk>/edit/', views.edit_event, name='edit_event'),

    path('logout/', views.logout_view, name='logout'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('signup/', views.signup, name='signup'),

]

