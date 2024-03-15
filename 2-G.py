t = int(input())

for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    cur_idx = -1
    count = 0
    lengths = []

    while cur_idx < n - 1:
        cur_idx += 1
        cur_min = a[cur_idx]
        cur_length = 1
        while cur_min > cur_length and cur_idx < n - 1:
            cur_idx += 1
            if a[cur_idx] < cur_length + 1:
                cur_min = a[cur_idx]
                cur_idx -= 1
            else:
                cur_length += 1
                cur_min = min(cur_min, a[cur_idx])

        count += 1
        lengths.append(cur_length)

    print(count)
    print(' '.join(map(str, lengths)))
