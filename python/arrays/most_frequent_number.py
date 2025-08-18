# ================ Cách 1 ==============================
number = list(map(int, input('Nhập dãy số: ').split()))

# tạo 1 dictionary để lưu cặp giá trị
freg = {}
for num in number:
    if num in freg:
        freg[num] += 1
    else: freg[num] = 1

max_count = -1
most_freg = None

for num, count in freg.items():
    if count > max_count:
        max_count = count
        most_freg = num

print('Số xuất hiện nhiều nhất: ', most_freg)
print('Số lần xuất hiện: ', max_count)


# ================ Cách 2 ==============================
number = list(map(int, input('Nhập các phần tử: ').split()))

number.sort()

max_count = 1
most_freg = number[0]
current_count = 1

for i in range(1, len(number)):
    if number[i] == number[i - 1]:
        current_count += 1
    else: current_count = 1

    if current_count > max_count:
        max_count = current_count
        most_freg = number[i]

print('Số xuất hiện nhiều nhất: ', most_freg)
print('Số lần xuất hiện nhiều nhất: ', max_count)