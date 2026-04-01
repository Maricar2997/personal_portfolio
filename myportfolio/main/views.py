from django.shortcuts import render
from .models import Skill, Project, Education

def home(request):
    return render(request, 'main/home.html', {
        'name': 'Maricar Pordan',
        'skills': Skill.objects.all(),
        'projects': Project.objects.all(),
        'education': Education.objects.all(),
    })


