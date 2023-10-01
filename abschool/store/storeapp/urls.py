from django.urls import path
from storeapp import views

urlpatterns = [
     path('', views.home, name='home'),
    path('login/', views.login_view, name='login'),  # Updated URL pattern for the login page
    path('register/', views.register, name='register'),
    path('new_page/', views.new_page, name='new_page'),
    path('new_page/<str:home>', views.new_page, name='new_page'),
    path('hom/',views.hom,name='hom'),
    path('view_order/',views.view_order,name='view_order'),
    path('submit_order/', views.submit_order, name='submit_order'),
    # Add more URL patterns as needed
    # Add more URL patterns as needed
]
