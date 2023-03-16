
from django.urls import path,include

from . import views
from . import movie_service as dynamodb
urlpatterns = [
    path('createTable', views.create_table),
    path('readCSV', views.readCSV),
    path('readtitle/<str:director>/<str:year1>/<str:year2>',views.read_from_movie),
    path('review/<str:review>', views.user_review)

]