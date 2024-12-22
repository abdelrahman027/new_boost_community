from django.urls import path, include
from . import views



urlpatterns = [
    path("trainers/", views.trainers, name="trainers"),
    path('trainers/<int:id>',
         views.trainer_detail, name='trainers-detail'),
    path('trainers/delete/<int:id>/<int:trainer_id>',
         views.delete_Commeent, name='delete_comment'),
    path("trainers/visa", views.trainer_visas, name="trainers_visa"),
    path("trainers/flights", views.trainer_flights, name="trainers_flights"),
]
