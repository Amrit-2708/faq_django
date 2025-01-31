from django.db import models
from django.utils.translation import gettext_lazy as _
from ckeditor.fields import RichTextField

class FAQ(models.Model):
    LANGUAGE_CHOICES = [
        ('en', 'English'),
        ('hi', 'Hindi'),
        ('bn', 'Bengali'),
    ]
    
    question = models.TextField(verbose_name=_("Question"))
    answer = RichTextField(verbose_name=_("Answer"))
    
    question_hi = models.TextField(blank=True, null=True, verbose_name=_("Question in Hindi"))
    question_bn = models.TextField(blank=True, null=True, verbose_name=_("Question in Bengali"))
    answer_hi = RichTextField(blank=True, null=True, verbose_name=_("Answer in Hindi"))
    answer_bn = RichTextField(blank=True, null=True, verbose_name=_("Answer in Bengali"))
    
    def get_translated_question(self, lang_code):
        # TODO: Implement transalation
        return self.question
    
    def get_translated_answer(self, lang_code):
        # TODO: Implement transalation
        return self.answer
    
    def __str__(self):
        return self.question