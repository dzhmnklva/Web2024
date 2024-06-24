a = int(input())
b = int(input())

start = int(a ** 0.5)  # Начальное число - корень из а, округленный вниз
end = int(b ** 0.5)  # Конечное число - корень из b, округленный вниз

for num in range(start, end + 1):
    square = num * num
    if a <= square <= b:
        print(square, end=" ")
