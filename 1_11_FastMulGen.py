# Реализуйте генератор программ fast_mul_gen(y) для примеров из задачи 4.
# Воспользуйтесь ранее полученным кодом fast_mul. Ваша функция должна выдать текст функции f(x) (умножение на ранее заданный y), 
# тело которой состоит из некоторого числа присваиваний. Для вывода функции используйте print. Добавьте автоматическое тестирование. 
# Объясните, почему в общем случае у вас получается большее количество сложений, чем в примерах из задачи 4.

def gen(num):
    print("def f(n):")
    if num == 0:
        print("    return 0")
    else:
        first = True
        retStr = "    return "
        digit_num = 0
        while (num != 0):
            if num % 2 == 1:
                if (first):
                    retStr += " (n << " + str(digit_num) + ")"
                    first = False
                else:
                    retStr += " + (n << " + str(digit_num) + ")"
            digit_num += 1
            num //= 2
        print(retStr)
            

def fast_mul_gen(num):
    print("def f(n):")
    if num == 0:
        print("    return 0")
    else:
        first = True
        current_digit = 0
        retStr = "    return "
        number_of_digit = len(str(bin(num))) - 2
        print("    x1 = n")
        for i in range(1, number_of_digit):
            print("    x" + str(2**i), "= x" + str(2**(i-1)), "+ x" + str(2**(i-1)))
        while (num != 0):
            if num % 2 == 1:
                if (first):
                    retStr += "x" + str(2**current_digit)
                    first = False
                else:
                    retStr += " + x" + str(2**current_digit)
            current_digit += 1
            num //= 2
        
        print(retStr)

def f(n):
    x1 = n
    x2 = x1 + x1
    x4 = x2 + x2
    x8 = x4 + x4
    x16 = x8 + x8
    x32 = x16 + x16
    return x1 + x4 + x16 + x32

x = 53
fast_mul_gen(x)
for i in range(100):
    if f(i) != i * x:
        raise Exception("ERROR, input:", i)
    
