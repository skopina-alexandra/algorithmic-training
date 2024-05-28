
def set_t_cur(t_cur, tx):
    if tx >= 0:
        if t_cur >= 0:
            t_cur = min(t_cur, tx)
        else:
            t_cur = tx
    return t_cur

def getTime(l, s01, v1, s02, v2):


    if abs(l/2 - s01) != abs(l/2 - s02) and v1 == 0 and v2 == 0:
        return -1

    if abs(l/2 - s01) == abs(l/2 - s02):
        return 0

    if abs(v1) < abs (v2):
        s01, s02 = s02, s01
        v1, v2 = v2, v1

    i = 0
    j = 1
    t_cur = -1.0
    found = False

    while not found:
        i += 1
        j = 1
        il2 = i * l / 2

        while j <= i and not found:

            jl2  = j * l / 2

            x = -1 * v1 + v2

            if x != 0:
                tx = (jl2 - s02 + il2 + s01) / x # 1
                t_cur = set_t_cur(t_cur, tx)

                tx = (jl2 - s02 - il2 + s01) / x # 5
                t_cur = set_t_cur(t_cur, tx)

                tx = (-jl2 - s02 -il2 + s01) / x # 9
                t_cur = set_t_cur(t_cur, tx)

            x = v1 + v2

            if x != 0:
                tx = (jl2 - s02 + il2 - s01) / x # 2
                t_cur = set_t_cur(t_cur, tx)

                tx = (jl2 - s02 - il2 - s01) / x # 4
                t_cur = set_t_cur(t_cur, tx)

            x = v1 - v2

            if x != 0:
                tx = (jl2 + s02 + il2 - s01) / x # 3
                t_cur = set_t_cur(t_cur, tx)

                tx = (-jl2 + s02 - il2 - s01) / x # 7
                t_cur = set_t_cur(t_cur, tx)

            x = -v1 - v2

            if x != 0:
                tx = (jl2 + s02 - il2 + s01) / x # 6
                t_cur = set_t_cur(t_cur, tx)

                tx = (-jl2 + s02 - il2 + s01) / x # 8
                t_cur = set_t_cur(t_cur, tx)

            a = s01 + v1 * t_cur
            b = s02 + v2 * t_cur
            found = (i * l >= abs(a) or j * l >= abs(b)) and abs(l/2 - abs(a % l)) - abs(l/2 - abs(b % l)) < 0.0000001
            j += 1

            if i > 5:
                return -1

    return t_cur



l, s01, v1, s02, v2 = map(int, input().split())

t = getTime(l, s01, v1, s02, v2)

if t < 0:
    print('NO')
else:
    print('YES')
    print(t)