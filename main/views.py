from django.shortcuts import render
from .models import *
# Create your views here.
def home(request):
    posts = Blog.objects.all()
    return render(request, 'home.html', {'ob_posts':posts, }) 