from django.db.models import Count

from bosh_sahifa.models import Category, News
from django import template

register = template.Library()


@register.simple_tag()
def tags():
    return Category.objects.annotate(sana=Count('categories')).all()
    #News.objects.all().select_related('categoty').annotate(sana=Count('category__news'))