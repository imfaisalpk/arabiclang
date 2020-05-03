from django.db import models
from django.conf import settings
from django.utils import timezone

class Lesson(models.Model):
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    lesson_title = models.CharField(max_length=200)
    lesson_type = models.CharField(max_length=200)
    lesson_level = models.CharField(max_length=200)
    description = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    status = models.BooleanField(default=True)

    def add_lesson(self):
        self.created_date = timezone.now()
        self.save()

    def __str__(self):
        return self.lesson_title


class LessonCard(models.Model):
    lesson_id = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    card_type = models.CharField(max_length=100)
    media_data_src = models.FileField(upload_to='material/')
    created_date = models.DateTimeField(default=timezone.now)
    status = models.BooleanField(default=True)

    def add_card(self):
        self.created_date = timezone.now()
        self.save()
    
    def __str__(self):
        return self.card_type
