from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from users.models import skill
from .forms import ProjectForm, ReviewForm, ProjectFormTemp
from .models import Project, Tag
from .utils import searchProjects

def projects(request):
    Projects, search_query  = searchProjects(request)

    context = {
            "projects":Projects, 
            "search_query":search_query
               }

    return render(request, "projects/projects.html", context = context)
 

def project(request, pk):
    project = Project.objects.get(id = pk)
    tags = project.tags.all()

    form = ReviewForm()

    if request.method == 'POST':
        form = ReviewForm(request.POST)

        review = form.save(commit = False)
        review.owner =  request.user.profile
        review.project = project
        review.save()

        project.VoteCalc

        return redirect("project", pk = project.id) #type:ignore

    return render(request, "projects/single-project.html", {"project" : project, "tags" : tags, "form":form})


@login_required(login_url = "login")
def create_project(request):
    profile = request.user.profile
    form = ProjectFormTemp()
    if request.method == 'POST':
        form = ProjectFormTemp(request.POST, request.FILES)

        if form.is_valid():
            project = form.save(commit = False)
            project.owner = profile
            project.save()

            for tag in project.tags.all():
                sk, created = skill.objects.get_or_create(
                    name = tag,
                    owner = profile
                )
            
            return redirect("projects")
    context = {"form": form}
    return render(request, "projects/projects_form.html", context)

@login_required(login_url = "login")
def update_project(request, pk):
    profile = request.user.profile
    project = profile.project_set.get(id=pk)
    form = ProjectFormTemp(instance=project)

    if request.method == 'POST':
        form = ProjectFormTemp(request.POST, request.FILES, instance=project)
        if form.is_valid():
            form.save()
            for tag in project.tags.all():
                sk, created = skill.objects.get_or_create(
                    name = tag,
                    owner = profile
                )
            return redirect("projects")

        
    context = {"form": form}
    return render(request, "projects/projects_form.html", context)

@login_required(login_url = "login")
def delete_project(request, pk):
    project = Project.objects.get(id = pk)
    if request.method == 'POST':
        project.delete()
        return redirect("projects")
    context = {'object' : project}
    return render(request, 'delete_template.html', context)
    
