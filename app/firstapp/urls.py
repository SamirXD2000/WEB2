from django.urls import path

from . import views

urlpatterns = [
    #path('', views.paito, name='paito'),
    # ex: /1.0/5/
    path('states/<int:id>/', views.state, name='state'),
    path('states/', views.states, name='states'),
    #path('client/update/', views.updateclient, name='updateclient'),
    #path('client/get/', views.getclient, name='getclient'),
    #path('client/delete/', views.deleteclient, name='deleteclient'),

]
