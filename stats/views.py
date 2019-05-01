from django.shortcuts import render
from .models import Team


# Create your views here.
def team_list(request):
    teams = Team.objects.all()
    return render(request, 'stats/team_list.html', {'teams': teams})

def team_detail(request, pk):
    #pk is short for primary key, 
    team = Team.objects.get(id=pk)
    return render(request, 'stats/team_detail.html', {'team': team})
