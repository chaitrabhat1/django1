from django.urls import path
from . import views
urlpatterns = [
    path('t1/',views.t1,name="t1")
]
