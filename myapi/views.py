from django.db import reset_queries
from django.shortcuts import render


# Create your views here.
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from myapp.models import Place, Restaurant
from .my_serializers import PlaceSerializer

# CURD trong API
# REST API : cần cung cấp URL + HTTP Method
# HTTP Method: GET, POST, PUT, PATCH, DELETE, OPTIONS, .....
# CURD
# Dùng method 
# 
# GET : lấy thông tin về: list data và view detail data. (R)
# POST: tạo mới dữ liệu (C)
# PUT: chỉnh sửa dữ liệu (U) + thông để xác định. Dữ liệu gửi lên server và dữ liệu nhậ thì phải có tất cả thuộc tính của đối tương đó
# PATCH: chỉnh sửa dữ liệu (U)  + thông để xác định. Client muốn chỉnh sửa thuộc tính nào thì gửi lên dữ liệu đó.
# DELET: xoá dữ liệu (D)
# OPTIONS: thường là dùng để kiểm tra xem server nó hổ trợ những methods

# Xác định được lỗi từ server trả về
# HTTP Status
# 200 -> OK không có lỗi
# 201 Created
# 204 No content

# 404 Not Found
# 403 Forbidden
# 405 Method Not Allowed
# 409 Conflict
# 401 Unauthorization
# 500 Internal Server
# 400 Bad Request

# Content-type: kiễu dữ liệu gửi/nhận
# application/json: JSON
# application/xml

# R: list all
@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def api_list_places(request):
    places = Place.objects.all()
    mydata = PlaceSerializer(places, many=True)
    # results = []
    # for place in places:
    #     data = {
    #         'id': place.id,
    #         'name': place.name,
    #         'address': place.address,
    #         'country': place.country
    #     }
    #     if Restaurant.objects.filter(place = place).exists():
    #         data['restaurant'] = {
    #             'serves_pizza': place.restaurant.serves_pizza,
    #             'serves_hot_dogs': place.restaurant.serves_hot_dogs,
    #             'serves_pho': place.restaurant.serves_pho,
    #         }
    #     results.append(data)
    return Response(data=mydata.data, status=200)

@permission_classes((IsAuthenticated,))
@api_view(['GET'])
def api_view_place(request, place_id):
    try:
        place = Place.objects.get(id=place_id)
        # result = {
        #     'id': place.id,
        #     'name': place.name,
        #     'address': place.address,
        #     'country': place.country
        # }
        mydata = PlaceSerializer(instance=place)
        print(mydata.data)
        return Response(data=mydata.data,status=200)
    except Place.DoesNotExist:
        return Response(data={
            "message": f"Place with '{place_id}' not found"
        }, status=404)

# C
# Method: POST
@api_view(['POST'])
def api_add_place(request):
    data = PlaceSerializer(data = request.data)
    if data.is_valid():
        print("Valided: ", data.validated_data)
        data.save()
        return Response( status=201)
    else:
        return Response(data=data.errors, status=409)
    # try:
    #     # Place.objects.get(name=request.data['name'])
    #     # return Response(data={
    #     #     "message": f"Place with name '{request.data['name']}' already existing. Please choose an other name"
    #     # },status=409) # Conflict: trùng data.
        

    # except Place.DoesNotExist:
    #     # Place.objects.create(
    #     #     name=request.data['name'],
    #     #     address=request.data['address'],
    #     #     country=request.data['country'],
    #     # )
    #     added_id = Place.objects.create(**request.data)
    #     return Response(data={"message": f"Place with id '{added_id.id}' created"}, status=201)

@api_view(["PUT"])
@permission_classes((IsAuthenticated,))
def api_update_place(request, place_id):
    try:
        place = Place.objects.get(id=place_id)
        place.address = request.data['address']
        place.country = request.data['country']
        place.save()
        return Response(status=204)
    except Place.DoesNotExist as e:
        return Response(data={
            "message": f"Place with '{place_id}' not found"
        }, status=404)

@api_view(["DELETE"])
@permission_classes((IsAuthenticated,))
def api_delete_place(request, place_id):
    try:
        place = Place.objects.get(id=place_id)
        place.delete()
        return Response(status=204)
    except Place.DoesNotExist as e:
        return Response(data={
            "message": f"Place with '{place_id}' not found"
        }, status=404)

class PlaceListAPI(APIView):
    # 2 APIs không có parameter: list all và add
    # liên quan đến danh sách cả Place

    def get(self, request):
        places = Place.objects.all()
        mydata = PlaceSerializer(places, many=True)
        return Response(data=mydata.data, status=200)
    
    def post(self, request):
        data = PlaceSerializer(data = request.data)
        if data.is_valid():
            print("Valided: ", data.validated_data)
            data.save()
            return Response( status=201)
        else:
            return Response(data=data.errors, status=409)
    
class PlaceAPI(APIView):

    def get(self, request, place_id):
        try:
            place = Place.objects.get(id=place_id)
            mydata = PlaceSerializer(instance=place)
            return Response(data=mydata.data,status=200)
        except Place.DoesNotExist:
            return Response(data={
                "message": f"Place with '{place_id}' not found"
            }, status=404)

    def put(self, request, place_id):
        try:
            place = Place.objects.get(id=place_id)
            place.address = request.data['address']
            place.country = request.data['country']
            place.save()
            return Response(status=204)
        except Place.DoesNotExist as e:
            return Response(data={
                "message": f"Place with '{place_id}' not found"
            }, status=404) 

    def delete(self, request, place_id):
        try:
            place = Place.objects.get(id=place_id)
            place.delete()
            return Response(status=204)
        except Place.DoesNotExist as e:
            return Response(data={
                "message": f"Place with '{place_id}' not found"
            }, status=404)
