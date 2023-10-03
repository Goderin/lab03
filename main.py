n = int(input("Введите количество чисел: "))
arr = []
for i in range(n):
    arr.append(int(input("Введите число: ")))

direction = input("Выберите направление сортировки (возрастание/убывание): ")
if direction == "возрастание":
    for i in range(n-1):
        for j in range(n-1-i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
elif direction == "убывание":
    for i in range(n-1):
        for j in range(n-1-i):
            if arr[j] < arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

print("Отсортированный массив:")
for i in arr:
    print(i, end=" ")