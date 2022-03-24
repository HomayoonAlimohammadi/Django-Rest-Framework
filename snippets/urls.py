from django.urls import path
from .views import * 

app_name = 'snippets'
urlpatterns = [
    path('snippets/', snippet_list, name='list'),
    path('snippets/<int:pk>/', snippet_detail, name='detail'),
]