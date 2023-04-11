from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from projects.models import Project, Review, Tag
from .serializers import ProjectSerializer

@api_view(['GET','POST'])
def getRoutes(request):
    routes = [{
        "GET" : "api/projects"},
        {"GET" : "api/projects/id"},
        {"POST" : "api/projects/id/vote"},

        {"POST" : "api/users/token"},
        {"POST" : "api/users/token/refresh"},
    ]
    return Response(routes)

@api_view(['GET'])
def getProjects(request):
    projects = Project.objects.all()
    serializers = ProjectSerializer(projects, many=True)
    return Response(serializers.data)

@api_view(['GET'])
def getProject(request, pk):
    project = Project.objects.get(id = pk)
    serializers = ProjectSerializer(project, many=False)
    return Response(serializers.data)

@permission_classes([IsAuthenticated])
@api_view(['POST'])
def getVote(request, pk):
    project = Project.objects.get(id = pk)
    review, created = Review.objects.get_or_create(
        owner = request.user.profile,
        project = project,
    )
    review.vote = request.data['vote']
    review.save()
    project.VoteCalc
    
    serializer = ProjectSerializer(project, many = False)
    return Response(serializer.data)