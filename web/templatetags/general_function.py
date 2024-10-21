from django import template
import locale

register = template.Library()

@register.filter
def format_rupiah(amount):
    locale.setlocale(locale.LC_ALL, 'id_ID.UTF-8')
    return locale.currency(amount, symbol='Rp', grouping=True)
