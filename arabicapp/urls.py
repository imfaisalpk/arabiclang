from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from arabicapp import views

urlpatterns=[
    path('',views.index, name="index"),
    path('login',views.login, name="login"),
    path('home',views.home, name="home"),
    
    path('listening',views.listening, name="listening"),
    path('reading',views.reading, name="reading"),
    path('grammar',views.grammar, name="grammar"),
    path('speaking',views.speaking, name="speaking"),

    path('add/lesson/',views.add_lesson, name="add_lesson"), # create lesson




    
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)