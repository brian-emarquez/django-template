from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm


def home(request):
    posts = Post.objects.all()
    return render(request, 'blog/home.html', {'posts': posts})

def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  # Redirigir a una página después de guardar
    else:
        form = PostForm()
    return render(request, 'blog/create_post.html', {'form': form})

# # Create your views here.
# def home(request):
#     return HttpResponse("Hola, bienvenido a mi blog")