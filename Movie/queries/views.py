from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status

from . import movie_service as dynamodb
from rest_framework.decorators import api_view

@api_view(['GET'])
def create_table(request):
    try:
        print(dynamodb.create_table_movie())
        return JsonResponse('Movie table created', status=status.HTTP_201_CREATED,safe=False)
    except:
        return JsonResponse('error while creating table',status=status.HTTP_500_INTERNAL_SERVER_ERROR, safe=False)


@api_view(['GET'])
def readCSV(request):
    # print("enterted views")
    try:
        dynamodb.read_csv_file()
        return JsonResponse('CSV inserted to database', status=status.HTTP_201_CREATED,safe=False)
    except:
        return JsonResponse('error while inserting table',status=status.HTTP_500_INTERNAL_SERVER_ERROR, safe=False)

#
@api_view(['GET'])
def read_from_movie(request,director,year1,year2):
    director = director
    year1 = int(year1)
    year2 = int(year2)
    # if year1==year2 or year1>year2 or year1<0 or year2<0:
    #     Exception (JsonResponse('please enter valid years', status=status.HTTP_500_INTERNAL_SERVER_ERROR, safe=False))

    try:
        # dynamodb.read_movie(director,year1,year2)
        return JsonResponse(dynamodb.read_movie(director,year1,year2), status=status.HTTP_201_CREATED,safe=False)
    except:
        return JsonResponse('error while running the query',status=status.HTTP_500_INTERNAL_SERVER_ERROR, safe=False)

@api_view(['GET'])
def user_review(request, review):
    review = int(review)
    try:
        # dynamodb.read_movie(director,year1,year2)
        return JsonResponse(dynamodb.review_movie(review), status=status.HTTP_201_CREATED,safe=False)
    except:
        return JsonResponse('error while running the query',status=status.HTTP_500_INTERNAL_SERVER_ERROR, safe=False)








