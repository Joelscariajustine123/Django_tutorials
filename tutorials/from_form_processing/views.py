from django.shortcuts import redirect, render
from .forms import UserProfileForm
from .models import UserProfile


# Create your views here.
def user_profile_view(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES)
        print(request.FILES)  
        if form.is_valid():
            form.save()
            return redirect('list_view')
    else:
        form = UserProfileForm()
    
    return render(request, 'from_form_processing/user_profile.html', {'form': form})

def list_view(request):
    profiles = UserProfile.objects.all()
    return render(request, 'from_form_processing/list_view.html', {'profiles': profiles})



from django.contrib import messages

def message_view(request):
    messages.success(request, 'This is a success message.')
    messages.error(request, 'This is an error message.')
    messages.warning(request, 'This is a warning message.')
    return render(request, 'from_form_processing/message_view.html')