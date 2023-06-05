from django.urls import path, re_path, include
import django.contrib.auth.urls

from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('addpage/', addpage, name='add_page'),
    path('feedback/', feedback, name='feedback'),
    path('user/', include('django.contrib.auth.urls'), name='login'),
    path('register/', Register_user.as_view(), name='register'),
    path('post/<int:post_id>/', show_post, name='post'),
    path('addtocard/<int:post_id>', add_to_card, name='add_to_card'),
    path('delfromcard/<int:post_id>', del_from_card, name='del_from_card'),
    path('card', card, name='card'),
    path('user_page/', user_page, name='user_page'),
]
