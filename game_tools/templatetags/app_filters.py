from django import template

from dma.dnd.treasure import gemsValue, jewelryValue

register = template.Library()

@register.filter
def gems_total_value(gem_list):
    return gemsValue(gem_list)
    
@register.filter
def jewelry_total_value(j_list):
    return jewelryValue(j_list)