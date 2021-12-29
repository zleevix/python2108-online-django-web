import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myweb.settings')
django.setup()
from myapp.models import Place, Restaurant

keyword = input("Hãy nhập từ khoá cần tìm: ")
matched_places = Place.objects.filter(name__contains=keyword)
matched_restaurants = Restaurant.objects.filter(place__name__contains=keyword)
# name là tên trường
# __contains == LIKE SQL
print("Danh sách các Places tìm được")
print("{0:>5}{1:>20}{2:>20}".format("ID", "Tên", "Địa Chỉ"))
for place in matched_places:
    print("{0:>5}{1:>20}{2:>20}".format(place.id, place.name, place.address))

print("Danh sách các Restaurants tìm được")
# print("{0:>5}{1:>20}{2:>20}".format("ID", "Tên", "Địa Chỉ"))
for restaurant in matched_restaurants:
    print(restaurant)
    # print("{0:>5}{1:>20}{2:>20}".format(restaurant.place.name, place.name, place.address))