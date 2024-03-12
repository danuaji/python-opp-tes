def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

# Contoh pemanggilan fungsi
year = int(input("Masukkan tahun: "))
if is_leap_year(year):
    print(f"{year} adalah tahun kabisat.")
else:
    print(f"{year} bukan tahun kabisat.")
