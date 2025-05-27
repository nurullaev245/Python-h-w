


user_input = int(input("Iltimos, 2 xonali son kiriting: "))

is_two_digit = (user_input >= 10 and user_input <= 99)

print(user_input, "- bu 2 xonali son." if is_two_digit else user_input, "- bu 2 xonali son emas.")

