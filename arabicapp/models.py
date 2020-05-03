from django.db import models
from django.conf import settings
from django.utils import timezone

class Lesson(models.Model):
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    lesson_title = models.CharField(max_length=200)
    LESSON_TYPES = (
        ('LISTENING','LISTENING'),
        ('READING','READING'),
        ('WRITING','WRITING'),
        ('SPEAKING','SPEAKING'),
        ('MISCELLANEOUS','MISCELLANEOUS'),

    )
    lesson_type = models.CharField(max_length=20, choices=LESSON_TYPES)
    LESSON_LEVEL = (
        ('BEGINNER','BEGINNER'),
        ('INTERMEDIATE','INTERMEDIATE'),
        ('PROFESSIONAL','PROFESSIONAL'),
        ('OTHER','OTHER'),

    )

    lesson_level = models.CharField(max_length=20, choices=LESSON_LEVEL)
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
    CARD_TYPE=(
        ('AUDIO','AUDIO'),
        ('VIDEO','VIDEO'),
        ('ANIMATION','ANIMATION'),
        ('IMAGE','IMAGE'),
        ('PDF','PDF'),
        ('MISCELLANEOUS','MISCELLANEOUS'),

    )
    card_type = models.CharField(max_length=20, choices=CARD_TYPE)
    card_title= models.CharField(default='Lesson Card', max_length=200)
    media_data_src = models.FileField(upload_to='material/')
    created_date = models.DateTimeField(default=timezone.now)
    status = models.BooleanField(default=True)

    def add_card(self):
        self.created_date = timezone.now()
        self.save()
    
    def __str__(self):
        return self.card_title +' -- '+self.card_type 
