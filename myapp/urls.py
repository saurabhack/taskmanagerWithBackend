from django.urls import path
from . import views

urlpatterns=[
    path('', views.index,name='index'),
    path('del/<str:item_id>', views.remove,name='del'),
    path('form',views.form,name='form'),
    path('com', views.complete,name='com')
    
]