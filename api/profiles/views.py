# profiles/views.py
from django.shortcuts import render, redirect
from .forms import ProfileForm
from django.contrib.auth.models import User

def create_profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            return redirect('profile_detail', pk=profile.pk)
    else:
        form = ProfileForm()
    return render(request, 'profiles/create_profile.html', {'form': form})

def profile_detail(request, pk):
    profile = User.objects.get(pk=pk).profile
    return render(request, 'profiles/profile_detail.html', {'profile': profile})
