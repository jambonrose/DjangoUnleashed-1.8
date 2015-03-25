from blog.sitemaps import PostSitemap
from organizer.sitemaps import (
    StartupSitemap, TagSitemap)

sitemaps = {
    'posts': PostSitemap,
    'startups': StartupSitemap,
    'tags': TagSitemap,
}
