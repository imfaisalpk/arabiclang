from django.shortcuts import render
from django.http import HttpResponse
from arabicapp.models import Lesson, LessonCard


def index(request):
    return HttpResponse('Arabic Language Web Application!!')

def base_site(request):
    return render(request,'base_site.html')

def home(request):
    return render(request,'home.html')

def listening(request):
    return render(request,'listening.html')
def reading(request):
    return render(request,'home.html')
def grammar(request):
    return render(request,'home.html')
def speaking(request):
    return render(request,'home.html')

#Create Lesson

def create_lesson(request):
    return render(request,'create_lesson.html')

def add_lesson(request):
    return render(request,'add_lesson.html')

def level_lesson(request,level):
    lessons = Lesson.objects.filter(lesson_level=level.upper())
    context= {
        'lessons':lessons,
        'level': level.capitalize()
    }
    return render(request,'level_lessons.html',context)

def lesson_cards(request, id,level,l_type):
    cards = LessonCard.objects.filter(id=id)
    print("cards: ",cards)
    lessons = Lesson.objects.filter(lesson_level=level.upper())
    context= {
        'cards':cards,
        'lessons':lessons,
        'id': id,
        'level':level,
        'type' :l_type,
        'title' : Lesson.objects.get(id=id).lesson_title
    }
    return render(request,'cards_lessons.html',context)

def add_media(request):
    return render(request,'add_media.html')
