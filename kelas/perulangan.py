# range(start, stop, step)

# batas = 5
# for i in range(batas):
#     print("Perulangan ke-", i)


# jawab = input("Do you love me? ")
# while jawab != "yes":
#     print("Please love me")
#     jawab = input("Do you love me? ")

# print("I love you too darling!")

# for i in range(30):
#     if i % 2 == 0:
#         print(i, "adalah bilangan genap")
#     print(i)

saldo = 1000000
total_belanja = int(input("Masukkan total belanja: "))
while total_belanja < saldo:
    saldo -= total_belanja
    print("Sisa saldo anda adalah: ", saldo)
    total_belanja = int(input("Masukkan total belanja: "))

print("Saldo anda tidak cukup untuk belanja!")
