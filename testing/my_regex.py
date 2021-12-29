# CHuỗi của người dùng là bắt đầu p
# kết thức n
# giữa p và n chỉ được phép thêm 3 ký tự bất kỳ.
string = "pabcn"
import re
pattern = "^p...n$"

# if string.startswith("p") and string.endswith("n") and len(string) == 5:
if re.match(pattern, string):
    print("Đạt yêu cầu")
else:
    print("NOK")

chuoi = "-623abc-5xyz-12k9l-2-p"
pattern = r"[a-zA-Z]+"
import re
print(list(map(str, re.findall(pattern, chuoi))))