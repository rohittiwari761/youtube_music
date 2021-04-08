from django import template

register =template.Library()


def split(string, sep):
    """Return the string split by sep.

    Example usage: {{ value|split:"/" }}
    """
    return string.split(sep,1)[0]
register.filter('split',split)
