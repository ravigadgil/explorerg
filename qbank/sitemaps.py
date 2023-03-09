from django.contrib.sitemaps import Sitemap
from .models import ExamHeader
from django.urls import reverse 
 
class ExamHeaderSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.64
    protocol = 'https'

    def items(self):
        return ExamHeader.objects.all()

    def lastmod(self, obj):
        return obj.date             

    def location(self,obj):
        return '/exam_preview/%s' % (obj.slug)


class StaticSitemap(Sitemap):
    changefreq = "yearly"
    priority = 0.8
    protocol = 'https'

    def items(self):
        return ['home', 'courses', 'aboutus', 'contactus']

    def location(self, item):
        return reverse(item)
