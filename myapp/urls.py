from django.conf.urls import url
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views # Đứng folder hiện tai, import của file views.py
from . import class_base_views
from . import user_views
# from .views import * # Import tất cả file views.py

urlpatterns = [
    url(r'^$', views.index, name="index"),
    # r'^welcome$': Nó sẽ bắt chính xác chữ welcome: path == welcome
    # r'^welcome': Chỉ cần bắt đầu là chữ welcome: path.startswith(welcome)
    url(r'^welcome$', views.welcome, name="welcome"),
    # Đăng ký/thêm mới vào file urls.py của webapp

    # Functions Views của Place
    url(r'^place/list$', views.list_places, name='list_places'),
    url(r'^place/search$', views.search_places, name='search_places'),
    url(r'^place/validdate-name$', views.validate_name, name='validate_name'),
    url(r'^place/add$', views.add_place, name='add_place'),
    url(r'^place/detail/(?P<place_id>[0-9]+)$', views.view_detail_place, name='view_detail_place'),
    url(r'^place/update/(?P<place_id>[0-9]+)$', views.update_place, name='update_place'),
    url(r'^place/delete/(?P<place_id>[0-9]+)$', views.delete_place, name='delete_place'),
    url(r'^place/confirm-delete/(?P<place_id>[0-9]+)$', views.confirm_delete, name='confirm_delete'),
    # path('place/detail/<int:place_id>', views.view_detail_place, name='view_detail_place'),
    url(r'^restaurant/add$', views.add_restaurant, name='add_restaurant'),
    url(r'^restaurant/list$', views.list_restaurants, name='list_restaurants'),
    url(r'^restaurant/update/(?P<place_id>[0-9]+)$', views.update_restaurant, name='update_restaurant'),
    url(r'^waiter/add$', views.add_waiter, name='add_waiter'),
    url(r'^waiter/list$', views.list_waiters, name='list_waiters'),

    # Class View của Place
    url(r'^class/place/list$', class_base_views.PlaceListView.as_view(), name='class_list_places'),
    url(r'^class/place/detail/(?P<pk>[0-9a-z]+)$', class_base_views.PlaceDetailView.as_view(), name='class_view_detail_place'),
    url(r'^class/place/add$', class_base_views.PlaceCreateView.as_view(), name='class_add_place'),
    url(r'^class/place/update/(?P<pk>[0-9]+)$', class_base_views.PlaceUpdateView.as_view(), name='class_update_place'),
    url(r'^class/place/delete/(?P<pk>[0-9]+)$', class_base_views.PlaceDeleteView.as_view(), name='class_delete_place'),

    url(r'^class/restaurant/list$', class_base_views.RestaurantListView.as_view(), name='class_list_restaurants'),
    url(r'^class/restaurant/detail/(?P<pk>[0-9]+)$', class_base_views.RestaurantDetailView.as_view(), name='class_view_detail_restaurant'),
    url(r'^class/restaurant/add$', class_base_views.RestaurantCreateView.as_view(), name='class_add_restaurant'),
    url(r'^class/restaurant/update/(?P<pk>[0-9]+)$', class_base_views.RestaurantUpdateView.as_view(), name='class_update_restaurant'),
    url(r'^class/restaurant/delete/(?P<pk>[0-9]+)$', class_base_views.RestaurantDeleteView.as_view(), name='class_delete_restaurant'),

    url(r'^class/waiter/list$', class_base_views.WaiterListView.as_view(), name='class_list_waiters'),
    url(r'^class/waiter/detail/(?P<pk>[0-9a-z]+)$', class_base_views.WaiterDetailView.as_view(), name='class_view_detail_waiter'),
    url(r'^class/waiter/add$', class_base_views.WaiterCreateView.as_view(), name='class_add_waiter'),
    url(r'^class/waiter/update/(?P<pk>[0-9]+)$', class_base_views.WaiterUpdateView.as_view(), name='class_update_waiter'),
    url(r'^class/waiter/delete/(?P<pk>[0-9]+)$', class_base_views.WaiterDeleteView.as_view(), name='class_delete_waiter'),

    url(r'^register$', user_views.register_user, name='register_user'),
    url(r'^login$', user_views.login_user, name='login_user'),
    url(r'^logout$', auth_views.LogoutView.as_view(next_page="login_user"), name='logout_user'),

    url(r'^articles$', views.list_articles, name='list_articles'),
]