from django.conf import settings
from django.db import models
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView # R
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .models import Place, Restaurant, Waiter
from .forms import PlaceForm, RestaurantForm, WaiterForm

# R: CURD
class PlaceListView(ListView):
    # model = Place 
    # queryset = Place.objects.all()
    # Sử dụng ListView thì mình phải định nghĩa 1 trong cái:
    #   1. `model` # Chỉ lấy đc 1 model 
    #   2. `queryset` # Có thể kết hợp được nhiều model class với nhau
    #   3: Overide hàm `get_queryset()` # Giống queryset
    # Mặc định tempalate của ListView là templates/<tên app>/<tên class model>_list.html
    # Đổi tempalate bằng thuộc tính `template_name`
    template_name = 'class_base/list_view.html'

    # Biến có bên template là `object_list`
    # `Thay tên gợi nhớ` tên biến bên template
    context_object_name = 'all_places'

    # Thuộc tính để phân trang
    paginate_by = settings.PAGINATE_BY

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['class_name'] = 'PYTHON2108E-ONLINE: Addition context in ListView'
        return context

    def get_queryset(self):
        return Place.objects.all()

class PlaceDetailView(DetailView):
    model = Place
    # Mặc định tempalate của ListView là templates/<tên app>/<tên class model>_detail.html
    # Đổi tempalate bằng thuộc tính `template_name`
    template_name = 'class_base/detail_view.html'

    # Biến mặc định của DetailView là `object`
    context_object_name = 'place'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['class_name'] = 'PYTHON2108E-ONLINE: Addition context in DetailView'
        return context

# C: CRUD
@method_decorator(login_required(login_url='/login'), name="dispatch")
class PlaceCreateView(CreateView):
    model = Place
    # Phải có `fields`: trường nào sẽ được tạo ô input cho create view
    # Hoặc là `form_class` : Form mình muốn xài
    # fields = ('name', 'address')
    form_class = PlaceForm
    # <tên app>/<tên class>_form.html
    template_name = 'class_base/create_view.html'
    success_url = reverse_lazy('class_list_places')

@method_decorator(login_required(login_url='/login'), name="dispatch")
class PlaceUpdateView(UpdateView):
    model = Place
    # Phải có `fields`: trường nào sẽ được tạo ô input cho create view
    # Hoặc là `form_class` : Form mình muốn xài
    # fields = ('name', 'address')
    form_class = PlaceForm
    #  <tên app>/<tên class>_form.html
    template_name = 'class_base/update_view.html'
    success_url = reverse_lazy('class_list_places')

@method_decorator(login_required(login_url='/login'), name="dispatch")
class PlaceDeleteView(DeleteView):
    model = Place
    success_url = reverse_lazy('class_list_places')
    # <tên app>/<tên class>_confirm_delete.html
    template_name = 'class_base/confirm_delete_view.html'

# R: CURD
class RestaurantListView(ListView):
    model = Restaurant 
    # queryset = Place.objects.all()
    # Sử dụng ListView thì mình phải định nghĩa 1 trong cái:
    #   1. `model` # Chỉ lấy đc 1 model 
    #   2. `queryset` # Có thể kết hợp được nhiều model class với nhau
    #   3: Overide hàm `get_queryset()` # Giống queryset
    # Mặc định tempalate của ListView là templates/<tên app>/<tên class model>_list.html
    # Đổi tempalate bằng thuộc tính `template_name`
    template_name = 'class_base/list_view.html'

    # Biến có bên template là `object_list`
    # `Thay tên gợi nhớ` tên biến bên template
    context_object_name = 'all_restaurants'

    # Thuộc tính để phân trang
    paginate_by = settings.PAGINATE_BY

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['class_name'] = 'PYTHON2108E-ONLINE: Addition context in ListView'
        return context

class RestaurantDetailView(DetailView):
    model = Restaurant
    # Mặc định tempalate của ListView là templates/<tên app>/<tên class model>_detail.html
    # Đổi tempalate bằng thuộc tính `template_name`
    template_name = 'class_base/detail_view.html'

    # Biến mặc định của DetailView là `object`
    context_object_name = 'place'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['class_name'] = 'PYTHON2108E-ONLINE: Addition context in DetailView'
        return context

# C: CRUD
@method_decorator(login_required(login_url='/login'), name="dispatch")
class RestaurantCreateView(CreateView):
    model = Restaurant
    # Phải có `fields`: trường nào sẽ được tạo ô input cho create view
    # Hoặc là `form_class` : Form mình muốn xài
    # fields = ('name', 'address')
    form_class = RestaurantForm
    template_name = 'class_base/create_view.html'
    success_url = reverse_lazy('class_list_restaurants')

@method_decorator(login_required(login_url='/login'), name="dispatch")
class RestaurantUpdateView(UpdateView):
    model = Restaurant
    # Phải có `fields`: trường nào sẽ được tạo ô input cho create view
    # Hoặc là `form_class` : Form mình muốn xài
    # fields = ('name', 'address')
    form_class = RestaurantForm
    template_name = 'class_base/update_view.html'
    success_url = reverse_lazy('class_list_restaurants')

@method_decorator(login_required(login_url='/login'), name="dispatch")
class RestaurantDeleteView(DeleteView):
    model = Restaurant
    success_url = reverse_lazy('class_list_restaurants')
    template_name = 'class_base/confirm_delete_view.html'


# R: CURD
class WaiterListView(ListView):
    # model = Waiter 
    queryset = Waiter.objects.all()
    # Sử dụng ListView thì mình phải định nghĩa 1 trong cái:
    #   1. `model` # Chỉ lấy đc 1 model 
    #   2. `queryset` # Có thể kết hợp được nhiều model class với nhau
    #   3: Overide hàm `get_queryset()` # Giống queryset
    # Mặc định tempalate của ListView là templates/<tên app>/<tên class model>_list.html
    # Đổi tempalate bằng thuộc tính `template_name`
    template_name = 'class_base/list_view.html'

    # Biến có bên template là `object_list`
    # `Thay tên gợi nhớ` tên biến bên template
    context_object_name = 'all_waiters'

    # Thuộc tính để phân trang
    paginate_by = settings.PAGINATE_BY

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['class_name'] = 'PYTHON2108E-ONLINE: Addition context in ListView'
        return context

class WaiterDetailView(DetailView):
    model = Waiter
    # Mặc định tempalate của ListView là templates/<tên app>/<tên class model>_detail.html
    # Đổi tempalate bằng thuộc tính `template_name`
    template_name = 'class_base/detail_view.html'

    # Biến mặc định của DetailView là `object`
    context_object_name = 'place'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['class_name'] = 'PYTHON2108E-ONLINE: Addition context in DetailView'
        return context

# C: CRUD
@method_decorator(login_required(login_url='/login'), name="dispatch")
class WaiterCreateView(CreateView):
    model = Waiter
    # Phải có `fields`: trường nào sẽ được tạo ô input cho create view
    # Hoặc là `form_class` : Form mình muốn xài
    # fields = ('name', 'address')
    form_class = WaiterForm
    template_name = 'class_base/create_view.html'
    success_url = reverse_lazy('class_list_waiters')

@method_decorator(login_required(login_url='/login'), name="dispatch")
class WaiterUpdateView(UpdateView):
    model = Waiter
    # Phải có `fields`: trường nào sẽ được tạo ô input cho create view
    # Hoặc là `form_class` : Form mình muốn xài
    # fields = ('name', 'address')
    form_class = WaiterForm
    template_name = 'class_base/update_view.html'
    success_url = reverse_lazy('class_list_waiters')

@method_decorator(login_required(login_url='/login'), name="dispatch")
class WaiterDeleteView(DeleteView):
    model = Waiter
    success_url = reverse_lazy('class_list_waiters')
    template_name = 'class_base/confirm_delete_view.html'

