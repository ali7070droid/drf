from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from Music import views


urlpatterns = [
    path('music/',views.ArtistList.as_view()),
    path('music/<int:pk>', views.ArtistDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)