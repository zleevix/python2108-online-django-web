from django.shortcuts import render, redirect, HttpResponseRedirect, get_object_or_404
from django.http.response import HttpResponse, JsonResponse
from django.db.models import Q
from django.core.paginator import Paginator
from django.conf import settings
from django.contrib.auth import authenticate, login
from .forms import RegistrationForm, LoginForm

def register_user(request):
    register_form = RegistrationForm()
    if request.method == "POST":
        register_form = RegistrationForm(request.POST)
        if register_form.is_valid():
            new_user = register_form.save_user()
            user = authenticate(
                username=register_form.cleaned_data['username'],
                password=register_form.cleaned_data['password'],
            )
            login(request, user)
            return redirect('index')
    return render(
        request=request,
        template_name='user/register.html',
        context={
            'register_form': register_form
        }
    )


def login_user(request):
    login_form = LoginForm()
    message = ""
    if request.method == "POST":
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            # hàm authenticate nhận username/password người dùng gửi lên
            # Lấy trong db auth_user có đúng hay không ?
            user = authenticate(
                username=login_form.cleaned_data['username'],
                password=login_form.cleaned_data['password'],
            )
            if user:
                # Xác thực thành công
                # GIữ trạng thái user đang xác thực thành công
                login(request, user)
                print("Đăng nhập thành công")
                print(request.GET.get('next'))
                if request.GET.get('next'): # Kiểm tra url của mình có param `next`, nếu có chuyển về next
                    return HttpResponseRedirect(request.GET.get('next'))
                return redirect('index')
            else:
                message = "Thông in bạn nhập không đúng. Vui lòng kiểm tra lại"
                print("THông in bạn nhập không đúng. Vui lòng kieemr tra lại")
        else:
            print("Error", login_form.errors)

    return render(
        request=request,
        template_name='user/login.html',
        context={
            'login_form': login_form,
            'message': message
        }
    )
