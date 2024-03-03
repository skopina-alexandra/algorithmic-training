import sys
sys.set_int_max_str_digits(70000)

import time;


n, k, d = map(int,input().split())

start = time.time()

result = n
answer_exists = True

i = 0

while i < d and answer_exists:
    result *= 10
    remainder = result % k

    if remainder > 0:
        add = k - remainder
        if add < 10:
            result += add
        else:
            answer_exists = False

    i += 1
    

if not answer_exists:
    result = -1

print (result)

end = time.time();

print ('time', end - start)