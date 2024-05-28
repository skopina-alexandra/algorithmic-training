input()

first = set(list(map(int, input().split())))
input()

second = set(list(map(int, input().split())))
input()

third = set(list(map(int, input().split())))

common = first.intersection(second).union(first.intersection(third)).union(second.intersection(third))

print(' '.join(map(str, sorted(common))))