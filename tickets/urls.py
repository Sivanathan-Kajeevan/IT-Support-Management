from django.urls import path
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [

    # Employee Dashboard
    path(
        '',
        views.dashboard,
        name='dashboard'
    ),

    # Register
    path(
        'register/',
        views.register_view,
        name='register'
    ),

    # Login
    path(
        'login/',
        auth_views.LoginView.as_view(
            template_name='login.html'
        ),
        name='login'
    ),

    # Logout
    path(
        'logout/',
        auth_views.LogoutView.as_view(),
        name='logout'
    ),

    # Create Ticket
    path(
        'tickets/create/',
        views.create_ticket,
        name='create_ticket'
    ),

    # Ticket Details
    path(
        'tickets/<int:ticket_id>/',
        views.ticket_detail,
        name='ticket_detail'
    ),

    # Admin Dashboard
    path(
        'staff/dashboard/',
        views.admin_dashboard,
        name='admin_dashboard'
    ),

    # Admin Update Ticket
    path(
        'staff/tickets/<int:ticket_id>/update/',
        views.update_ticket,
        name='update_ticket'
    ),

]