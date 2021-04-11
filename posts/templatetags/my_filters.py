from django import template

register = template.Library()

@register.filter
def hashtag_link(post):
    content = post.content
    tags = post.hashtags.all()

    for tag in tags:
        content = content.replace(tag.content, f'<a href="/posts/hashtags/{tag.pk}">{tag.content}</a>')

    return content
