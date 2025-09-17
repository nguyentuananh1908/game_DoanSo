import random

# Máy tính chọn ngẫu nhiên 1 số từ 1 đến 100
secret_number = random.randint(1, 100)
guess = None

print("Chào mừng bạn đến với game Đoán số!")
print("Hãy thử đoán số từ 1 đến 100.")

# Vòng lặp cho đến khi đoán đúng
while guess != secret_number:
    guess = int(input("Nhập số bạn đoán: "))

    if guess < secret_number:
        print("Số bạn đoán nhỏ hơn rồi, thử lại nhé!")
    elif guess > secret_number:
        print("Số bạn đoán lớn hơn rồi, thử lại nhé!")
    else:
        print("🎉 Chúc mừng! Bạn đã đoán đúng số:", secret_number)
