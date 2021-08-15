from bosh_sahifa.models import  News
from django import template

register = template.Library()

@register.simple_tag()
def teglar(category_id):
    return News.objects.filter(category_id=category_id)