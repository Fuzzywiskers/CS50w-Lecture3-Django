from django.urls import path

from . import views         #import from . (aka current directory) import views#

urlpatterns = [
    path("", views.index, name="index"),     #when user is at "" url then the views.index function will run with a nicname of "index"#
    path("<str:name>", views.greet, name="greet"),      #call greet functoin from greet function when url is just an unspecificed name#
    path("malia", views.malia, name="malia"),    #calls upon malia function from views when url has malia#
]