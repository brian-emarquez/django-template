# from django.shortcuts import render

# Create your views here.
# comments/views.py
from django.shortcuts import render, get_object_or_404, redirect
from .forms import CommentForm
from blog.models import Post

def add_comment_to_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('home')  # Redirigir a la página del post o a la página principal
    else:
        form = CommentForm()
    return render(request, 'comments/add_comment_to_post.html', {'form': form, 'post': post})
