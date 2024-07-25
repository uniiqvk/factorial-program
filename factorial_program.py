import math

def get_positive_integer():
    while True:
        try:
            user_input = input("Введите положительное целое число: ")
            number = int(user_input)
            if number < 0:
                raise ValueError("Число должно быть положительным.")
            return number
        except ValueError as e:
            print(f"Ошибка ввода: {e}. Попробуйте еще раз.")

def calculate_factorial(number):
    return math.factorial(number)

def main():
    number = get_positive_integer()
    factorial = calculate_factorial(number)
    print(f"Факториал числа {number} равен {factorial}")

if __name__ == "__main__":
    main()
