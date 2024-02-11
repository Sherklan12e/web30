from django.shortcuts import render
from .models import Post
from django.shortcuts import get_object_or_404

def index(request):
    todo = Post.objects.all()
    
    return render(request, 'index.html',{'todo':todo})

def detalles(request, detalles):
    post = get_object_or_404(Post ,id=detalles)
    return render(request, 'Blog/detalle.html',{'post':post})



def caseros(request):
    todo = Post.objects.all()
    
    return render(request, 'index.html',{'todo':todo})

def packs(request):
    todo = Post.objects.all()
    
    return render(request, 'index.html',{'todo':todo})

