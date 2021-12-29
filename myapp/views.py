from django.contrib.auth import login
from django.shortcuts import render, redirect, HttpResponseRedirect, get_object_or_404
from django.http.response import HttpResponse, JsonResponse
from django.db.models import Q
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required, permission_required
from django.conf import settings
import time
import datetime
# from . import models
from .models import Place, Restaurant, Waiter, Article
from .forms import PlaceForm, RestaurantForm, WaiterForm
# Function-base views: tất cả hàm đều có tham số là requerequest: HttpRequestst
# Phía back-end/server/máy chủ
# Create your views here.
def welcome(request):
    # Tham số của hàm tên là request: HttpRequest
    # Client/browser gõ URL vào thanh địa chỉ: HTTP REQUEST
    # Server nhận HTTP REQUEST
    #        trả về Client/Browser HTTP RESPONSE
    response = HttpResponse()
    response.write("<h1>Welcome to my first django web</h1>")
    response.write("<a href='https://www.djangoproject.com/'> Trang chủ django</a>")
    response.write("<h2>Danh sách các Places</h2>")
    places = Place.objects.all()
    response.write("<ul>")
    for place in places:
        if Restaurant.objects.filter(place = place).exists():
            restaurant_place = place.restaurant
            response.write(f"<li>Place: {place}, Restaurant: {restaurant_place}")
            response.write("<ol>")
            for waiter in restaurant_place.waiter_set.all():
                response.write(f"<li>{waiter.name}</li>")
            response.write("</ol></li>")
        else:
            response.write(f"<li>Place: {place}</li>")
    response.write("</ul>")
    return response

def index(request):
    # Mình truyền xữ liệu từ python cho HTML hiển thị
    # print("Logger user:", request.session['logged_user'])
    # lst = ["Python", "HTML", "CSS", "Javascript"]
    # now = datetime.datetime.now()
    places = Place.objects.all()
    return render(
        request=request,
        template_name='index.html', 
        context={ 
            # context: giá trị truyền qua cho temaplate html hiển thị
            # keys của context là các biến bên HTML sẽ gọi
            # 'logged_user': request.session['logged_user'],
            'places': places,
            
            }
        )

# Thứ tự 1 mới 1 functions view
# Bước 1: Viết cái hàm, render template cùng tên với tên hàm :))

@permission_required("myapp.list_places", login_url='/login',raise_exception=True)
def list_places(request):
    # Check user đã đangư nhập hay chưa ? 
    # Chưa đăng nhập: `AnonymousUser`
    # đăng nhập rồi: tên username
    user = request.user
    places = Place.objects.all()
    keyword = request.GET.get('keyword', None)
    if keyword: # Kiểm tra keyword có tồn tại hay không 
        # Lấy tất cả Place có name/address có chưa cái từ trong keyword
        places = Place.objects.filter(Q(name__contains=keyword) | Q(address__contains=keyword))
        print(places)
    paginator = Paginator(object_list = places, per_page= settings.PAGINATE_BY)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(
        request=request,
        template_name='place/list.html',
        context={
            'page_obj': page_obj
        }
    )

def search_places(request):
    places = []
    keyword = request.GET.get('keyword', None)
    if keyword:
        places = Place.objects.filter(Q(name__contains=keyword) | Q(address__contains=keyword))
    results = []
    for place in places:
        results.append({
            "id": place.id,
            "name": place.name,
            "address": place.address,
            "country": place.country
        })
    time.sleep(1)
    return JsonResponse({
            "results": results
        }, status = 200)

def validate_name(request):
    if request.method == "POST":
        name = request.POST['name']
        try:
            Place.objects.get(name=name)           
        except Place.DoesNotExist: # Là `Place` không có tồn tại
            return JsonResponse({
                "message": f"Bạn có thể sử dụng {name}"
            }, status = 200)
        return JsonResponse({
                "message": f"{name} đã tồn tại"
            }, status = 409) # 409 Conflict

# C (CREATE): Trong CURD
@permission_required("myapp.add_place", login_url='/login',raise_exception=True)
@login_required(login_url='/login') # Đặt decorator login_required để yêu cầu người đăng nhập thì mới thực hiện được view này
def add_place(request):
    user = request.user
    # if user.has_perm("myapp.add_place"):
    form = PlaceForm()
    if request.method == "POST":
        print(request.POST)
        form = PlaceForm(request.POST)
        if form.is_valid(): # Kiểmm tra/validate
            form.save()
            # redirect là chuyển về URL theo name được định nghĩa trong urls.py webapp
            return redirect('list_places')
            # HttpResponseRedirect là chuyển về chính xác cái URL prefix của view
            # return HttpResponseRedirect('/place/list')
        else:
            # Form data bị lỗi
            print(form.errors)
    return render(
        request=request,
        template_name='place/add.html',
        context={
            'form': form
        }
    )
    # return render(request, '403.html')

# R (READ): Trong CURD
@login_required(login_url='/login')
def view_detail_place(request, place_id): # pk là PrimaryKey = id
    try:
        print("Vô function->view_detail_place")
        place = Place.objects.get(id=place_id) # get_object_or_404(Place,id=place_id) #
        return render(
            request=request,
            template_name='place/detail.html',
            context={
                'place':place
            }
        )
    except BaseException as e:
        print("Error: ", e)
        return render(
            request=request,
            template_name='errors.html',
            context= {
                'error': e
            }
        )

# U (UPDATE): Trong CURD
@login_required(login_url='/login')
def update_place(request, place_id):
    try:
        place = Place.objects.get(id=place_id)
    except Place.DoesNotExist:
        return render(
            request=request,
            template_name='404.html'
        )
    form = PlaceForm(instance=place)
    print("request", request)
    print("request.method", request.method)
    if request.method == "POST":
        print("Method POST")
        # place.name = request.POST.get('name')
        place.address = request.POST.get('address')
        place.country = request.POST.get('country')
        place.save()
        # redirect là chuyển về URL theo name được định nghĩa trong urls.py webapp
        return redirect('list_places')
    return render(
        request=request,
        template_name='place/update.html',
        context={
            'form': form
        }
    )

# D (DELETE): CURD
@login_required(login_url='/login')
def confirm_delete(request, place_id):
    data = get_object_or_404(Place,id=place_id) #Place.objects.get(id=place_id)
    return render(
        request=request,
        template_name='place/confirm_detele.html',
        context={
            'data': data
        }
    )

def delete_place(request, place_id):
    place = get_object_or_404(Place,id=place_id) #Place.objects.get(id=place_id)
    place.delete() # Xoá đối tượng 
    return redirect('list_places')

def list_restaurants(request):
    restaurants = Restaurant.objects.all()
    return render(
        request=request,
        template_name='restaurant/list.html',
        context={
            'restaurants': restaurants
        }
    )

# C (CREATE): Trong CURD
@login_required(login_url='/login')
def add_restaurant(request):
    form = RestaurantForm()
    if request.method == "POST":
        print(request.POST)
        form = RestaurantForm(request.POST)
        if form.is_valid(): # Kiểmm tra/validate
            form.save()
            # redirect là chuyển về URL theo name được định nghĩa trong urls.py webapp
            return redirect('list_restaurants')
            # HttpResponseRedirect là chuyển về chính xác cái URL prefix của view
            # return HttpResponseRedirect('/place/list')
        else:
            # Form data bị lỗi
            print(form.errors)
    return render(
        request=request,
        template_name='restaurant/add.html',
        context={
            'form': form
        }
    )

@login_required(login_url='/login')
def update_restaurant(request, place_id):
    try:
        place = Place.objects.get(id=place_id)
        restaurant = Restaurant.objects.get(place=place)
    except Restaurant.DoesNotExist:
        return render(
            request=request,
            template_name='404.html'
        )
    form = RestaurantForm(instance=restaurant)
    if request.method == "POST":
        print(request.POST)
        restaurant.serves_pizza = True if request.POST.get('serves_pizza') == 'on' else False
        restaurant.serves_hot_dogs = True if request.POST.get('serves_hot_dogs') == 'on' else False
        restaurant.serves_pho = True if request.POST.get('serves_pho') == 'on' else False
        restaurant.save()
        # redirect là chuyển về URL theo name được định nghĩa trong urls.py webapp
        return redirect('list_restaurants')
    return render(
        request=request,
        template_name='restaurant/update.html',
        context={
            'form': form
        }
    )


def list_waiters(request):
    waiters = Waiter.objects.all()
    return render(
        request=request,
        template_name='waiter/list.html',
        context={
            'waiters': waiters
        }
    )
# C (CREATE): Trong CURD
@login_required(login_url='/login')
def add_waiter(request):
    form = WaiterForm()
    if request.method == "POST":
        print(request.POST)
        form = WaiterForm(request.POST)
        if form.is_valid(): # Kiểmm tra/validate
            form.save()
            # redirect là chuyển về URL theo name được định nghĩa trong urls.py webapp
            return redirect('list_waiters')
            # HttpResponseRedirect là chuyển về chính xác cái URL prefix của view
            # return HttpResponseRedirect('/place/list')
        else:
            # Form data bị lỗi
            print(form.errors)
    return render(
        request=request,
        template_name='waiter/add.html',
        context={
            'form': form
        }
    )


def list_articles(request):
    articles = Article.objects.all()
    return render(
        request=request,
        template_name='article.html',
        context={
            'articles': articles
        }
    )
