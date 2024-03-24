first = input()
second = input()

def isAnagram(first, second):

    first_letters = {}

    for ch in first:
        if first_letters.get(ch) != None:
            first_letters.update({ch: first_letters.get(ch) + 1})
        else:
            first_letters.update({ch: 1})

    for ch in second:
        if first_letters.get(ch) == None:
            return False
        else:
            first_letters.update({ch: first_letters.get(ch) - 1})
            if first_letters.get(ch) == 0:
                first_letters.pop(ch)

    return len(first_letters) == 0

result = isAnagram(first, second)

print('YES' if result else 'NO')