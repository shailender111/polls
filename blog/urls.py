from django.urls import path
from . import views


app_name = 'blog'
urlpatterns = [
    path('', views.PollListView.as_view(), name="home"),
    path('about/<int:pk>', views.PollDetailView.as_view(), name='about'),
    path('vote/<int:pk>', views.vote, name='vote'),
    path('results/<int:pk>', views.PollResultView.as_view(), name='results'),
]
