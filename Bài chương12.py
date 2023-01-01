f = open("bai_tho.txt",'r',encoding = 'utf-8')
a = f.read(25)   #đọc 25 kí tự đầu tiên
print("Nội dung 25 kí tự đầu tiên là:\n", a)
b = f.read(35)   #đọc 35 kí tự tiếp theo
print("Nội dung 35 kí tự tiếp theo là:\n", b)
c = f.read()     #đọc phần còn lại
print("Nội dung phần còn lại là:\n, c")