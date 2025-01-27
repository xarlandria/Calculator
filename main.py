
#Функция сложения
def addition(num1: float, num2: float) -> float:
    return num1 + num2

#Функция вычитания
def subtraction(num1: float, num2: float) -> float:
    return num1 - num2

#Функция обычного деления
def division(num1: float, num2: float) -> float:
    return num1 / num2

#Функция целочисленного деления
def integer_division(num1: float, num2: float) -> float:
    return num1 // num2

#Функция деления с остатком
def division_with_remainder(num1: float, num2: float) -> float:
    return num1 % num2

#Функция умножения
def multiplication(num1: float, num2: float) -> float:
    return num1 * num2

#Функция ввода чисел и выбора математической операции
def main():
    print('Программа "Калькулятор". Введите два числа, чтобы продолжить:')
    try:
        number_1 = float(input("Первое число: "))
        number_2 = float(input("Второе число: "))
        print('''Теперь я попрошу тебя выбрать математическую операцию (введи символ или название): 
                # +: сложение;
                # -: вычитание;
                # /: обычное деление;
                # //: целочисленное деление;
                # %: деление с остатком;
                # *: умножение.''')
        selected_operation = input("Ваш выбор: ")
        match selected_operation:
            case '+' | 'Сложение' | 'сложение':
                print(addition(number_1, number_2))
            case '-' | 'Вычитание' | 'вычитание':
                print(subtraction(number_1, number_2))
            case '/' | 'Обычное деление' | 'обычное деление':
                print(division(number_1, number_2))
            case '//' | 'Целочисленное деление' | 'целочисленное деление':
                print(integer_division(number_1, number_2))
            case '%' | 'Деление с остатком' | 'деление с остатком':
                print(division_with_remainder(number_1, number_2))
            case '*' | 'Умножение' | 'умножение':
                print(multiplication(number_1, number_2))
            case _:
                print('Выбрана неизвестная операция!')
    except ValueError:
        print('Один или оба введенных аргумента не являются числами! ')
    except ZeroDivisionError:
        print('Делить на ноль нельзя!')

#Основная программа
main()
while True:
    decision = input('Посчитать что-нибудь еще? Ответь \'да\' или \'нет\': ')
    match decision:
        case 'да' | 'Да':
            main()
        case 'нет' | 'Нет':
            print('Возвращайтесь снова!')
            break
        case _:
            print('Неверный вариант выбора, попробуйте еще раз!')