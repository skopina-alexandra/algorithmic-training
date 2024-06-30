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

    primes = generate_primes(n)

    if n in primes:
        print(n-1)
        return
    
    for i in range(2, n):
        is_mutually_simple = True
        for prime in primes:
            if prime > i:
                break
            if i % prime == 0:
                is_mutually_simple = False
                break
        ans += 1 if is_mutually_simple else 0
    
    print(ans)

 
is_prime = lambda number: all(number % i != 0 for i in range(2, int(number ** 0.5) + 1))

def generate_primes(n):
    primes = []
    for i in range (2, n + 1):
        if is_prime(i) and n % i == 0:
            primes.append(i)
    return primes


if __name__ == '__main__':
    main()