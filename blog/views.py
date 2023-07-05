from django.shortcuts import render
from django.views import generic
from django.http import HttpResponse
from blog.models import Blog
def index(request):
	return HttpResponse("index")

# def detail(request, blog_id):
# 	return HttpResponse("detail")

class DetailView(generic.DetailView):
	model = Blog
	template_name = "blog/detail.html"

	def get_query_set(self):
		return Blog.objects.all()



