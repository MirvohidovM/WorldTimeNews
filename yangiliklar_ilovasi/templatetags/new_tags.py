from django.db.models import Count

from bosh_sahifa.models import  Category
from django import template

register = template.Library()

@register.simple_tag()
def teglar():
    return  Category.objects.all()

@register.simple_tag()
def tags():
    return Category.objects.annotate(sana=Count('news'))