import sys


def main():
    """
    Для чтения входных данных необходимо получить их
    из стандартного потока ввода (sys.stdin).
    Данные во входном потоке соответствуют описанному
    в условии формату. Обычно входные данные состоят
    из нескольких строк.
    Можно использовать несколько методов:
    * input() -- читает одну строку из потока без символа
    перевода строки;
    * sys.stdin.readline() -- читает одну строку из потока,
    сохраняя символ перевода строки в конце;
    * sys.stdin.readlines() -- вернет список (list) строк,
    сохраняя символ перевода строки в конце каждой из них.
    Чтобы прочитать из строки стандартного потока:
    * число -- int(input()) # в строке должно быть одно число
    * строку -- input()
    * массив чисел -- map(int, input().split())
    * последовательность слов -- input().split()
    Чтобы вывести результат в стандартный поток вывода (sys.stdout),
    можно использовать функцию print() или sys.stdout.write().
    Возможное решение задачи "Вычислите сумму чисел в строке":
    print(sum(map(int, input().split())))
    """
    n = int(input())

    ans = 1

    primes = []

    ndividers = []

    for i in range(2, n):
        is_prime = True
        for prime in primes:
            if i % prime == 0:
                is_prime = False
                break
        
        if is_prime:
            primes.append(i)
            if n % i != 0:
                ans += 1
            else:
                ndividers.append(i)
        else:
            has_common_divider = False
            for x in ndividers:
                if i % x == 0:
                    has_common_divider = True
                    break
            if not has_common_divider:
                ans += 1
    
    print(ans)


if __name__ == '__main__':
    main()