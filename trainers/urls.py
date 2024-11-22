from django.urls import path, include
from . import views



urlpatterns = [
    path("trainers/", views.trainers, name="trainers"),
    path('trainers/<int:id>',
         views.trainer_detail, name='trainers-detail'),

]
