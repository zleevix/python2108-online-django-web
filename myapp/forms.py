from django.forms import ModelForm, Form, TextInput, Select, CheckboxInput, widgets, PasswordInput, EmailInput
from django.core.exceptions import ValidationError
from django.forms.fields import CharField, EmailField
from django.contrib.auth.models import User
from .models import Place, Restaurant, Waiter

class PlaceForm(ModelForm):
    class Meta:
        model = Place
        fields = '__all__' # ('name', 'address', 'country')
        widgets = {
            'name': TextInput(attrs={
                'class': 'form-control'
            }),
            'address': TextInput(attrs={
                'class': 'form-control'
            }),
            'country': TextInput(attrs={
                'class': 'form-control'
            }),
        }
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     print("Instances update: ", getattr(self,'instance'))
    # Tạo ra những cái hàm để validate data
    # vaidate cho name thì cần phải tạo tên hàm là clean_name
    # Valite cho `field` thì sẽ tạo hàm têm clean_`field`
    # Server validation
    # Tất cả các hàm bắt đầu là clean_<field> thì sẽ được chạy khi mà gọi .is_valid()
    def clean_name(self):
        name = self.cleaned_data['name']
        try:
            # objects.get -> Trả duy nhất 1 object nếu tìm thấy. Còn không thì raise lỗi
            Place.objects.get(name=name) # Lấy thử Place qua `name`
            # Nếu trả về thì đồng nghĩa đã có tồn tại -> Thông báo cho người dùng biết là `name` đã tồn tại.
            # Không trả giá trị về Place với `name` hiện tại là không có -> add thoải mái
            print("Instances update: ", getattr(self,'instance'))
            if hasattr(self,'instance'):
                return name
            raise ValidationError(f"{name} đã tồn tại. Vui lòng chọn name khác")
        except Place.DoesNotExist: # Là `Place` không có tồn tại
            return name
            
class RestaurantForm(ModelForm):
    class Meta:
        model = Restaurant
        fields = '__all__'
        widgets = {
            'place': Select(attrs={
                'class': 'form-control'
            }),
            'serves_hot_dogs': CheckboxInput(attrs={
                'class': 'form-check-input'
            }),
            'serves_pizza': CheckboxInput(attrs={
                'class': 'form-check-input'
            }),
            'serves_pho': CheckboxInput(attrs={
                'class': 'form-check-input'
            }),
        }

class WaiterForm(ModelForm):
    class Meta:
        model = Waiter
        fields = '__all__'
        widgets = {
            'restaurant': Select(attrs={
                'class': 'form-control'
            }),
            'serves_hot_dogs': CheckboxInput(attrs={
                'class': 'form-check-input'
            }),
            'serves_pizza': CheckboxInput(attrs={
                'class': 'form-check-input'
            }),
            'serves_pho': CheckboxInput(attrs={
                'class': 'form-check-input'
            }),
        }

# Form đăng ký
class RegistrationForm(Form):
    # username, password, email, first_name, last_name
    # username: không được trùng nhau
    username = CharField(
        label="Tên Đăng Nhập",
        help_text="Tên dùng để đăng nhập vào website",
        max_length="50",
        widget=TextInput(
            attrs={
                'class': 'form-control'
            }
        )
    )
    password = CharField(
        label="Mật Khẩu",
        widget=PasswordInput(
            attrs={
                'class': 'form-control'
            }
        )
    )
    # Trải nghiệm người dùng:
        # Nếu chỉ có lần nhập password thì 90% người dùng nhập sai và không biết sai ở đâu vì ẩn đi rồi.
        # Tăng trải nghiệm: thêm confirm_password
        # Nhập lần 2 về password thì nhập rất là kỹ.
    # Điều kiên: password và confirm_password phải giống nhau
    confirm_password = CharField(
        label="Nhập Lại Mật Khẩu",
        widget=PasswordInput(
            attrs={
                'class': 'form-control'
            }
        )
    )
    # email không trùng email. Đề phòng trường hợp gửi email
    email = EmailField(
        label="Địa Chỉ Email",
        widget=EmailInput(
            attrs={
                'class': 'form-control'
            }
        )
    )
    first_name = CharField(
        label="Tên",
        max_length="50",
        widget=TextInput(
            attrs={
                'class': 'form-control'
            }
        )
    )
    last_name = CharField(
        label="Họ",
        max_length="50",
        widget=TextInput(
            attrs={
                'class': 'form-control'
            }
        )
    )

    def clean_username(self):
        username = self.cleaned_data['username']
        try:
            User.objects.get(username=username) 
            raise ValidationError(f"Tên đăng nhập '{username}'' đã tồn tại. Vui lòng chọn tên đăng nhập khác")
        except User.DoesNotExist:
            return username

    def clean_confirm_password(self):
        password = self.cleaned_data['password']
        confirm_password = self.cleaned_data['confirm_password']
        if password != confirm_password:
            raise ValidationError(f"Mật khẩu không khớp. Vui lòng nhập lại")
        return confirm_password

    def clean_email(self):
        email = self.cleaned_data['email']
        try:
            User.objects.get(email=email) 
            raise ValidationError(f"Email '{email}'' đã tồn tại. Vui lòng chọn email khác")
        except User.DoesNotExist:
            return email
    # ModelForm là có sẳn hàm .save()
    # Form là phải tự viết
    def save_user(self):
        return User.objects.create_user(
            username=self.cleaned_data['username'],
            password=self.cleaned_data['password'],
            email=self.cleaned_data['email'],
            first_name=self.cleaned_data['first_name'],
            last_name=self.cleaned_data['last_name'],
        )

# Form đăng nhập
class LoginForm(Form):
    username = CharField(
        label="Tên Đăng Nhập",
        max_length="50",
        widget=TextInput(
            attrs={
                'class': 'form-control'
            }
        )
    )
    password = CharField(
        label="Mật Khẩu",
        widget=PasswordInput(
            attrs={
                'class': 'form-control'
            }
        )
    ) 