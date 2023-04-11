from django.db.models import Q
from .models import Project, Tag

def searchProjects(request):
    search_query = ''

    if request.GET.get("search_query"):
        search_query = request.GET.get("search_query")

    tag = Tag.objects.filter(tag_name__icontains = search_query)
    Projects = Project.objects.distinct().filter(
        Q(Title__icontains=search_query) |
        Q(Description__icontains=search_query) |
        Q(owner__name__icontains=search_query) |
        Q(tags__in=tag)
    )
    print(Projects) 
    
    return Projects, search_query