def kt_snt(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

number = int(input("nhap so can ktra: "))

if kt_snt(number):
    print(number, "la so nguyen to")
else:
    print(number, " ko la so nguyen to")