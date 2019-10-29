from django.urls import path
from . import views
# all small_letter
urlpatterns = [
    path('', views.post_list, name='post_list'),
]