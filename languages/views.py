from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import Language,Paradigm,Programmer
from .serializers import LanguageSerializer,ParadigmSerializer,ProgrammerSerializer
# Create your views here.

class LanguageView(viewsets.ModelViewSet):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer
    #template_name = "languages/home.html"
    #permission_classes =(permissions.IsAuthenticatedOrReadOnly,)

#def home(request):
#    return render(request, languages/home.html, name = "home")


class ParadigmView(viewsets.ModelViewSet):
    queryset = Paradigm.objects.all()
    serializer_class = ParadigmSerializer
    #permission_classes =(permissions.IsAuthenticatedOrReadOnly,)

class ProgrammerView(viewsets.ModelViewSet):
    queryset = Programmer.objects.all()
    serializer_class = ProgrammerSerializer