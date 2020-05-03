from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from arabicapp import views

urlpatterns=[
    # path('',views.index, name="index"),
    # path('',views.base_site, name="base_site"),
    path('home',views.home, name="home"),
    
    path('listening',views.listening, name="listening"),
    path('reading',views.reading, name="reading"),
    path('grammar',views.grammar, name="grammar"),
    path('speaking',views.speaking, name="speaking"),

    path('add/lesson/',views.add_lesson, name="add_lesson"), # create lesson
    path('add/media/',views.add_media, name="add_media"), # create lesson
    path('lesson/level/<slug:level>/',views.level_lesson, name="level_lesson"), # level lesson
    path('lesson/cards/<slug:level>/<slug:l_type>/<int:id>/',views.lesson_cards, name="lesson_cards"), 

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)