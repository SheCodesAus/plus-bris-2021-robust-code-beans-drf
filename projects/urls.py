from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
path('projects/', views.ProfileList.as_view()),
path('projects/<int:pk>/', views.ProfileDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)

