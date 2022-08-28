from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import Staff
from .forms import StaffInsertForm
from django.contrib import messages




def ShowStaffInfo(request):
    all_Staff = Staff.objects.all()

    context={
        'all_staff': all_Staff
    }
    return render(request,'store/staff_list.html',context)



@login_required
def CreateProfile(request):
    form = StaffInsertForm()
    if request.method == "POST":
        form = StaffInsertForm(request.POST, request.FILES)

    if form.is_valid():
        profile_object = form.save(commit=False)
        profile_object.user = request.user
        profile_object.save()
        return redirect('/')
    try:
        value = Staff.objects.get(user=request.user)
    except Staff.DoesNotExist:
        value = '0'
    context = {
        'val': value,
        'form': form,
    }
    return render(request, 'Profile/create_profile.html', context)

def ViewProfile(request):
    try:
        profile = Staff.objects.get(user=request.user)
    except Staff.DoesNotExist:
        profile = print("Please complete your Profile to view")
    context = {
        'profile': profile,
    }
    return render(request, 'Profile/view_profile.html', context)















