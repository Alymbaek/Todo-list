from .models import Task
from modeltranslation.translator import TranslationOptions,register

@register(Task)
class ProductTranslationOptions(TranslationOptions):
    fields = ('title', 'description')