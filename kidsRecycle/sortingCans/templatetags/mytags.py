from django import template

register = template.Library()

register.tag(name='compost_pic')
