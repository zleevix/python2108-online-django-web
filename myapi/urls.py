from django.conf.urls import url
from . import views # Đứng folder hiện tai, import của file views.py
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    url(r"^token$", jwt_views.TokenObtainPairView.as_view(), name='get_token'), # Lầy token
    url(r"^token/refresh$", jwt_views.TokenRefreshView.as_view(), name='refresh_token'), # Refresh khi mà token hết hạn/experid
    url(r"^places$", views.api_list_places, name='api_list_places'),
    url(r"^add-place$", views.api_add_place, name='api_add_place'),
    
    url(r"^place/(?P<place_id>[0-9]+)$", views.api_view_place, name='api_view_place'),
    url(r"^update-place/(?P<place_id>[0-9]+)$", views.api_update_place, name='api_update_place'),
    url(r"^delete-place/(?P<place_id>[0-9]+)$", views.api_delete_place, name='api_delete_place'),

    url(r"^class/places$", views.PlaceListAPI.as_view()),
    url(r"^class/place/(?P<place_id>[0-9]+)$", views.PlaceAPI.as_view()),
]