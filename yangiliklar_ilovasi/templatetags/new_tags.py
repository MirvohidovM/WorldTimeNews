from django.db.models import Count

from bosh_sahifa.models import  Category
from django import template

register = template.Library()


@register.simple_tag()
def tags():
    return Category.objects.all().annotate(sana=Count('news'))
    #News.objects.all().select_related('categoty').annotate(sana=Count('category__news'))