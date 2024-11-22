from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.root, name='root'),
    path('event/<slug:slug>/', views.event_details, name='event_details'),
    path('get_ticket_price/<int:ticket_type_id>/', views.get_ticket_price, name='get_ticket_price'),
    
    path('search/', views.search_results, name='search_results'),

    path('dashboard/', views.dashboard, name='dashboard'),
    path('dashboard/event/<int:event_id>/', views.event_booking_detail, name='event_booking_detail'),

    path('events/add/', views.add_event, name='add_event'),
    path('my-events/', views.list_user_events, name='list_user_events'),
    path('events/delete/<int:event_id>/', views.delete_event, name='delete_event'),
    path('event/<int:pk>/edit/', views.edit_event, name='edit_event'),

    path('logout/', views.logout_view, name='logout'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('signup/', views.signup, name='signup'),

    path('category/<slug:slug>/', views.category_events, name='category_events'),
]

