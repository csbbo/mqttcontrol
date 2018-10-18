from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('w/',views.forward),
    path('s/',views.back),
    path('a/',views.left_turn),
    path('d/',views.right_turn),
    path('slow/',views.slow),
    path('genner/',views.genner),
    path('fast/',views.fast),
    path('soon/',views.soon),
]