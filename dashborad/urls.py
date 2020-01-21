from django.urls import path

from dashborad.views import IndexView

app_name = 'dashborad'
urlpatterns = [
    path('', IndexView.as_view(), name='index'),
]
