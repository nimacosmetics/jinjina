from django.urls import path

from . import views
app_name = 'sop'
urlpatterns = [
    path('', views.index, name='index')
]