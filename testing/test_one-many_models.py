import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myweb.settings')
django.setup()

from myapp.models import Place, Restaurant, Waiter
place1 = Place.objects.get(pk=1) # pk = id của Place
# Tên biến thì mình đạtw y chang tên class viet thuong
# Để: biết đuoc biến là từ đây 
print(place1)
restaurant = place1.restaurant
print(restaurant)
waiters = restaurant.waiter_set.all()
print(waiters)
# # Cách 1: dùng tên chính xác cột trong table -> dùng chính xác kiểu dữ lieuje tuongw ungw
# waiter1 = Waiter(name="Alice", restaurant_id=restaurant.place_id)
# waiter1.save() # Bước này quan trọng khi khởi biến từ 1 class

# # Cách 2: Tên thuộc tính định nghĩa trong class
# waiter2 = Waiter(name="Alice 1", restaurant=restaurant)
# waiter2.save() # Bước này quan trọng khi khởi biến từ 1 class

# # Cách 3: Dùng objects.create
# waiter3 = Waiter.objects.create(name="Alice 2", restaurant=restaurant)
# # Không cần .save(). Insert xong thì nó sẽ trả về biến

# # Cách 4: dùng quan hệ 1-n
# # Restaurant là class 1
# # Waiter là class n
# # Thì class 1 sẽ tự động có thể 1 attribute là waiter_set = Waiter.objects
# restaurant.waiter_set.create(name="Alice 3")
