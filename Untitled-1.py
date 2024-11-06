def gcd(a, b):
    # Selama b tidak sama dengan 0, lakukan pembagian Euclidean
    while b != 0:
        a, b = b, a % b
    return a

# Contoh penggunaan
num1 = int(input("Masukkan bilangan pertama: "))
num2 = int(input("Masukkan bilangan kedua  : "))

hasil_gcd = gcd(num1, num2)
print(f"FPB dari {num1} dan {num2} adalah {hasil_gcd}")