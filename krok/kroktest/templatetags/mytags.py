from django import template

register = template.Library()


@register.filter
def mult(a, b):
    return a*b


@register.filter
def get(A, i):
    return A[i]
