from django import template
from main import views

register = template.Library()


@register.simple_tag(name='getcats')
def get_categories():
    return views.cats_db


@register.inclusion_tag('main/list_categories.html')
def show_categories(cat_selected: int = 0) -> dict:
    return {'cats': views.cats_db,
            'cat_selected': cat_selected,
            }