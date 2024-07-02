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
    words = list(input().split())
    pairs = {}
    max = 0
    max_pair = ''

    for word in words:
        i = 0
        word_len = len(word)
        while i + 1 < word_len:
            pair = word[i] + word[i + 1]
            if pairs.get(pair):
                pairs[pair] += 1
            else:
                pairs[pair] = 1
            if pairs[pair] >= max:
                if pairs[pair] == max:
                    max_pair = pair if pair > max_pair else max_pair
                else:
                    max_pair = pair
                max = pairs[pair]
            i += 1

    print(max_pair)


if __name__ == '__main__':
    main()