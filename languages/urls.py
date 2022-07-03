from django.db import router
from django.urls import path
from .import views
from rest_framework import routers
#from .views import LanguageView

router = routers.DefaultRouter()
router.register('api/languages', views.LanguageView)
router.register('api/paradigms', views.ParadigmView)
router.register('api/programmers', views.ProgrammerView)


#urlpatterns = [
#     path('', include(router.urls)),
#     path('home/',views.home, name = "home"),
#]

urlpatterns = router.urls
