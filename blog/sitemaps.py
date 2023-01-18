from django.contrib.sitemaps import Sitemap
from .models import Post

class PostSitemap(Sitemap):
    # Set frequency and priority
    changefreq = 'weekly'
    priority = 0.7
    
    
def items(self):
    # List of posts
    return Post.published.all()

def lastmod(self, obj):
    # Check last modification
    return obj.updated

