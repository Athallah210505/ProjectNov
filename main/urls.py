from django.urls import path
from main.views import show_main, create_wish, delete_wish, show_wish, show_clue

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('create_wish', create_wish , name= 'create_wish'),
    path('delete_wish/<str:id>', delete_wish, name='delete_wish'),
    path('show_wish', show_wish, name='show_wish'),
    path('show_clue', show_clue, name='show_clue'),
]