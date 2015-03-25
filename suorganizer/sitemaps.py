from blog.sitemaps import (
    PostArchiveSitemap, PostSitemap)
from organizer.sitemaps import (
    StartupSitemap, TagSitemap)

sitemaps = {
    'post-archives': PostArchiveSitemap,
    'posts': PostSitemap,
    'startups': StartupSitemap,
    'tags': TagSitemap,
}
