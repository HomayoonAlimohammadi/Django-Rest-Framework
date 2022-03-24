from django.urls import path
from .views import * 

urlpatterns = [
    path('', snippet_list),
    path('<int:pk>/', snippet_detail),
]