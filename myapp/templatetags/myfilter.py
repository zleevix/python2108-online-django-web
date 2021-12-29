from django import template
from django.conf import settings
register = template.Library() # Tạo biến để xác định các hàm python là filter 

@register.filter
def ly_thua(co_so, so_mu):
    return co_so**so_mu

# ly_thua(2,3) bình thường
# Trong Django template thì 2|ly_thua:3

@register.filter
def make_range(number):
    return range(1, number + 1)

@register.filter
def make_index_paginattion(current_page, index):
    # current_page = 3
    # index = 1
    # index-page = 11 = pagenate_by * (current_page - 1) + index
    return settings.PAGINATE_BY * (current_page - 1) + index