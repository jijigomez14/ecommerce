
from django.urls import path
from .views import index, header, footer,product

from . import views
urlpatterns = [
    path('', index, name='index'),
    path('header/', header, name='header'),
    path('footer/', footer, name='footer'),
	path('product/', views.product, name='product'),
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('about/', views.about_view, name='about'),
    path('blog/', views.blog_view, name='blog'),
    path('about/', views.about_view, name='about'),
    
    # Add more URL patterns as needed
]
