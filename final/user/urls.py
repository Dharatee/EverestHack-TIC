from django .urls import path
from . import views

urlpatterns= [
    path('appointment',views.request,name='request'),
    path('prediction',views.prediction,name='prediction')
]