from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User

from .utils import searchProfiles
from .models import Profile
from .forms import CustomUserCreationForm, ProfileForm, SkillForm

# Create your views here.
def loginPage(request):
    page = "login"
    context = {"page":page}
    if request.user.is_authenticated:
        return redirect("profiles")

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        try:
            user = Profile.objects.get(name = username)
        except:
            pass

        user = authenticate(request, username = username, password = password)
        if user is not None:
            login(request, user)
            return redirect(request.GET['next'] if next in request.GET else "account")
        
        else:
            pass
        
    return render(request, "users/login_page.html", context = context)

def logoutPage(request):
    logout(request)
    messages.info(request, "User Logged Out!!") 
    return redirect("login")

def UserRegistration(request):
    form  = CustomUserCreationForm()
    page = "register"
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()        
            user.save()

            login(request, user)
            return redirect("edit_account")
        else:
            pass
    context = {"page":page, "form":form}
    return render(request, "users/login_page.html", context= context)

def profiles(request):
    profiles, search_query = searchProfiles(request)

    context = {"profiles" : profiles, "search_query":search_query}
    return render(request, 'users/profiles.html', context)


def user_profile(request, pk):
    user = Profile.objects.get(id = pk)
    topSkills = user.skill_set.exclude(description__exact = "") #type: ignore
    otherSkills = user.skill_set.filter(description__exact = "") #type: ignore

    context = {"user" : user, 
               "topSkills" : topSkills, 
               "otherSkills" : otherSkills}
    
    return render(request, "users/user-profile.html", context)


@login_required(login_url="login")
def userAccount(request):
    profile  = request.user.profile
    context = {"profile":profile}
    return render(request, "users/account.html", context)

@login_required(login_url="login")
def edit_account(request):
    profile = request.user.profile
    form = ProfileForm(instance = profile)

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance = profile)
        if form.is_valid():
            form.save()
            return redirect(request.GET['next'] if 'next' in request.GET else "profiles")
    context = {"form":form}
    return render(request, "users/profile_form.html", context)

@login_required(login_url="login")
def create_skill(request):
    profile = request.user.profile
    form = SkillForm()

    if request.method == "POST":
        form = SkillForm(request.POST)
        if form.is_valid():
            skill = form.save(commit = False)
            skill.owner = profile
            skill.save()
            return redirect("account")

    context = {"form":form}
    return render(request, "users/skill_form.html", context)

@login_required(login_url="login")
def update_skill(request, pk):
    profile = request.user.profile
    skill = profile.skill_set.get(id = pk)
    form = SkillForm(instance = skill)

    if request.method == "POST":
        form = SkillForm(request.POST, instance = skill)
        if form.is_valid():
            form.save()
            return redirect("account")
        
    context = {"form":form}
    return render(request, "users/skill_form.html", context)

@login_required(login_url="login")
def delete_skill(request, pk):
    profile = request.user.profile
    skill = profile.skill_set.get(id = pk)

    if request.method == "POST":
        skill.delete()
        return redirect("account")

    context = {"object":skill}
    return render(request, "delete_template.html", context)