from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
path('projects/', views.ProfileList.as_view()),
path('projects/<int:pk>/', views.ProfileDetail.as_view()),
path('', include('users.urls'))
]

urlpatterns = format_suffix_patterns(urlpatterns)

