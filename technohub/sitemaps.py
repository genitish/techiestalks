from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from articles.models import Article,Category
#from accounts.urls import login,signup
class ArticleSitemap(Sitemap):
		priority = 0.5
		changefreq = 'daily'
		protocol='https'
		def items(self):
			return Article.objects.all().filter(status="PUBLISHED")
		def lastmod(self, obj):
			return obj.date

class CategorySitemap(Sitemap):
	priority = 0.5
	changefreq = 'daily'
	protocol='https'
	def items(self):
		return Category.objects.all()
	#def lastmod(self, obj):
	#	return obj.date

class StaticViewSitemap(Sitemap):
	priority = 0.5
	changefreq = 'daily'
	protocol='https'
	def items(self):
		return ['accounts:signup','accounts:login','articles:create','home','ads']
	def location(self,item):
		return reverse(item)
