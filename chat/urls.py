from django.urls import path

from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('search', views.search, name='search'),
    path('<slug:category_slug>/<slug:character_slug>/', views.chat_with_character, name='chat_with_character'),
    ]
