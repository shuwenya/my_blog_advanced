import markdown

from django import template
from django.template.defaultfilters import stringfilter
from django.utils.encoding import force_text
from django.utils.safestring import mark_safe
from markdown.extensions.toc import TocExtension

register = template.Library() #自定义filter时必须加上

# @符号开始的代码不是注释
@register.filter(is_safe=True)  # 注册template filter
@stringfilter  # 希望字符串作为参数
def custom_markdown(value):
    md = markdown.Markdown(extensions=['markdown.extensions.fenced_code',
                                       'markdown.extensions.codehilite',
                                       'markdown.extensions.extra',
                                       'markdown.extensions.toc', 
                                       TocExtension(slugify=slugify),],
                           safe_mode=True,
                           enable_attributes=False
                           )
    value = md.convert(value)
    if value == 'post.toc':
        value = md.toc
    return value

