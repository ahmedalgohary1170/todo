from django.urls import path
from .views import todolist,tododatial
urlpatterns = [
    path('',todolist),
    path('/<int:pk>/',tododatial)

]
