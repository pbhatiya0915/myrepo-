start = int(input("enter: "))

my_list = [start]
for _ in range(10):
    num = my_list[len(my_list)-1]
    if num % 2 == 0:
        num /= 2
    else:
        num *= 3
        num -= 1
    my_list.append(num)
print(my_list)
