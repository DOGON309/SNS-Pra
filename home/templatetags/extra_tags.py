# python
import re

# Django
from django import template
register = template.Library()

from django.template.defaultfilters import stringfilter
from django.utils.safestring import mark_safe


http_re = re.compile(r'(?P<url>https?://[\w./#%-:]+)')
at_re = re.compile(r'(?<![\w!@#$%&*])(?P<at>[@＠])(?P<name>\w+)')
hash_re = re.compile(r'(?<![{0}0-9_&/])(?P<hash>[#＃])(?P<word>[{0}0-9_]*[{0}]+[{0}0-9_]*)'.format(u'ｦ-ﾟー゛゜々ヾヽぁ-ヶ一-龠ａ-ｚＡ-Ｚ０-９a-zA-Z'))

def http_to_anchor(m):
    url = m.group('url')
    return '<a href="{0}" target="_blank" rel="nofollow">{0}</a>'.format(url)

def at_to_anchor(m):
    at = m.group('at')
    name = m.group('name')
    return '{0}<a href="/{1}" target="_blank" rel="nofollow">{1}</a>'.format(at, name)

def hash_to_anchor(m):
    hash = m.group('hash')
    word = m.group('word')
    return u'{0}<a href="/search/{1}" target="_blank" rel="nofollow">{1}</a>'.format(hash, word)


@register.filter(is_safe=True)
@stringfilter
def twitter_urlize(text):
    return mark_safe(hash_re.sub(hash_to_anchor, at_re.sub(at_to_anchor, http_re.sub(http_to_anchor, text))))