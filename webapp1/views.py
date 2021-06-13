from django.shortcuts import render
from .forms import add_blog
from .models import Blogs
# Create your views here.

def index(request):
    form1 = add_blog()
    all_blog = Blogs.objects.all()
    context = {'form1':form1, 'all_blog':all_blog}
    return render(request, 'index.html', context)