from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.contrib.sitemaps.views import sitemap
from django.views.generic.base import TemplateView
from .sitemap import StaticSitemap, ProductSitemap

sitemaps = {
    'home': StaticSitemap,
    'ProductSitemap':ProductSitemap
}



urlpatterns = [
    path("admin/", admin.site.urls),
    path('',  include('home.urls')),
    path('robots.txt', TemplateView.as_view(template_name="home/robots.txt", content_type="text/plain"),),
    path('googleaa93c46e2efe273f.html', TemplateView.as_view(template_name="home/googleaa93c46e2efe273f.html", content_type="text/plain"),),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
]

# Product static and media file 
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root =settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root =settings.MEDIA_ROOT)
