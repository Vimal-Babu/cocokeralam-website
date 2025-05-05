from datetime import datetime
from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from home.models import Product

class StaticSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.5
    protocol = 'https'
 
    def items(self):
        return ['indexPage', 'aboutPage', 'contactPage', 'productsPage', 'termandconditionPage', 'cancellationandrefundPage', 'privacyandpolicyPage', 'shippinganddeliveryPage',]
 
    def location(self, item):
        return reverse(item)
    
    def lastmod(self, item):
        return datetime(2025, 3, 3)
    
class ProductSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.5
    protocol = 'https'

    def items(self):
        return Product.objects.all()

    def lastmod(self, item):
        return item.updated_at