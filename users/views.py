from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm
from .models import Profile
from .forms import ProfileForm

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirect to login after successful signup
    else:
        form = CustomUserCreationForm()
    return render(request, 'users/register.html', {'form': form})

@login_required
def profile(request):
    return render(request, 'users/profile.html')


@login_required
def profile_detail(request):
    profile = get_object_or_404(Profile, user=request.user)
    return render(request, 'users/profile.html', {'profile': profile})

@login_required
def profile_edit(request):
    user = request.user
    # Fetch or create the profile for the logged-in user
    profile, created = Profile.objects.get_or_create(user=user)

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile, user=user)
        if form.is_valid():
            form.save()  # Save the profile data
            user.email = form.cleaned_data.get('email')  # Save email separately
            user.save()  # Save the user instance
            return redirect('profile')  # Redirect to the profile page
    else:
        form = ProfileForm(instance=profile, user=user)

    return render(request, 'users/profile_edit.html', {'form': form})


@login_required
def profile_delete(request):
    user = request.user
    if request.method == "POST":
        # Delete the user and all associated data
        user.delete()

        messages.success(request, "Your account has been deleted successfully.")
        return redirect('home')  # Redirect to a page after deletion (e.g., homepage)

    return render(request, 'users/profile_delete.html', {'user': user})