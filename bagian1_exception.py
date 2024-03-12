def division():
    try:
        num1 = float(input("Masukkan angka pertama: "))
        num2 = float(input("Masukkan angka kedua: "))
        result = num1 / num2
        return result
    except ZeroDivisionError:
        print("Error: Tidak dapat membagi dengan nol")
        return None

# Contoh pemanggilan fungsi
print(division())
