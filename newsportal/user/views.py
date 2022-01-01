from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .forms import CustomUserCreationForm, ProfileForm, InterestForm
from .models import Profile, Interest


# Create your views here.


def loginUser(request):
    if request.user.is_authenticated:
        return redirect('profile')

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        try:
            user = User.objects.get(username=username)

        except:
            print("Username does not exist")
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Username does not exist')

    return render(request, 'user/sigin.html')


def logoutUser(request):
    logout(request)
    messages.info(request, 'User Successfully logout')
    return redirect('login')


def registerUser(request):
    page = 'register'
    form = CustomUserCreationForm()

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()

            messages.success(request, 'User account was created !')

            login(request, user)
            return redirect('home')
        else:
            messages.success(request, 'An error has occurred during registration')
    context = {
        'page': page,
        'form': form
    }

    return render(request, 'user/signup.html', context=context)


@login_required(login_url='login')
def profile(request, pk):
    profiles = Profile.objects.get(id=pk)
    context = {
        'profile': profiles
    }
    return render(request, 'user/profile.html', context=context)


@login_required(login_url='login')
def userAccount(request):
    profile = request.user.profile
    interest = Interest.objects.all()
    news = profile.news_set.all()
    context = {
        'profile': profile,
        'interests': interest,
        'news': news,
    }
    return render(request, 'user/account.html', context=context)


@login_required(login_url='login')
def editAccount(request):
    profile = request.user.profile
    form = ProfileForm(instance=profile)
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('account')
    context = {'form': form}
    return render(request, 'user/profile_form.html', context=context)


@login_required(login_url='login')
def createInterest(request):
    profile = request.user.profile
    form = InterestForm()

    if request.method == 'POST':
        form = InterestForm(request.POST)
        if form.is_valid():
            interest = form.save(commit=False)
            interest.owner = profile
            interest.save()
            messages.success(request, 'Skill was added successfully!')
            return redirect('account')

    context = {'form': form}
    return render(request, 'user/skill_form.html', context)


@login_required(login_url='login')
def updateInterest(request, pk):
    profile = request.user.profile
    interest = profile.interest_set.get(id=pk)
    form = InterestForm(instance=interest)

    if request.method == 'POST':
        form = InterestForm(request.POST, instance=interest)
        if form.is_valid():
            form.save()
            messages.success(request, 'Skill was updated successfully!')
            return redirect('account')

    context = {'form': form}
    return render(request, 'user/skill_form.html', context)


@login_required(login_url='login')
def deleteInterest(request, pk):
    profile = request.user.profile
    interest = profile.interest_set.get(id=pk)
    if request.method == 'POST':
        interest.delete()
        messages.success(request, 'Skill was deleted successfully!')
        return redirect('account')

    context = {'object': interest}
    return render(request, 'delete_template.html', context)

