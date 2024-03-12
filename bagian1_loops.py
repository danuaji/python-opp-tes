def count_odd_numbers():
    count = 0
    for i in range(1, 51):
        if i % 2 != 0:
            count += 1
    return count

# Contoh pemanggilan fungsi
print("Jumlah bilangan ganjil dari 1 hingga 50 adalah:", count_odd_numbers())
