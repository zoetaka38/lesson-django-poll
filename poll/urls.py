from django.urls import path
from poll import views as poll_views


app_name = 'poll'

urlpatterns = [
    path('', poll_views.HomeView.as_view(), name='home'),
    path('create/', poll_views.PollCreateView.as_view(), name='create'),
    path('vote/<poll_id>/', poll_views.vote, name='vote'),
    path('results/<int:pk>/', poll_views.ResultView.as_view(), name='results'),
]