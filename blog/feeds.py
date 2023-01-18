import markdown
from django.contrib.syndication.views import Feed
from django.template.defaultfilters import truncatewords_html
from django.urls import reverse_lazy
from .models import Post


class LatestPostsFeed(Feed):
    title = 'My blog'
    link = reverse_lazy('blog:post_list')
    description = 'New posts of my blog.'
    
    
    def items(self):
        # Get last 5 posts
        return Post.published.all()[:5]

    def item_title(self, item):
        # Return title
        return item.title

    def item_description(self, item):
        # Convert markdown to html
        return truncatewords_html(markdown.markdown(item.body), 30)

    def item_pubdate(self, item):
        # Return publish date
        return item.publish