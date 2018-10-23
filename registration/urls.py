from django.urls import path
from . import views

app_name = "registration"

urlpatterns = [
    path('', views.IndexPage.as_view(), name="index")
]