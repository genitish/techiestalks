from django.http import HttpResponse
from django.shortcuts import render
from contact.forms import ContactForm
from articles.models import Category,Article,Home

def homepage(request):
    h=Home.objects.all()
    categories=Category.objects.all()
    articles=Article.objects.all()[:3]

    if request.method=='POST':
    	form=ContactForm(request.POST )
    	if form.is_valid():
    		form.save()
    else:
    	form=ContactForm()
    #meta=h[0].as_meta()
    return render(request,"home.html",{'form':form,'categories':categories,'articles':articles})
