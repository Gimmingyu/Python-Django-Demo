from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
]
"""
The include() function allows referencing other URLconfs. 

Whenever Django encounters include(), it chops off whatever part of the URL matched up to that point and sends the remaining string to the included URLconf for further processing.

The idea behind include() is to make it easy to plug-and-play URLs. Since polls are in their own URLconf (polls/urls.py), they can be placed under “/polls/”, or under “/fun_polls/”, or under “/content/polls/”, or any other path root, and the app will still work.
"""