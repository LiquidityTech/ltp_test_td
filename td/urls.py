from django.urls import path
from td import views

urlpatterns = [
    path("", views.td_req, name="td demo"),



]



