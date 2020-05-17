"""djangonautic URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from .import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings
from articles import views as article_views
from django.contrib.sitemaps.views import sitemap
from technohub.sitemaps import ArticleSitemap,CategorySitemap
from technohub.sitemaps import StaticViewSitemap
from django.views.generic import TemplateView

sitemaps={
    'articles':ArticleSitemap,
    'category':CategorySitemap,
    'static':StaticViewSitemap,
}
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/',include('accounts.urls')),
    url(r'^articles/',include('articles.urls')),
    url('sitemap.xml',sitemap,{'sitemaps':sitemaps}),
    url(r'^$',views.homepage,name="home"),
    url(r'^like/$', article_views.like_post, name='like_post'),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),

    #url(r'^category/(?P<hierarchy>.+)/$', article_views.show_category, name='category')

]
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
urlpatterns += [
    url('ads.txt', TemplateView.as_view(template_name="ads.txt", content_type='text/plain'),name='ads'),
]
urlpatterns += [
    url('BingSiteAuth.xml', TemplateView.as_view(template_name="BingSiteAuth.xml", content_type='text/xml'),name="BingSiteAuth.xml"),
]
