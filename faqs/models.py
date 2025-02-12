from django.db import models
from django_ckeditor_5.fields import CKEditor5Field
from googletrans import Translator
from django.utils.html import strip_tags  # ✅ To handle HTML content

# Create your models here.
class FAQ(models.Model):
    question = models.TextField()
    answer = CKEditor5Field('Answer', config_name='default')
    question_hi = models.TextField(blank=True, null=True)

    # Hindi translation
    answer_hi = models.TextField(blank=True, null=True)

    # Bengali translation
    question_bn = models.TextField(blank=True, null=True)
    answer_bn = models.TextField(blank=True, null=True)

    def save(self, *args, **kwargs):
        translator = Translator()

        # ✅ Translate only if question exists
        if self.question and not self.question_hi:
            self.question_hi = translator.translate(
                self.question, dest='hi').text
        if self.question and not self.question_bn:
            self.question_bn = translator.translate(
                self.question, dest='bn').text

        # ✅ Strip HTML tags before translating answers
        plain_answer = strip_tags(self.answer)

        if plain_answer and not self.answer_hi:
            self.answer_hi = translator.translate(plain_answer, dest='hi').text
        if plain_answer and not self.answer_bn:
            self.answer_bn = translator.translate(plain_answer, dest='bn').text

        super().save(*args, **kwargs)  # ✅ Call parent save method

    def __str__(self):
        return self.question

