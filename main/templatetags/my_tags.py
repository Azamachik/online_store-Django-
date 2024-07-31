from django import template
from goods.models import Categories

register = template.Library()


@register.inclusion_tag('main/list_categories.html')
def show_categories(cat_selected: int = 0) -> dict:
    return {'cats': Categories.objects.all(),
            'cat_selected': cat_selected,
            }