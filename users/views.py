from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm, update_form, prof_update_form

def register(request):
	if request.method == 'POST':
		form = UserRegistrationForm(request.POST)
		if form.is_valid():
			form.save()
			user_name = form.cleaned_data.get('username')
			messages.success(request, f'Account created - {user_name} - You can now Log In')
			return redirect('login')

	else:
		form = UserRegistrationForm()
	return render(request, 'users/register.html', {'form': form})

@login_required
def profile(request):
	if request.method == 'POST':
		user_update = update_form(request.POST, instance= request.user)
		profile_update = prof_update_form(request.POST, request.FILES, instance= request.user.profile)
		
		if user_update.is_valid() and profile_update.is_valid():
			user_update.save()
			profile_update.save()
			messages.success(request, f'Account updated')
			return redirect('profile')
	else:
		user_update = update_form(instance= request.user)
		profile_update = prof_update_form(instance= request.user.profile)

	context = {
		'user_update': user_update,
		'profile_update': profile_update
	}
	return render(request, 'users/profile.html', context)

@login_required
def predict(request):
	return render(request, 'users/playnow.html')
