from django.urls import path
from . import views 

urlpatterns = [
    path('',views.GeneratePassword.as_view())
]
