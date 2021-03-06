from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from users.forms import UserRegisterForm

# Create your views here.
class UsersView():
  def register(request):
    if request.method == 'POST':
      form = UserRegisterForm(request.POST)

      if form.is_valid():
        form.save()
        username = form.cleaned_data.get('username')
        messages.success(request, f'Account has been created for {username}, you can login now.')
        return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form, 'title': 'Register'})

  @login_required
  def profile(request):
    return render(request, 'users/profile.html', {'title': 'Profile'})