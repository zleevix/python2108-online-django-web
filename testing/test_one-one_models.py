import os
import sys
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myweb.settings')
django.setup()
os.getcwd()
# '/Users/lehungvi/OneDrive-NVC3/OneDrive - NVC/T3H Classes/T3H-PYTHON2108E/DjangoWeb/myweb'
from myapp.models import Place, Restaurant
# Lay tat ca Place
# print(Place.objects.all())
# <QuerySet [<Place: Takashimya the place>]>
# Place.objects.all() # == SELECT * FROM Place;
# <QuerySet [<Place: Takashimya the place>]>
# Restaurant.objects.all()
# <QuerySet [<Restaurant: Takashimya the restaurant>]>
# Them moi 1 Place
# place = Place(name="Ben Thanh Market", address = "Quan 1", country = "Viet Nam")
# place.save()
# INSERT INTO Place(name, address, country) VALUES ("Ben Thanh Market", "Quan 1", "Viet Nam")
# place1 = Place.objects.create(name = "SaiGon Square", address="Quan 1", country="Viet Nam")
# place1
# <Place: SaiGon Square the place>
# Khi dùng khơi tạo từ class thì phải có bien.save() thì moi luu vao db. Còn dùng class.objects.create() không can paho .save()
# place_id1 = Place.objects.get(id=1) # == SELECT * FROM Place WHERE id = 1;
# place_id1
# <Place: Takashimya the place>
# rest1 = Restaurant.objects.get(place_id = place_id1.id)
# rest1
# <Restaurant: Takashimya the restaurant>
# rest1 = Restaurant.objects.get(place = place_id1) # Láya theo tên trong định nghĩa class
# rest1
# <Restaurant: Takashimya the restaurant>
# place_id1.restaurant # tên class Restaurant viết thuong
# <Restaurant: Takashimya the restaurant>
# place_id1.restaurant # SELECT * FROM Place, Restaurant WHERE Place.id = Restaurant.place_id AND Place.id = 1;
# <Restaurant: Takashimya the restaurant>
# SELECT * FROM Place, Restaurant WHERE Place.id = Restaurant.place_id AND Place.id = 1;
# SELECT * FROM Place INNER JOIN Restaurant ON Place.id = Restaurant.place_id WHERE id = 1;
# rest1
# <Restaurant: Takashimya the restaurant>
# rest1.place
# <Place: Takashimya the place>
# rest1.place.name
# 'Takashimya'
# place_id1.restaurant.serves_pho
# True
# "Co ban phở" if place_id1.restaurant.serves_pho else "Khong ban"
# 'Co ban phở'